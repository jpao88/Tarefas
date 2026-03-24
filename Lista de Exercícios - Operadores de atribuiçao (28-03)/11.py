#Solicite ao usuário uma distância em metros e depois converta para km inteiros com //= 1000, guarde os metros restantes utilizando %= (utilize outra variável).
m = int(input("Digite uma distância em metros:"))  
m_originales = m
m //= 1000
m_originales %= 1000
print("Os kilometros resultantes são", m, "e os metros restantes são", m_originales)