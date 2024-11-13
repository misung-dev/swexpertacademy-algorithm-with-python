# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

test = int(input())

for _ in range(1, test+1):
  t = int(input())
  n = list(map(int, input().split()))

  n_dic = {}
  for i in n:
    if i not in n_dic:
      n_dic[i] = 1
    else:
      n_dic[i] += 1
  
  max_key = max(n_dic, key = n_dic.get)

  print(f"#{t} {max_key}")