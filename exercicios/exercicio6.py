while True:
    resposta = int(input("Digite o tamanho da lista: "))

    if resposta > 0:
        break
    print()
    print("ERRO: O número não pode ser negativo ou zero")

lista = []

for i in range(resposta):
    lista.append(input("Digite algo: "))

for i in range(resposta - 1, -1, -1):
    if i == 0:
        print(lista[i])
    else:
        print(lista[i], end = ", ")
    