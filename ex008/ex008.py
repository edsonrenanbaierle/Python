# Na última aula de matemática, Rafael, Beto e Carlos aprenderam algumas novas funções matemáticas. Cada um deles se identificou com uma função em especial, e resolveram competir para ver quem tinha a função de maior resultado.

# A função que Rafael escolheu é r(x, y) = (3x)² + y².

# Já Beto escolheu a função b(x, y) = 2(x²) + (5y)².

# Carlos, por sua vez, escolheu a função c(x, y) = -100x + y³.

# Dados os valores x e y, diga quem escolheu a função com o maior resultado.

# Entrada
# A primeira linha de entrada contém um inteiro N que determina a quantidade de casos de teste. Cada caso de teste consiste em dois inteiros x e y (1 ≤ x, y ≤ 100), indicando as variáveis a serem inseridas na função.

# Saída
# Para cada caso de teste imprima uma linha, contendo uma frase, indicando quem ganhou a competição. Por exemplo, se Rafael ganhar a competição, imprima “Rafael ganhou”. Assuma que nunca haverá empates.

def Rafael(x, y):
    total = ((3*x)**2) + y**2

    return total

def Beto(x, y):
    total = 2*(x**2) + ((5*y)**2)

    return total
    
def carlos(x, y):
    total = 2*(x**2) + ((5*y)**2)

    return total


number1 = int(input("Digite o valor de X: "))
number2 = int(input("Digite o valor de Y: "))
resultado1=Rafael(number1, number2)
resultado2=Beto(number1, number2)
result3=carlos(number1, number2)


if resultado1>resultado2 and result3:
    print("Rafael Ganhou!")
elif resultado2>resultado1 and result3:
    print("Beto Ganhou!")
else:
    print("Carlos Ganhou!")

print("Rafa: {} Beto:{} Carlos: {}".format(resultado1, resultado2, result3))