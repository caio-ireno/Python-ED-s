# Exercício: Filtrando Alunos Maiores de Idade

# Você foi encarregado de criar um programa em Python para ajudar a filtrar alunos maiores de idade a partir de uma lista de alunos cadastrados. O programa deve permitir que o usuário cadastre o nome e a idade de cada aluno e, em seguida, exibir apenas os alunos que são maiores de idade, ou seja, têm 18 anos ou mais.

# O programa deve funcionar da seguinte forma:

# Solicita ao usuário que insira o nome e a idade de cada aluno.
# Os dados de cada aluno (nome e idade) são armazenados em um dicionário, onde o nome é a chave e a idade é o valor associado.
# O programa permite ao usuário continuar cadastrando alunos até que ele decida encerrar o processo, digitando "sair".
# Após o encerramento do cadastro, o programa exibe na tela os nomes e idades dos alunos maiores de idade.

alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    try:
        idade = int(input("Digite a idade do aluno: "))
    except ValueError:
        print("Idade inválida. Por favor, insira um número válido para a idade.")
        continue

    alunos[nome] = idade

print("\nAlunos maiores de idade:")
for nome, idade in alunos.items():
    if idade >= 18:
        print(f"Nome: {nome}, Idade: {idade}")
