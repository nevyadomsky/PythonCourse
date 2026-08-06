n, m, k = int(input('RowsCount: ')), int(input('ColumnsCount: ')), int(input('BombsCount'))  # чтение размеров поля и числа мин

#################################################### заполнение поля нулями
a = []

for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append('0')

#################################################### расставляем мины
for i in range(k):
    row, col = int(input('BombRow ' + str(i) + ': ')), int(input('BombColumn ' + str(i) + ': '))
    # !!!!! можно делать -1 в зависимости как мы хотим считать
    a[row][col] = '*'

#################################################### делаем подсчет

for i in range(n):
    for j in range(m):
        if a[i][j] == '0':  # в этой клетке мины нет, поэтому считаем число мин вокруг
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, ai)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == '*':
                        a[i][j] = str(int(a[i][j]) + 1)
#################################################### вывод результата
print(*a, sep="\n")