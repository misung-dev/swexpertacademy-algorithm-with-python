# 1961. 숫자 배열 회전 

T = int(input())

for t in range(1, T+1):
  print(f"#{t}")
  num = int(input())
  N = []
  result = []
  
  for n in range(num):
    row = list(map(int, input().split()))
    N.append(row)
  

  # 90도 회전
  for i in range(num):
    word = ''
    for j in range(num-1, -1, -1):
      word += str(N[j][i])
    result.append(word)
    
  # 180도 회전
  for i in range(num-1, -1, -1):
    word = ''
    for j in range(num-1, -1, -1):
      word += str(N[i][j])
    result.append(word)
  
  # 270도 회전 
  for i in range(num-1, -1, -1):
    word = ''
    for j in range(num):
      word += str(N[j][i])
    result.append(word)
    
  final = []
  for i in range(num):
    for j in range(3):
      print(result[j*num + i], end=' ')
    print()
  

