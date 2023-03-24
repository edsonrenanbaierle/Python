# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.

def livedTime(day):
    year=0
    month=0
    dias=0
    while day>0:
        if day>=365:
            year+=1
            day-=365
        elif day>=30:
            month+=1
            day-=30
        else:
            dias+=1
            day-=1

    print("Voce ja viviu: {} ano(s), {} mes(es), {} dia(s)".format(year, month, dias))
        


days = int(input("Digite a quantidade de dias que você ja viveu: "))
livedTime(days)