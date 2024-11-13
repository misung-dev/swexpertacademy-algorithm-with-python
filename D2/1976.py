# 1976. 시각 덧셈

test = int(input())

for t in range(1, test+1):
  h1, m1, h2, m2 = map(int, input().split())
  
  m = m1 + m2
  h = h1 + h2 + (m // 60)
  m %= 60

  h = (h - 1) % 12 + 1  # 12시간제로 변환 (0은 12로 처리)  
  # if h > 12:
  #   h %= 12

  # if h == 0:
  #   h = 12  

  print(f"#{t} {h} {m}")