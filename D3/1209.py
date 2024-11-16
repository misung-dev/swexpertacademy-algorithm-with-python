# 1209. [S/W 문제해결 기본] 2일차 - Sum

for _ in range(1, 11):
  t = int(input())
  arr = [list(map(int, input().split())) for _ in range(100)]

  # 가로 합
  row_sum = []
  for i in range(100): 
    r_total = 0
    
    for j in range(100):
      r_total += arr[i][j]
    row_sum.append(r_total)

  # 세로 합
  col_sum = []
  for j in range(100): 
    c_total = 0
    
    for i in range(100):
      c_total += arr[i][j]
    col_sum.append(c_total)
    
  # 대각선 합
  left_diag_sum = 0
  for i in range(100):
    left_diag_sum += arr[i][i]
    
  right_diag_sum = 0
  for i in range(100):
    right_diag_sum += arr[i][99-i]
      
  find_max_value = [max(row_sum), max(col_sum), left_diag_sum, right_diag_sum]
  result = max(find_max_value)
  
  print(f"#{t} {result}")

  