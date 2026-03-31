#2 [LIST] Remova um número se ele existir
num1 = int(input("Digite um primeiro número inteiro:"))
num2 = int(input("Digite um segundo número inteiro:"))
num3 = int(input("Digite um terceiro número inteiro:"))
num4 = int(input("Digite um quarto número inteiro:"))

lista_inteiros = [num1,num2,num3,num4]
print("O número original de números na lista é:", len(lista_inteiros))

num5 = int(input("Digite um quinto número inteiro:"))
num5 in lista_inteiros and lista_inteiros.remove(num5)

print("O número atual de itens na lista é:", len(lista_inteiros))


# Tarefa: Leia quatro inteiros e crie uma lista. 
# Leia um valor alvo e remova se ele estiver na lista. 
# Mostre o tamanho antes e depois.
# Use: int(), input(), in, remove(), len(), print()
# Tipos: int, list.
# Conceitos: teste de pertencimento, tratamento simples de remoção, função len().
