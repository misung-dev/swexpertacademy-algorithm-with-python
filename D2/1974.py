# 1974. 스도쿠 검증

T = int(input())
for test_case in range(1, T + 1):
    sdoq = []
    for i in range(9):
      row = list(map(int, input().split()))
      sdoq.append(row)
      result = 1
    
    # 가로줄 검사
    for r in range(9):
      if set(sdoq[r]) != set(range(1, 10)):
            result = 0
            break

    # 세로줄 검사
    for r in range(9):
      column_test = []
      for c in range(9):
        column_test.append(sdoq[c][r])
        column_test.sort()
      if set(column_test) != set(range(1, 10)):
        result = 0
        break

    # 3x3 격자 검사
    for i in range(0, 9, 3):
      for j in range(0, 9, 3):
        grid_test = []
        for x in range(3):
          for y in range(3):
            grid_test.append(sdoq[i + x][j + y])
        if set(grid_test) != set(range(1, 10)):
          result = 0
          break
      if result == 0:
        break

    print(f"#{test_case} {result}")

