#[DICT] Criar e exibir dicionário de aluno

nome = input("Qual é seu nome?")
idade = input("Qual é sua edade?")

aluno = {"Nome": nome, "Idade": idade}
print("Aluno é:", aluno)
print("Seu tipo é:", type(aluno))

# Tarefa: Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
# Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()
# Tipos: str, int, dict.
# Conceitos: mapeamento chave-valor, criação e exibição.