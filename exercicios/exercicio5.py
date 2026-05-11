def lista_inversa_nomes(nomes):
    print("=====Lista de Nomes Reversa=====")
    for i in range(len(nomes) - 1, -1, -1):
        print(nomes[i])
    print("==============")

nomes = []

while True:
    resposta = input("\nDigite um nome: ")
    print()

    if resposta == "":
        if len(nomes) > 0:
            lista_inversa_nomes(nomes)
        print("Programa Encerrado")
        break

    nomes.append(resposta)
    lista_inversa_nomes(nomes)