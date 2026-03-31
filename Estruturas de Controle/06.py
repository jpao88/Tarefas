#6. Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. 
# Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operação = input("Digite a operação que deseja realizar: 'adição', 'subtração', 'multiplicação' ou 'divisão' ")

if operação == "adição":
    print(num1 + num2)
elif operação == "subtração":
    print(num1 - num2)
elif operação == "multiplicação":
    print(num1 * num2)
else:
    print(num1 / num2)