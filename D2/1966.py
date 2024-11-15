# 1966. 숫자를 정렬하자

test = int(input())

for t in range(1, test+1):
  num = int(input())
  n_list = list(map(int, input().split()))

  n_list.sort()
  result = ' '.join(map(str, n_list))

  print(f"#{t} {result}")