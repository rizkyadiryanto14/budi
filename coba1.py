from numpy import *

data = array([
    [17, 20, 22, 27],
    [10, 15, 16.2, 18],
])

print('Matriks A=', data)

# === Metode Eliminasi Gauss === #
n = len(data)
for k in range(0, n-1):
    for i in range(k+1, n):
        m = data[i][k]/data[k][k]
        for j in range(0, n+1):
            data[i][j] = data[i][j]-m*data[k][j]

X = zeros((n, 1))
X[n-1][0] = data[n-1][n]/data[n-1][n-1]
for j in range(n-2, -1, -1):
    S = 0
    for i in range(j+1, n):
        S = S+data[j][i]*X[i][0]
        X[j][0] = (data[j][n] - S)/data[j][j]

print('X=', X)
