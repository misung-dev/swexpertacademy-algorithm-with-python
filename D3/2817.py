# 2817. 부분 수열의 합 (DFS)

tc = int(input())

def dfs(i, result):
  global count
  # 현재까지의 합이 목표 값 K와 같은 경우
  if result == K:
    count += 1
    return
  # 배열의 끝에 도달한 경우
  if i == N:
    return
  dfs(i+1, result+arr[i])
  dfs(i+1, result)

for t in range(1, tc+1):
  N, K = map(int, input().split())
  arr = list(map(int, input().split()))
  count = 0
  dfs(0,0)

  print(f"#{t} {count}")