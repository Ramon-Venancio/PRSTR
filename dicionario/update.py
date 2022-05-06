#O "update" atualiza um dicionário.
contatos = {"Yan":"1234-5678","escola":"3401-2286","Pedro":"9999-9999",
                "Ana":"8765-4321","João":"8887-7778"}
contatos2 = {"Yan":"1234-5679","Fernado":"4402-3397","Luíza":"4443-3334"}

contatos.update(contatos2)
print(contatos)