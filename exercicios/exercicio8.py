def preencher_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Digite um valor para matriz[{i}][{j}]: "))

def inserir_tamanho_matriz(linha, coluna):
    return [[0.0 for _ in range(coluna)] for _ in range(linha)]

linha = 2
coluna = 2

matriz_A = inserir_tamanho_matriz(linha, coluna)

matriz_B = inserir_tamanho_matriz(linha, coluna)

soma_matriz = inserir_tamanho_matriz(linha, coluna)

print("====Prenchendo Matriz A====")
preencher_matriz(matriz_A)

print("\n====Prenchendo Matriz B====")
preencher_matriz(matriz_B)

for i in range(len(matriz_A)):
    for j in range(len(matriz_A[i])):
        soma_matriz[i][j] = matriz_A[i][j] + matriz_B[i][j]

print("\n====Soma Matriz====")

for lista in soma_matriz:
    for item in lista:
        print(item, end=" ")
    print()