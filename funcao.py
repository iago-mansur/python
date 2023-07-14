# Função inicial

def saudacao():
    print('Seja bem-vinda(o)!')
    print('olá, é um prazer ter você fazendo parte desse curso!')

saudacao()

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Fulano', 'Python')

# Função com parâmetros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Fulano')
saudacao('Fulano','C++')

# Funções com retorno

def soma(num1, num2):
    return num1+num2
    
resultado = soma(5,7)

print('O resultado da soma é', resultado)

# def calculadora(num1, num2, operacao='+'):
#     if operacao == '+':
#         return num1+num2
#     elif operacao == '-':
#         return num1-num2

# resultado = calculadora(10, 20)

# print(resultado)

# resultado = calculadora(10, 20, '-')

# print(resultado)