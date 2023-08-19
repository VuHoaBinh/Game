from collections import deque
a, b = map(int, input("Nhập điểm bắt đầu x, y: ").split())
c, d = map(int, input("Nhập điểm kết thúc x, y: ").split())

chess_board = [[0] * 8 for _ in range(8)]


pos_x = (2, 2, 1, 1,-2,-1, -2, -1)
pos_y = (1,-1, 2,-2, 1, 2, -1, -2)


def is_valid(x, y):
	return 0 <= x < 8 and 0 <= y < 8 and chess_board[x][y] == 0

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

start_position = (a,b)
target_position = (c,d)
shortest_path = bfs(start_position, target_position)
counter = 1


print("Đường đi ngắn nhất từ {} đến {}:".format(start_position, target_position))
for position in shortest_path:
	print(position)
	chess_board[position[0]][position[1]] = counter
	counter+=1
for row in chess_board:
    print(" ".join(map(str, row)))
# print(chess_board)