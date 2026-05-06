meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(len(meses)):
    print(f"O Mês de {meses[i]} tem {dias_meses[i]} dias ao todo")
