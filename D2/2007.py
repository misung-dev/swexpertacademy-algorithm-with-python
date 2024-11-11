# 2007. 패턴 마디의 길이

test = int(input())

for t in range(1, test+1):
  original = str(input())
  pattern = ''

  for o in range(2, len(original)+1):
    pattern = original[:o]
    full_word = pattern * (len(original)//o) + pattern[:len(original)%o]

    if full_word == original:
      break
  
  print(f"#{t} {len(pattern)}")
