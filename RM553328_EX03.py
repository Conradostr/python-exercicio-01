pontos_par = 0.0
pontos_impar = 0.0



print("*** VOCÊ ESTÁ DIGITANDO AS NOTAS DOS NUMEROS PARES ***")
for x in range(2,51,2):
    pontos_par = pontos_par + float(input(f"Por favor digite a nota no aluno {x}: "))


print("*** VOCÊ ESTÁ DIGITANDO AS NOTAS DOS NUMEROS IMPARES ***")
for x in range(1,51,2):
    pontos_impar = pontos_impar + float(input(f"Por favor digite a nota no aluno {x}: "))

media_par = pontos_par/25
media_impar = pontos_impar/25

if media_par > media_impar:
    print(f"*** O grupo com maior nota é o PAR com média {media_par} ***")
    print(f"*** O grupo IMPAR ficou com média {media_impar} ***")
elif media_impar > media_par:
    print(f"*** O grupo com maior nota é o IMPAR com média: {media_impar} ***")
    print(f"*** O grupo PAR ficou com média: {media_par} ***")
else:
    print("Ouve empate entre os grupos")