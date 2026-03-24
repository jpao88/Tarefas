#Solicite um valor de estoque (int), subtraia as vendas utilizando -= e depois a reposição do estoque utilizando +=, por fim, aplique %= 6. 
estoque = int(input("Qual é o seu estoque?: "))
vendas = int(input("Quantas vendas foram realizadas?: "))
estoque -= vendas

reposição = int(input("Quantas unidades serão adicionadas?: "))
estoque += reposição

estoque %= 6
print(estoque)