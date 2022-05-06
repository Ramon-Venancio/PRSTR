#O comando startswith procura pelas letras iniciais das palavras.
#Exemplos:
''''
teste = "Programar em Python é massa!"
print(teste.startswith('pro'))
print(teste.startswith('Pro'))
'''
'''
teste = "Programar em Python é massa!"
print(teste.startswith('Pro'))
print(teste.startswith('Pro',1,6))
print(teste.startswith('Pyt',13,20))
print(teste.startswith('ro',0,6))
'''
#O comando endswith procura pelas letras finais das palavras.
#Exemplos:
teste = "Programar em Python é massa....meu irmão"
suffix = "irmão"

print(teste.endswith(suffix))
print(teste.endswith(suffix,20))

suffix = 'ro'
print(teste.endswith(suffix,2,4))
print(teste.endswith(suffix,2,6))