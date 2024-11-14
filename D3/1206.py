# 1206. [S/W 문제해결 기본] 1일차 - View

for t in range(1, 11):
  len = int(input())
  buildings = list(map(int, input().split()))
  result = 0

  for i in range(2, len-2):
    building_range = buildings[i-2:i+3]
    current = buildings[i]
    highest = max(building_range)

    if highest == current:
      building_range.remove(current)
      second_highest = max(building_range)
      result += highest - second_highest

  print(f"#{t} {result}")
