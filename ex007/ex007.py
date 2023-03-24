# Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.

# Entrada
# A primeira linha de entrada contem um único inteiro N (1 < N < 1000), indicando o número de elementos que deverão ser lidos em seguida para o vetor X[N] de inteiros. A segunda linha contém cada um dos N valores, separados por um espaço. Vale lembrar que nenhuma entrada haverá números repetidos.

# Saída
# A primeira linha apresenta a mensagem “Menor valor:” seguida de um espaço e do menor valor lido na entrada. A segunda linha apresenta a mensagem “Posicao:” seguido de um espaço e da posição do vetor na qual se encontra o menor valor lido, lembrando que o vetor inicia na posição zero.

def position(number):
    Array = []

    for i in range(number):
        Array.append(int(input("Digite um número: ")))

    maior=Array[1]
    # daria para fazer junto, mas vou fazer separado para ver como procura

    for ind in range(number):
        if Array[ind]<maior:
            maior=Array[ind]
            posicao=ind;

    print("O menor número é: {} / encontrase na posição: {}".format(maior, posicao))





num = int(input("Digite o tamanho que deseja que seja o vetor: "))
position(num)