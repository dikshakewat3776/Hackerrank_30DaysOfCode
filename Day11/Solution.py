matrix = []
arrsum = []

for i in range(6):
    arr = list(map(int, input().strip().split()))
    matrix.append(arr)

def calculate(i,j):
    return(matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2])

for i in range(0,4):
    for j in range(0,4):
        res = calculate(i,j)
        arrsum.append(res)

print(max(arrsum))
