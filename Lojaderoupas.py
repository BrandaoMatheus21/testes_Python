print ("================================================")
print ("===============LOJA DE ROUPAS===================")
print ("================================================")
print ("BOA TARDE , SENHOR(A) !")
print ("Você irá calcular o valor final de sua compra: ")
valor = float(input("Digite o valor da compra: "))
meiodepag = input("Informe a forma de pagamento (a prazo, a vista): ")

if meiodepag == "a vista":
    if valor >= 500 and valor < 1000 :
        print (valor - (valor * 0.15))
    elif valor >= 1000 :
        print (valor - (valor * 0.2))
    elif valor <= 500 :
        print (valor - (valor * 0.1))

if meiodepag == "a prazo" :
    parcelas = int(input("Digite a quantidade de parcelas. Acima de 10 possui juros:(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18) "))
    if parcelas == 1 :
        print (valor)
    if parcelas == 2 :
        print (valor / 2)
    if parcelas == 3 :
        print (valor / 3)
    if parcelas == 4 :
        print (valor / 4)
    if parcelas == 5 :
        print (valor / 5)
    if parcelas == 6 :
        print(valor / 6)
    if parcelas == 7 :
        print (valor / 7)
    if parcelas == 8 :
        print (valor / 8)
    if parcelas == 9 :
        print (valor / 9)
    if parcelas == 10 :
        print (valor / 10)
    if parcelas == 11 :
        print (valor + valor * (0.05 * 11))
    if parcelas == 12:
        print (valor + valor * (0.065 * 12))
    if parcelas == 13 : 
        print (valor + valor * (0.07 * 13))
    if parcelas == 14 :
        print (valor + valor * (0.09 * 14))
    if parcelas == 15 :
        print (valor + valor * (0.095 * 15))
    if parcelas == 16 :
        print (valor + valor * (0.1 * 16))
    if parcelas == 17 : 
        print (valor + valor * (0.113 * 17))
    if parcelas == 18 :
        print (valor + valor * (0.12 * 18))