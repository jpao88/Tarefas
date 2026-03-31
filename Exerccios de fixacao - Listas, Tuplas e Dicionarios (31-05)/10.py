#[DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes

agenda = {"Ana":"1111-1111","Bruno":"2222-2222"}
print("A agenda é:", agenda)

novo_contato = input("Digite o novo contato: ")
novo_telefone = input("Digite o novo telefone: ")

agenda[novo_contato] = novo_telefone
print("Agenda atual:", agenda)

nome_atualizar = input("Digite o nome do contato que deseja atualizar: ")
telefone_atualizar = input("Digite o novo telefone: ")
nome_atualizar in agenda and agenda.__setitem__(nome_atualizar, telefone_atualizar)
print("Após atualizar contato:", agenda)

nome_remover = input("Digite o nome do contato que deseja remover: ")
agenda.pop(nome_remover, None)
print("Após remover contato:", agenda)

nomes_ordenados = sorted(agenda.keys())
print("Nomes ordenados:", nomes_ordenados)


#Tarefa: agenda = {"Ana", "1111-1111", "Bruno": "2222-2222"}
# Adicionar um novo contato (nome→telefone)
# Atualizar o telefone de um contato informado (se existir)
# Remover um contato pelo nome (se existir)
# Exibir a lista ordenada de nomes de contatos
# Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).
# Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.
# Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()