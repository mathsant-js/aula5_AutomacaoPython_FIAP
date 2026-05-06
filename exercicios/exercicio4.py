tamanho = int(input("Digite a quantidade de números que deseja calcular: "))
numeros = []
soma_numeros = 0

# Usando métodos prontos
for i in range(tamanho):
    num = float(input(f"Digite um número: "))
    numeros.append(num)
    soma_numeros += numeros[i]

print(f"Soma dos Números: {soma_numeros}")

# Sem usar métodos prontos
tamanho = int(input("Digite a quantidade de números que deseja calcular: "))
numeros = [0.0] * tamanho
soma_numeros = 0

for numero in numeros:
    numero = float(input(f"Digite um número: "))
    soma_numeros += numero

print(f"Soma dos Números: {soma_numeros}")