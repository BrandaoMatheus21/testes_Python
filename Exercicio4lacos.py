alunos = []
notas = []
continua == 'S'

while continua == 'S':
    aluno = input("Informe o nome do aluno: ")
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))
    alunos.append(aluno)
    notas.append((nota1, nota2, nota3, nota4))
    continua = input("Dseja inserir mais alunos: (S/N)")

for aluno in alunos:
    print(f"Aluno: {aluno}")
    notas_aluno == notas[alunos.index(aluno)]

    media = sum(notas_aluno) / len(notas_aluno)
    print(f"Média: %.2f" % media)