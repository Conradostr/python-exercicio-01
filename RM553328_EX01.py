print("****************************************")
print("                BEM VINDO               ")
print("****************************************")
print("             LISTA DE PLANOS            ")
print("BASIC - 30% DE BÔNUS")
print("SILVER - 20% DE BÔNUS")
print("GOLD - 10% DE BÔNUS")
print("PLATINUM - 5% DE BÔNUS")
print("****************************************")


assinatura = input("Informe sua assinatura: ")
faturamento = float(input("Informe seu faturamento: "))

if assinatura.upper() == "BASIC":
    faturamento = faturamento * 0.3
    print(f"O seu bônus será de: {faturamento}")
elif assinatura.upper() == "SILVER":
    faturamento = faturamento * 0.2
    print(f"O seu bônus será de: {faturamento}")
elif assinatura.upper() == "GOLD":
    faturamento = faturamento * 0.1
    print(f"O seu bônus será de: {faturamento}")
elif assinatura.upper() == "PLATINUM":
    faturamento = faturamento * 0.05
    print(f"O seu bônus será de: {faturamento}")
else:
    print("**** Assinatura invalida ****")
