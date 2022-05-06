#O "get" busca uma chave-valor no dicionario e depois printa o valor.
contatos = {"Yan":"1234-5678","escola":"3401-2286"}
print(contatos)
print("\n")

print(contatos.get("Yan","Contato não encontrado."))
print(contatos.get("João","Contato não encontrado."))
print("\n")

#O "pop" busca uma chave-valor no dicionario e depois deleta e printa o valor.
print(contatos.pop("Marina","Contato não encontrado.")) 
print(contatos.pop("escola","Contato não encontrado."))
print(contatos)