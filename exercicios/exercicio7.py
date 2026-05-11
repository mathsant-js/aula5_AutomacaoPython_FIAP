matriz = [
    [0.0] * 4,
    [0.0] * 4,
    [0.0] * 4
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = input(f"Digite o valor para matriz[{i}][{j}]: ")

# Loop Tradicional
print("\n====Loop Tradicional====")
for i in range(len(matriz)):
    print("[", end=" ")
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=", ")
    print("]", end="")
    print()

# For-each
print("\n====For-each====")
for m in matriz:
    for n in m:
        print(n, end=" ")
    print()