# 2805. 농작물 수확하기

test = int(input())

for t in range(1, test+1):
  n = int(input())
  mid = n//2
  farm = [] 

  for _ in range(n):
    farm.append(list(map(int, input().strip())))

  total_sum = 0
  for i in range(n):
    if i <= mid: 
      total_sum += sum(farm[i][mid - i: mid + i + 1])
    else: 
      total_sum += sum(farm[i][i - mid: n - (i - mid)])

  print(f"#{t} {total_sum}")