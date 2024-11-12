# 2001. 파리 퇴치

test = int(input())

for t in range(1, test+1):
  n, m = map(int, input().split())

  matrix = []
  for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

  max_sum = 0
  for i in range(n-m+1):
    for j in range(n-m+1):
      sum = 0
      for x in range(m):
        for y in range(m):
          sum += matrix[i+x][j+y]
      
      if sum >= max_sum:
        max_sum = sum

  print(f"#{t} {max_sum}")