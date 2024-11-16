# 1979. 어디에 단어가 들어갈 수 있을까

test = int(input())

for t in range(1, test+1):
  n, k = map(int, input().split())
  puzzle = []
  result = 0

  for _ in range(n):
    row = list(map(int, input().split()))
    puzzle.append(row)

  # 가로 방향 검사
  for c in range(n):
    r = 0
    
    while r <= n-k:
      row_puzzle = [1] * k
      if puzzle[c][r:r+k] == row_puzzle:
        left_valid = (r==0 or puzzle[c][r-1]==0)
        right_valid = (r == n-k or puzzle[c][r+k]==0)
        if left_valid and right_valid:
          result += 1
        r += k
      else:
        r += 1

  # 세로 방향 검사
  for r in range(n):
    c=0
    while c <= n-k:
      col_puzzle = [puzzle[c+i][r] for i in range(k)]
      if col_puzzle == [1] * k:
        top_valid = (c == 0 or puzzle[c-1][r] == 0 )
        bottom_valid = (c+k == n or puzzle[c+k][r] == 0)
        if top_valid and bottom_valid:
          result += 1
        c += k
      else:
        c += 1

  print(f"#{t} {result}")