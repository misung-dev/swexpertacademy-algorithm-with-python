# 2071. 평균값 구하기

test = int(input())

for t in range(1, test+1):
  n_list = list(map(int, input().split()))

  sum = 0
  for i in n_list:
    sum += i

  value = round(sum/len(n_list))


  print(f"#{t} {value}")