#4 [LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
                 
notas = [n1,n2,n3]
print("As notas são:", notas)

media = (notas[0] + notas[1] + notas[2]) / 3
print("A média das notas é:", media)

nota_minima = min(notas)
indice_minimo = notas.index(nota_minima)

nova_nota = float(input("Insira a nova nota: "))
notas[indice_minimo] = nova_nota
notas.sort()
print("Notas crescentes:", notas)

nova_media = (notas[0] + notas[1] + notas[2]) / 3
print("A nova média das notas é:", nova_media)


#Tarefa: Leia três notas (float) em uma lista. 
#Calcule a média. Substitua a menor nota por uma nova informada. 
#Ordene a lista e mostre a nova média.
#Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
#Tipos: float, list.
#Conceitos: mutabilidade, ordenação in-place, média aritmética.