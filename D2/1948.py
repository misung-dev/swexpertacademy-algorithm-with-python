# 1948. 날짜 계산기

t = int(input())
months=[31,28,31,30,31,30,31,31,30,31,30,31]

for tc in range(1, t+1):
  m1,d1, m2, d2 = map(int, input().split())
  days = 1

  if m1 != m2 :
    # 첫달 남은 날짜
    days += months[m1-1] - d1
    
    # 중간
    if m2 - m1 > 1:
      days += sum(months[m1:m2-1])

    # 잉여
    days += d2
  
  # 같은달
  else:
    days += d2 - d1
    
  print(f"#{tc} {days}")
  