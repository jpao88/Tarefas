#[DICT - CONTINUIDADE DO EXERCÍCIO ANTERIOR] 

nome = input("Qual é seu nome?")
idade = input("Qual é sua edade?")

aluno = {"Nome": nome, "Idade": idade}

nota = float(input("Digite a nota: "))

aluno["nota"] = nota
print("Aluno é:", aluno)


# Adicionar uma nova chave nota
# Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
# Use: float(), input(), atribuição dict["nota"] = valor, print()
# Tipos: float, dict.
# Conceitos: atualização/adição de chave, tipos numéricos.