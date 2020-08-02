def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac
    
n =  int(input())
res = factorial(n)
print(res)
