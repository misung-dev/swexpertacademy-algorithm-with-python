# 1954. 달팽이 숫자

total = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(total):
  print(f"#{t+1}")
  num = int(input())

  snail = [[0] * num for _ in range(num)]

  x, y = 0, 0
  direction = 0

  for n in range(1, num*num + 1):
    snail[x][y] = n

    nx, ny = x + dx[direction], y + dy[direction]

    if nx < 0 or nx >= num or ny < 0 or ny >= num or snail[nx][ny] != 0:
      direction = (direction + 1) % 4
      nx, ny = x + dx[direction], y+ dy[direction]

    x, y = nx, ny

  for row in snail:
    print(" ".join(map(str, row)))

