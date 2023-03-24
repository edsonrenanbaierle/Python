def multiplos(num1, num2):
    if num1>num2:
        if(num1%num2>0):
            print("O número {} e {} não são multiplos".format(num1, num2))
        else:
            print("O número {} e {} são multiplos".format(num1, num2))
    else:
        if(num2%num1>0):
            print("O número {} e {} não são multiplos".format(num1, num2))
        else:
            print("O número {} e {} são multiplos".format(num1, num2))



    


print("Descubra se são números multiplos entre si!")
number1 = int(input("Digite o 1 número: "))
number2 = int(input("Digite o 2 número: "))
multiplos(number1, number2)