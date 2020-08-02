n = int(input())    
binary = bin(n)[2:]
con = 0
res = 0

for i in binary:
    num = int(i)
    if num == 1:
        con += 1
        res = max(res, con)
    else:
        con = 0

print(res)
