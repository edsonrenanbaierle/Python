# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

# Entrada
# O arquivo de entrada contém dois valores inteiros.

# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores #fornecidos na entrada que deverá caber em um inteiro.

def soma(a, b):
    total=0
    if a>b:
        while b<a:
            if b%2>0:
                total+=b
            b+=1
    else:
        while a<b:
            if a%2>0:
                total+=a
            a+=1
        

    print("A soma dos ímpares deu: ", total)

        
        



x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
soma(x, y)
