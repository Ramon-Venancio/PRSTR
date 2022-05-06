#O "del" exclui um item do dicionário.
#O "in" verifica se uma chave existe no dicionário.
#O "keys" obtém as chaves de um dicionário.
#O "values" obtém os valores de um dicionário.
#Exs.:
D = {"arroz":17.30,"feijão":12.50,"carne":23.90,"alface":3.40}
print(D)
print("\n")

del D["feijão"]
print(D)
print("\n")
if "batata" in D:
    print("Existe sim 'batata' no dicionario.")
else:
    print("Não existe 'batata' no dicionarios.")
print("\n")
print(D.keys())
print(D.values())