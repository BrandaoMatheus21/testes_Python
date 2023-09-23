print("==== IMPRIMINDO NUMERO DE 1 A 10====")
for numero in range(1, 11):
    print(numero)
print("========================================")

numero_max = int(input("Digite o número máximo :"))
ordem = input("Qual a ordem: (C/D)")

if ordem == 'C' :
    for numero in range (1, numero_max + 1):
        print(numero)
if ordem == 'D' :
        for numero in range (numero_max, 0, -1):
         print(numero)