# Solicite ao usuário que informe o saldo da sua conta e o valor que será depositado;
# ambos os valores devem ser do tipo FLOAT. Utilize atribuição += para adicionar o deposito ao saldo da conta e exiba o novo saldo na tela.  
saldo = float(input("Qual é o saldo da sua conta?: "))
deposito = float(input("Qual é o valor que será depositado?: "))

saldo += deposito
print("Seu novo saldo é: ", saldo)