quantidade_aluno = int(input("Digite a quantidade de alunos: "))
notas_turma = []
notas_acima = []
notas_na_media = []
notas_abaixo = []
media_turma = 0

for i in range(quantidade_aluno):
    notas_turma.append(float(input(f"Digite a {i + 1}ª nota: ")))
    media_turma += notas_turma[i]

media_turma /= quantidade_aluno

for i in range(quantidade_aluno):
    if notas_turma[i] > media_turma:
        notas_acima.append(notas_turma[i])
    elif notas_turma[i] < media_turma:
        notas_abaixo.append(notas_turma[i])
    else:
        notas_na_media.append(notas_turma[i])

print()
print("==== NOTAS MÉDIAS ====")
print(f"Média da Turma: {media_turma}")
print(f"Notas Acima da média: {notas_acima}")
print(f"Notas na Média: {notas_na_media}")
print(f"Notas Abaixo da Média: {notas_abaixo}")