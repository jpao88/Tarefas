#Leia a distância (km) e o tempo (h), calcule a velocidade média.
distância = float(input("Digite a distância em quilômetros:"))
tempo = int(input("Digite o tempo:"))
velocidade = distância / tempo
velocidade_str = str(velocidade)
print("A velocidade é", velocidade_str+"km/h")