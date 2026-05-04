lista_frutas = ["Maçã", "Banana", "Pêssego"]

# lista_fruta[0] = "Maçã"
# lista_fruta[1] = "Banana"
# lista_fruta[2] = "Pêssego"

print(lista_frutas[0])

lista_frutas.append("Uva")
print(lista_frutas)
# lista_fruta[3] = "Uva"

# for tradicional
for i in range(len(lista_frutas)):
    print(lista_frutas[i])

# for-each
for fruta in lista_frutas:
    print(fruta)