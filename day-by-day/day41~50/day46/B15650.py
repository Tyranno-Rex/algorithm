# from itertools import permutations
# p = permutations(range(1, n+1), m)
# for i in p:
#     print(" ".join(map(str, i)))

n, m = map(int, input().split())
def dfs(st):
    if len(st) == m:
        print(" ".join(map(str, st)))
        return
    for i in range(1, n+1):
        if i not in st and (len(st) == 0 or i > st[-1]):
            st.append(i)
            dfs(st)
            st.pop()

dfs([])
