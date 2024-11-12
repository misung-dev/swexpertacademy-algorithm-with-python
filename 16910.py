# 6910. 원 안의 점 

test = int(input())

for i in range(1, test+1):
  n = int(input())
  count = 0
  
  for x in range(-n, n+1):
    for y in range (-n, n+1):
      if x**2 + y**2 <= n**2:
        count += 1

  print(f"#{i} {count}")
