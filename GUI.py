import tkinter as tk
from collections import deque
from PIL import Image, ImageTk


cols = 8  
rows = 8  
pos_x = (2, 2, 1, 1,-2,-1, -2, -1)
pos_y = (1,-1, 2,-2, 1, 2, -1, -2)
global knight_path
knight_path = []

def is_valid(x, y):
    return 0 <= x < cols and 0 <= y < rows

# def dfs(start, target):
#     status = [[False] * cols for _ in range(rows)]
#     status[start[0]][start[1]] = True

#     previous = [[None] * cols for _ in range(rows)]

#     stack = []
#     stack.append(start)

#     while stack:
#         x, y = stack.pop()

#         if (x, y) == target:
#             path = []
#             while (x, y) != start:
#                 path.append((x, y))
#                 x, y = previous[x][y]
#             path.append(start)
#             path.reverse()
#             return path

#         for i in range(8):
#             next_x = x + pos_x[i]
#             next_y = y + pos_y[i]
#             if is_valid(next_x, next_y) and not status[next_x][next_y]:
#                 status[next_x][next_y] = True
#                 previous[next_x][next_y] = (x, y)
#                 stack.append((next_x, next_y))

def bfs(start, target):
  status = [[False] * 8 for _ in range(8)]
  status[start[0]][start[1]] = True

  previous = [[None] * 8 for _ in range(8)]

  queue = deque()
  queue.append(start)
  while queue:
      x, y = queue.popleft()
        
      if (x,y) == target:
          path = []
          while (x, y) != start:
              path.append((x, y))
              x, y = previous[x][y]
          path.append(start)
          path.reverse()
          return path

      for i in range(8):
          next_x = x + pos_x[i]
          next_y = y + pos_y[i]
          if is_valid(next_x,next_y) and not status[next_x][next_y]:
              status[next_x][next_y] = True
              previous[next_x][next_y] = (x, y)
                
              queue.append((next_x, next_y))

def create_grid(event=None):
    colors = ["white", "black"]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]

            x0 = col * 64
            y0 = row * 64
            x1 = x0 + 64
            y1 = y0 + 64

            canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    


def move_knight_along_path():
    if not knight_path:
        return

    position = knight_path.pop(0)

    # index 'red' knight went
    x0 = position[0] * 64
    y0 = position[1] * 64
    canvas.create_rectangle(x0, y0, x0 + 64, y0 + 64, fill="red")

    # Create image
    knight_image = Image.open("Knight.png")
    knight_image = knight_image.resize((64, 64))
    knight_image = ImageTk.PhotoImage(knight_image)

    canvas.create_image(x0, y0, image=knight_image, anchor="nw")
    canvas.image = knight_image

    root.after(1000, move_knight_along_path)


def find_path():
    a = int(entry_start_x.get())
    b = int(entry_start_y.get())
    c = int(entry_target_x.get())
    d = int(entry_target_y.get())

    start_position = (a, b)
    target_position = (c, d)
    # shortest_path = dfs(start_position, target_position)
    shortest_path = bfs(start_position, target_position)
    global knight_path
    knight_path = shortest_path

    # result_label.config(text="Đường đi ngắn nhất: " + " -> ".join(map(str, knight_path)))
    move_knight_along_path()


root = tk.Tk()
root.title("Knight")
chessboard_frame = tk.Frame(root)
chessboard_frame.pack()


canvas = tk.Canvas(root, width=512, height=512)
canvas.pack(fill="both", expand=True)

canvas.bind("<Configure>", create_grid)

start_label = tk.Label(root, text="Tọa độ bắt đầu (x, y):")
start_label.pack()

entry_start_x = tk.Entry(root)
entry_start_x.pack()

entry_start_y = tk.Entry(root)
entry_start_y.pack()

target_label = tk.Label(root, text="Tọa độ đích (x, y):")
target_label.pack()

entry_target_x = tk.Entry(root)
entry_target_x.pack()

entry_target_y = tk.Entry(root)
entry_target_y.pack()

find_button = tk.Button(root, text="Tìm đường", command=find_path)
find_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
