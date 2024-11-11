# 1926. 간단한 369게임

test = int(input())
game = []

for t in range(1, test+1):
  str_t = str(t)

  clap = 0
  
  str_t = str_t.replace('3', '-')
  str_t = str_t.replace('6', '-')
  str_t = str_t.replace('9', '-')
  
  if '-' in str_t:
    clap = str_t.count('-')
    str_t = '-' * clap

  game.append(str_t)

print(" ".join(map(str, game)))
