numero = int(input("informe os minutos: "))
cont = numero
f = 1


while cont > 0:
    f *= cont
    cont-=1
print(f"sua senha é LIBERDADE{f}")
