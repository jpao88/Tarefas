#Solicite ao usuário que informe os tempos em segundos (int). 
# Converta para minutos inteiros com //= e depois use %= para obter segundos restantes. 
seg = int(input("Quantos segundos você quer converter em minutos?: "))
seg_originales = seg
seg //= 60
seg_originales %= 60
print("Os minutos são", seg, "e os segundos restantes são", seg_originales)