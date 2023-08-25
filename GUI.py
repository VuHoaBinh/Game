import tkinter as tk
from collections import deque
from PIL import Image, ImageTk
import random

cols = 8
rows = 8
pos_x = (2, 2, 1, 1, -2, -1, -2, -1)
pos_y = (1, -1, 2, -2, 1, 2, -1, -2)import tkinter as tk
from collections import deque
from PIL import Image, ImageTk
import random
import time

cols = 8
rows = 8
pos_x = (2, 2, 1, 1, -2, -1, -2, -1)
pos_y = (1, -1, 2, -2, 1, 2, -1, -2)
knight_path = []

def is_valid(x, y):
	return 0 <= x < cols and 0 <= y < rows

def dfs(start, target):
	status = [[False] * cols for _ in range(rows)]

	status[start[0]][start[1]] = True

	previous = [[None] * cols for _ in range(rows)]

	stack = [start]
	while stack:
		x, y = stack.pop()

		if (x, y) == target:
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
			if is_valid(next_x, next_y) and not status[next_x][next_y]:
				status[next_x][next_y] = True
				previous[next_x][next_y] = (x, y)
				stack.append((next_x, next_y))

def bfs(start, target):
	status = [[False] * 8 for _ in range(8)]

	status[start[0]][start[1]] = True

	previous = [[None] * 8 for _ in range(8)]

	queue = deque([start])

	while queue:
		x, y = queue.popleft()

		if (x, y) == target:
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
			if is_valid(next_x, next_y) and not status[next_x][next_y]:
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


def move_knight_along_path_BFS():
	if not knight_path:
		return

	position = knight_path.pop(0)
	x0 = position[0] * 64
	y0 = position[1] * 64
	canvas.create_rectangle(x0, y0, x0 + 64, y0 + 64, fill="red")

	knight_image = Image.open("Knight.png").resize((64, 64))
	knight_image = ImageTk.PhotoImage(knight_image)
	canvas.create_image(x0, y0, image=knight_image, anchor="nw")
	canvas.image = knight_image

	root.after(1000, move_knight_along_path_BFS)


def move_knight_along_path_DFS():
	if not knight_path:
		return

	position = knight_path.pop(0)
	x0 = position[0] * 64
	y0 = position[1] * 64
	canvas.create_rectangle(x0, y0, x0 + 64, y0 + 64, fill="green")

	knight_image = Image.open("Knight.png").resize((64, 64))
	knight_image = ImageTk.PhotoImage(knight_image)
	canvas.create_image(x0, y0, image=knight_image, anchor="nw")
	canvas.image = knight_image

	root.after(1000, move_knight_along_path_DFS)
	
# time_flag = 0
def find_path(algorithm):
	# time_flag = 0
	start_x, start_y, target_x, target_y = map(int, (entry_start_x.get(), entry_start_y.get(), 
		entry_target_x.get(), entry_target_y.get()))

	start_position, target_position = (start_x, start_y), (target_x, target_y)

	global knight_path


	if algorithm == 'BFS':
		start_time = time.time()

		shortest_path = bfs(start_position, target_position)

		knight_path = shortest_path
		move_knight_along_path_BFS()

		end_time = time.time()
		execution_time = end_time - start_time
		result_label.config(text="TIME: {:.2f} giây".format(execution_time))
	else:
		start_time = time.time()

		shortest_path = dfs(start_position, target_position)
	
		knight_path = shortest_path
		move_knight_along_path_DFS()

		end_time = time.time()
		execution_time = end_time - start_time
		result_label.config(text="TIME: {:.2f} giây".format(execution_time))

root = tk.Tk()
root.title("Knight =)")

canvas = tk.Canvas(root, width=512, height=512)
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", create_grid)

start_label = tk.Label(root, text="Starting coordinates (x, y):")
entry_start_x = tk.Entry(root)
entry_start_y = tk.Entry(root)

target_label = tk.Label(root, text="End coordinates (x, y):")
entry_target_x = tk.Entry(root)
entry_target_y = tk.Entry(root)

find_button_BFS = tk.Button(root, text="BFS run", command=lambda: find_path("BFS"))
find_button_DFS = tk.Button(root, text="DFS run", command=lambda: find_path("DFS"))

result_label = tk.Label(root, text="")


start_label.pack()
entry_start_x.pack()
entry_start_y.pack()
target_label.pack()
entry_target_x.pack()
entry_target_y.pack()
find_button_BFS.pack()
find_button_DFS.pack()
result_label.pack()

root.mainloop()

knight_path = []

def is_valid(x, y):
    return 0 <= x < cols and 0 <= y < rows

def dfs(start, target):
    status = [[False] * cols for _ in range(rows)]
    status[start[0]][start[1]] = True
    previous = [[None] * cols for _ in range(rows)]
    stack = [start]

    while stack:
        x, y = stack.pop()

        if (x, y) == target:
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
            if is_valid(next_x, next_y) and not status[next_x][next_y]:
                status[next_x][next_y] = True
                previous[next_x][next_y] = (x, y)
                stack.append((next_x, next_y))

def bfs(start, target):
    status = [[False] * 8 for _ in range(8)]
    status[start[0]][start[1]] = True
    previous = [[None] * 8 for _ in range(8)]
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if (x, y) == target:
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
            if is_valid(next_x, next_y) and not status[next_x][next_y]:
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
    x0 = position[0] * 64
    y0 = position[1] * 64
    canvas.create_rectangle(x0, y0, x0 + 64, y0 + 64, fill="red")

    knight_image = Image.open("Knight.png").resize((64, 64))
    knight_image = ImageTk.PhotoImage(knight_image)
    canvas.create_image(x0, y0, image=knight_image, anchor="nw")
    canvas.image = knight_image

    root.after(1000, move_knight_along_path)

def find_path(algorithm):
    start_x, start_y, target_x, target_y = map(int, (entry_start_x.get(), entry_start_y.get(), 
    	entry_target_x.get(), entry_target_y.get()))

    start_position, target_position = (start_x, start_y), (target_x, target_y)

    global knight_path
    if algorithm == 'BFS':
        shortest_path = bfs(start_position, target_position)
    else:
        shortest_path = dfs(start_position, target_position)
    
    knight_path = shortest_path
    move_knight_along_path()

root = tk.Tk()
root.title("Knight")

canvas = tk.Canvas(root, width=512, height=512)
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", create_grid)

start_label = tk.Label(root, text="Starting coordinates (x, y):")
entry_start_x = tk.Entry(root)
entry_start_y = tk.Entry(root)

target_label = tk.Label(root, text="End coordinates (x, y):")
entry_target_x = tk.Entry(root)
entry_target_y = tk.Entry(root)

find_button_BFS = tk.Button(root, text="BFS run", command=lambda: find_path("BFS"))
find_button_DFS = tk.Button(root, text="DFS run", command=lambda: find_path("DFS"))

result_label = tk.Label(root, text="")

start_label.pack()
entry_start_x.pack()
entry_start_y.pack()
target_label.pack()
entry_target_x.pack()
entry_target_y.pack()
find_button_BFS.pack()
find_button_DFS.pack()
result_label.pack()

root.mainloop()
