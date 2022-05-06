nome = str(input("escolha crie um nome de usuário:\n"))
senha = str(input("Agora crie uma senha, mas que seja diferente do nome do usuário:\n"))

while nome == senha:
    print("A senha está igual ao usuário.")
    senha = str(input("Digite novamente:\n"))

