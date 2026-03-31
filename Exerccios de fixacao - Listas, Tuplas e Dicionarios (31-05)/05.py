#5 [LIST - desafio] Fila: chegadas, prioridade e atendimento
fila = ["Ana", "Bruno"]
print("A lista original é:", fila)

nombre1 = input("Digite o primeiro nome: ")
nombre2 = input("Digite o segundo nome: ")

fila.extend([nombre1, nombre2])
print("O resultado final após adicionar os nomes:", fila)

cliente = input("Digite o nombe do cliente prioritário: ")
fila.insert(1, cliente)
print("Depois de adicionar o cliente prioritário, a lista fica assim", fila)

atendido = fila.pop(0)
print("Cliente atendido:", atendido)
print("Fila final:", fila)


#Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). 
# Leia um cliente prioritário e insira na posição 1. 
# Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
# Use: input(), extend(), insert(), pop(), print()
# Tipos: str, list.
#Conceitos: estrutura de fila, operações de inserção/remoção, ordem.