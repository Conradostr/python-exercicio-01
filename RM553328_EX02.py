votos_segunda = int(input("Informe os votos da segunda feira: "))
votos_terca = int(input("Informe os votos da terça feira: "))
votos_quarta = int(input("Informe os votos da quarta feira: "))
votos_quinta = int(input("Informe os votos da quinta feira: "))
votos_sexta = int(input("Informe os votos da sexta feira: "))

if votos_segunda > (votos_terca and votos_quarta and votos_quinta and votos_sexta):
    print("O dia com mais voto é: Segunda")
elif votos_terca > (votos_segunda and votos_quarta and votos_quinta and votos_sexta):
    print("O dia com mais votos é: Terça")
elif votos_quarta > (votos_segunda and votos_terca and votos_quinta and votos_sexta):
    print("O dia com mais votos é: Quarta")
elif votos_quinta > (votos_segunda and votos_terca and votos_quarta and votos_sexta):
    print("O dia com mais votos é: Quinta")
elif votos_sexta > (votos_segunda and votos_terca and votos_quarta and votos_quinta):
    print("O dia com mais votos é: Sexta")
else:
    print("Ouve empate")