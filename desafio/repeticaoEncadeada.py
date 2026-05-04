nomes = ["Ana", "Lara", "Luiz", "Caio"]

print("Não mostra duplas repetidas com variável temporária")
# Não mostra duplas repetidas com variável temporária
for i in range(len(nomes)):
    temp = 1
    for j in range(len(nomes)):
        if temp < len(nomes) and nomes[i] != nomes[temp]:
            print(f"{nomes[i]} + {nomes[temp]}")
            temp += 1
print()

print("Não mostra duplas repetidas")
# Não mostra duplas repetidas
for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        print(f"{nomes[i]} + {nomes[j]}")

print()

print("Mostra duplas repetidas")

# Mostra duplas repetidas
for i in range(len(nomes)):
    for j in range(len(nomes)):
        if j < len(nomes) and nomes[i] != nomes[j]:
            print(f"{nomes[i]} + {nomes[j]}")