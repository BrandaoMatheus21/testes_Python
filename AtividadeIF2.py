#Programa de calculadora

numero1 = float(input("Informe um numero"))
numero2 = float(input("Informe mais um numero"))
operacao = input("Informe uma operação (Divisão, adição, multiplicação e subtração)")

if operacao == "Divisão": 
    print(numero1 / numero2)
if operacao == "adição":
    print(numero1 + numero2)
if operacao == "multiplicação":
    print(numero1 * numero2)
if operacao == "subtração":
    print(numero1 - numero2)