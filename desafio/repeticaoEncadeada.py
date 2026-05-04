nomes = ["Ana", "Lara", "Luiz", "Caio"]

for i in range(len(nomes)):
    temp = 1
    for j in range(len(nomes)):
        if temp < len(nomes) and nomes[i] != nomes[temp]:
            print(f"{nomes[i]} + {nomes[temp]}")
            temp += 1
        