matriz = [
    [0.0] * 4,
    [0.0] * 4,
    [0.0] * 4
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = input("Digite algo: ")

for m in matriz:
    for n in m:
        print(n)