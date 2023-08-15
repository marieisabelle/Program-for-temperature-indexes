soma = 0
media = 0
qtdMesesEscaldantes = 0
mesMaisEscaldante = -100
mesMenosQuente = 100
mesesAno = (["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])

for i in range(1,13):
    temp = float(input(f"Digite a temperatura máxima do mês {i} em graus Celsius: "))

    while not -90 <= temp <= 60:
        temp = float(input("Valor inválido. Digite dentro do intervalo -90°C a +60°C: "))

        #Temperatura média máxima anual
    soma += temp
    media = soma/12

        #Quantidade de meses escaldantes
    if temp > 40:
        qtdMesesEscaldantes += 1

        #Mês mais escaldante do ano
    if temp > mesMaisEscaldante:
        mesMaisEscaldante = temp
        mesMaisEscaldanteNome = mesesAno[i - 1]

        #Mês menos quente do ano
    if temp < mesMenosQuente:
        mesMenosQuente = temp
        mesMenosQuenteNome = mesesAno[i - 1]

print(f"Temperatura média máxima anual: {media:.2f} °C")
print(f"Quantidade de meses escaldantes: {qtdMesesEscaldantes}")
print(f"Mês mais escaldante do ano: {mesMaisEscaldanteNome} ({mesMaisEscaldante:.2f} °C)")
print(f"Mês menos quente do ano: {mesMenosQuenteNome} ({mesMenosQuente:.2f} °C)")