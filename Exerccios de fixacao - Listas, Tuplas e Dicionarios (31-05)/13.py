#[TUPLE] Contar quantas vezes um número aparece

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

numeros = (n1, n2, n3, n4)
print("Os números são:", numeros)

n5 = int(input("Digite um número para saber se foi registrado: "))

print("O número aparece esse número de vezes:", numeros.count(n5))

#Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.
#Orientações: 
#método: tuple.count()
#tipos: int, tuple