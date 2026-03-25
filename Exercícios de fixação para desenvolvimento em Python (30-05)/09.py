#Leia o preço de um produto e imprima o preço com 10% de desconto.
preço = float(input("Qual é o preço do procuto:"))
desconto = preço * 0.1
preço_atual = preço - desconto
print("O preço atual é:", preço_atual)