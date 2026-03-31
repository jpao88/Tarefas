#4. Solicite ao usuário que informe um número e depois exiba se é par ou ímpar.

num = int(input("Digite um número: "))

par = num % 2

if par == 0:
    print("O número é par")
else:
    print("O número é negativo")