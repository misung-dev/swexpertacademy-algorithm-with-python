# 2063. 중간값 찾기

num = int(input())
n_list = list(map(int, input().split()))

mid = len(n_list)//2
n_list.sort()

print(n_list[mid])