#O replace substitui na string o trecho 1 pelo trecho 2. 
#Sintaxe: str.replace(old, new [,count])
# Ps.: old - é a string antiga; 
# new - é a nova string
# e count - quantidade de vezes que você quersubstituir a string antiga pela nova

song = "frio, muito frio"
print(song.replace('frio','quente\n'))

song = "Let it be, Let it be, Let it be"
print(song.replace('Let','so',0))
print(song.replace('Let','so',1))


