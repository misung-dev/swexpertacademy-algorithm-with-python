# 2072. 홀수만 더하기

num = int(input())

for i in range(1, num+1):
  n_list = list(map(int, input().split()))
  sum = 0

  for n in n_list:
    if (n % 2 == 1):
      sum += n

  print("#{} {}".format(i, sum))