#Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input("Qual é o seu salário?"))
aumento = float(input("Qual será a porcentagem de aumento salarial?"))
aumento_percentual = salario * (aumento / 100)
novo_salario = salario + aumento_percentual
print("O novo salario é::", novo_salario)