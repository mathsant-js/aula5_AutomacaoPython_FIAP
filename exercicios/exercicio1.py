tamanho = int(input("Digite o tamanho do vetor: "))
numeros = []

# Usando método pronto de adicionar
for i in range(tamanho):
    numeros.append(float(input("Digite um número: ")))

print(numeros)

# Não usando nenhum método pronto
numeros = [0.0] * tamanho

for i in range(tamanho):
    numeros[i] = float(input("Digite um número: "))

print(numeros)