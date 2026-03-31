#[TUPLE] Exibir maior e menor valor

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

numeros = (n1, n2, n3, n4)
print("Os números são:", numeros)

maior = max(numeros)
print("O maior número é:", maior)

menor = min(numeros)
print("O menor número é:", menor)

#Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
#Orientações: 
#funções: max(), min()
#tipos: int, tuple
#conceito: operações básicas de agregação