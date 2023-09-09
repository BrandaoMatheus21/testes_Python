# Programa para calcular o IMC
print ("CALCULE SEU IMC")
print ("==========================================")

nome = input ("Qual seu nome?")

idade = int(input("Qual sua idade?"))

peso = float(input("Qual seu peso?"))

altura = float(input("Qual sua altura?"))

imc = peso / (altura * altura)

print (f"Olá {nome}")
print (f"Sua idade é de {idade} anos")
print (f"seu IMC é de {imc}")