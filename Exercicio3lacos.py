from random import randint

numero_aleatorio = randint (0, 100)
palpite = 0

while palpite != numero_aleatorio:
    palpite = int(input("Qual seu palpite: "))
    tentativas +=1


    if palpite > numero_aleatorio:
        print("O numero sorteado é menor")
    elif palpite < numero_aleatorio:
        print("O numero sorteado é maior")
    else:
        print("Você acertou!")

print ("tentativas: {tentativas}")
