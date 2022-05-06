#O min retorna o menor valor de uma lista.
#Ex.:
print("O maior número entre of 4,12,43.3,19 e 100 é:")
print(min(4,12,43.3,19,100))
print("O menor entre 'Canhão','Macarronada','Flamengo','Campeão' é:")
print(min("Canhão",'Macarronada',"Flamengo","Campeão"))

print(""*2)
#O max retorna o maior valor de uma lista.
#Ex.:
print("O maior número entre of 4,12,43.3,19 e 100 é:")
print(max(4,12,43.3,19,100))
print("O maior entre 'Canhão','Macarronada','Flamengo','Campeão' é:")
print(max('Canhão','Macarronada','Flamengo','Campeão'))

a = '1 2 3 4 5'
b = [int(n) for n in a.split()]
print("O maior é",max(b))