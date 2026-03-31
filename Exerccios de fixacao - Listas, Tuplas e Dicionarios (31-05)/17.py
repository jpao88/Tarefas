#[TUPLE - desafio] Organizar valores sem mexer na tupla original

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

tupla_numeros = (num1, num2, num3, num4)
print("A tupla original é:", tupla_numeros)

lista_ordenada = list(tupla_numeros)
lista_ordenada.sort()
print("Os numero ordenados sao:", lista_ordenada)

print("O tipo da variável é:", type(lista_ordenada))



# Tarefa: Leia quatro números em uma tupla e exiba: 
# a tupla original
# uma lista ordenada apenas para visualização
# o tipo da variável ordenada
# Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.
# Use: sorted(), print(), type()


