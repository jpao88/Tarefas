#[DICT - desafio] Atualizar preço e quantidade; calcular o total 



nome = input("Ingresa el nombre del producto: ")
preco = float(input("Ingresa el precio: "))
quantidade = int(input("Ingresa la cantidad: "))

producto = {"nome":nome, "preco":preco, "quantidade":quantidade}

# Pedimos el porcentaje de aumento
aumento = float(input("Ingresa el porcentaje de aumento (%): "))

# Actualizamos precio y cantidad en el diccionario
producto["preco"] = producto["preco"] * (1 + aumento / 100)
producto["quantidade"] = producto["quantidade"] + 2

# Calculamos el total
total = producto["preco"] * producto["quantidade"]

# Mostramos los resultados
print(f"\nProducto:          {producto['nome']}")
print(f"Precio actualizado: R$ {producto['preco']:.2f}")
print(f"Cantidad actualizada: {producto['quantidade']}")
print(f"Total:              R$ {total:.2f}")

# Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. 
# Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
# Use: float(), int(), input(), acesso/atribuição por chave, print()
# Tipos: str, float, int, dict.
# Conceitos: operadores aritméticos (*, +), atualização de valores no dict.