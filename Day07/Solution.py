n = int(input())
lst  = list(map(int, input().split()))
res = []

if len(lst) == n:
    rev_lst = lst[::-1]
    for n in rev_lst:
        res.append(n)
    o = ' '.join(map(str, res))
    print(o)