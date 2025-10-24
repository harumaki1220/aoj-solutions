n, m = map(int, input().split())

A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

b = []
for j in range(m):
    val = int(input())
    b.append(val)

for i in range(n):
    c_i = 0
    for j in range(m):
        c_i += A[i][j] * b[j]
    print(c_i)
