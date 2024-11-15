# 1989. 초심자의 회문 검사

test = int(input())

for t in range(1,test+1):
  word = input()
  mid = len(word)//2
  left = word[:mid]  
  
  if len(word)%2 == 1:
    right = word [mid+1:len(word)]  
  else: 
    right = word [mid:len(word)]
  
  right_reserved = right[::-1]

  if left == right_reserved:
    result = 1
  else:
    result = 0

  print(f"#{t} {result}")
