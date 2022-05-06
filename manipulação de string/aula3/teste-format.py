nome = "denilson"
nome_maiusculo = nome.capitalize()
print(nome_maiusculo)

mensagem = "Olá {0}.".format(nome_maiusculo)
print(mensagem)

segunda_mensagem = "Olá {0}, me chamo {1}".format(nome_maiusculo, "Python")
print(segunda_mensagem)

print('Mas o que acontece se colocarmos mais de um "{0}"? Vamos testar')

terceira_mensagem = "Olá {0}, me chamo {1}. {0}".format(nome_maiusculo, "Python")
print(terceira_mensagem)

nome = "denilson"
nome_maiusculo = nome.capitalize()
print(nome_maiusculo)

print(f'Olá {nome_maiusculo}.')
print(f'Olá {nome_maiusculo}, me chamo Python')
print(f'Olá {nome_maiusculo}, me chamo Python. {nome_maiusculo}')