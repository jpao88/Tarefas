# 3. Solicite ao usuário que informe a sua idade e depois classifique em:
#      a. Menor ou igual a 11 anos = criança.
#      b. Maior do que 11 e menor ou igual a 17 = adolescente.
#      c. Maior do que 17 e menor ou igual a 59 = adulto
#      d. Maior do que 59 = idoso.

idade = int(input("Por favor, informe sua idade: "))

if idade <= 11:
    print("Você é classificado como: 'Criança'")
elif idade > 11 and idade <= 17:
    print("Você é classificado como: 'Adolescente'")
elif idade > 17 and idade <= 59:
    print("Você é classificado como: 'Adulto'")
else:
    print("Você é classificado como: 'Idoso'")