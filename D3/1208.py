# 1208. [S/W 문제해결 기본] 1일차 - Flatten

for t in range(1, 11):
  num = int(input())
  box = list(map(int, input().split()))

  for n in range(num): 
    max_n = box.index(max(box))
    box[max_n] -= 1
    min_n = box.index(min(box))
    box[min_n] += 1

  gap = max(box) - min(box)

  print(f"#{t} {gap}")