# > ESTRUTURAS CONICIONAIS

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você foi aprovada(o)!')
elif media >= 5:
    print('Recuperação')
else:
    print('Você foi reprovada(o).')

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado!')
else:
    print('Reprovado')