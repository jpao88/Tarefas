#3 [LIST] Atualizar elemento com uma operação

n1 = int(input("Digite um primeiro número inteiro:"))
n2 = int(input("Digite um segundo número inteiro:"))
n3 = int(input("Digite um terceiro número inteiro:"))

lista_inteiros_sem_soma = [n1,n2,n3]
print("Lista original:", lista_inteiros_sem_soma)

lista_inteiros_sem_soma[2] = lista_inteiros_sem_soma[0] + lista_inteiros_sem_soma[1]
print("A lista atual é:", lista_inteiros_sem_soma)


# Tarefa: Crie uma lista com três inteiros. 
# Atualize o último elemento para a soma dos dois primeiros. 
# Exiba a lista.
# Use: int(), input(), indexação lista[i], print()
# Tipos: int, list.
# Conceitos: operadores aritméticos (+), acesso/atribuição por índice.