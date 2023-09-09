print ("CALCULADORA DE JUROS SIMPLES")
print ("=============================")

valor = float(input ("Qual o valor?"))
taxa = float(input("Qual a taxa de juros em porcentagem?"))
periodo = float(input("Qual o periodo? (Em anos))"))


final = valor + (valor * (taxa) * (periodo/100))
print (f"O valor final pago será de {final}")
