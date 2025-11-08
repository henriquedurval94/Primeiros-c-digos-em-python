#### Primeiro codigos em Python #######

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

if media >= 7:
    print('A media do aluno é', media, ' - APROVADO')
else :
    print('A média do aluno é', media, ' - REPROVADO')
