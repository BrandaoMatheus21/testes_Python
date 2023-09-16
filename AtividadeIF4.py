salario = float(input("Insira seu salario:"))
tempo_servico = float(input("Insira o seu tempo de serviço:"))

total = 0
if tempo_servico >= 5 :
    total = salario * 1.05
    print(total)
else:
    total = salario