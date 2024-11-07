# 21425. +=

num = int(input())

for i in range(num):
  x, y, n = map(int, input().split())
  count = 1

  while (x+y) <=n:
    if x > y:
      y += x
    else:
      x += y
    count += 1
  print(count)