#[DICT] Remover uma chave com segurança

nome = input("Digite o nome do seu produto: ")
preco = float(input("Digite o preço de seu produto"))

produto = {"Nome": nome, "Preço": preco}
print("Produto atual:", produto)

produto.pop("desconto", "Chave nao encontrada")

print("Depois da remoçao:", produto)

# Tarefa: Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
# Use: input(), float(), dict.pop("chave", valor_padrao), print()
# Tipos: str, float, dict.
# Conceitos: remoção segura, estado antes/depois.