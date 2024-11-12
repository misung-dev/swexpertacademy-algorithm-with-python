# 1959. 두 개의 숫자열

test = int(input())

for t in range(1, test+1):
  n, m = map(int, input().split())

  i_arr = list(map(int, input().split()))
  j_arr = list(map(int, input().split()))

  if len(i_arr) <= len(j_arr):
    long_arr = j_arr
    short_arr = i_arr
  else:
    long_arr = i_arr
    short_arr = j_arr

  max_sum = 0
  for l in range(len(long_arr) - len(short_arr) + 1):
    sum = 0
    for s in range(len(short_arr)):
      sum += short_arr[s] * long_arr[l+s]

    if sum >= max_sum:
      max_sum = sum

  print(f"#{t} {max_sum}")