texto = "FIAP Paulista"

print(texto[0])

tamanho = len(texto)
print(tamanho)
print()

for i in range(tamanho):
    print(f"texto[{i}] = {texto[i]}")

for c in texto:
    print(c)