# 1215. [S/W 문제해결 기본] 3일차 - 회문1

def isPalindrome(word):
  mid = len(word) // 2
  left = word[:mid]
  right = word[-mid:]
  return left == right[::-1]
  
for t in range(1, 11):
  num = int(input())
  arr = []
  result = 0
  
  for _ in range(8):
    row = input()
    arr.append(row)
    
  # 가로 방향 검사
  for i in range(8):
    for j in range(8-num+1):
      word = arr[i][j:j+num]
      if isPalindrome(word):
        result += 1
        
  # 세로 방향 검사
  for j in range(8):
    for i in range(8-num+1):
      word = ''.join([arr[x][j] for x in range(i, i+num)])
      if isPalindrome(word):
        result += 1
      
  print(f"#{t} {result}")