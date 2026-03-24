# Solicite ao usuário que informe um orçamento (float) e um gasto (float). Utilize atribuição -= para descontar o gasto do orçamento.  
orçamento = float(input("Qual é o seu orçamento?: "))
gasto = float(input("Qual foi o valor do seu gasto?: "))

orçamento -= gasto
print("O orçamento atual é de: ", orçamento)