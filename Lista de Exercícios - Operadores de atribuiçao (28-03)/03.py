#Solicite ao usuário que informe o estoque no início do dia (int) e a quantidade vendida ao final do dia (int). 
# Atualize a quantidade utilizando atribuição -= para mostrar o estoque final. 
estoque = int(input("Qual é o seu estoque no início do dia?: "))
vendas = int(input("Qual é a quantidade vendida ao final do dia?: "))

estoque -= vendas
print("Seu estoque final é: ", estoque)
