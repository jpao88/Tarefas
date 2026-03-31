#[TUPLE] Acessar elementos da tupla
fruta1 = input("Digite a primeira fruta: ")
fruta2 = input("Digite a segunda fruta: ")
fruta3 = input("Digite a terceira fruta: ")

frutas = (fruta1, fruta2, fruta3)
print("As frutas são:", frutas)

fruta4 = input("Digite o nome de uma fruta para saber se ela já foi registrada: ")
mensagens = ("A fruta nao foi registrada", "A fruta foi registrada")

print(mensagens[fruta4 in frutas])

#Tarefa: Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela está ou não na tupla.
#Orientações: 
#  usar in
#  usar input()
#  tipo: str, tuple
#  conceito: operador de pertinência