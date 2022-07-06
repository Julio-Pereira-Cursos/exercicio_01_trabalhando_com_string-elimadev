'''
Programa em Python que solicite as informações de três pessoas, 
como nome, idade, peso, altura. Apresenta na tela estas informações 
de modo que permaneçam alinhados verticalmente com formatação de interpolação.
'''

print('='*33)
print('*** Dados da Primeira Pessoa ***')
print('='*33)
nome1   = input('Nome  : ')
idade1  = input('Idade : ')
peso1   = input('Peso  : ')
altura1 = input('Altura: ')

print()
print('='*33)
print('*** Dados da Segunda Pessoa ***')
print('='*33)
nome2   = input('Nome  : ')
idade2  = input('Idade : ')
peso2   = input('Peso  : ')
altura2 = input('Altura: ')

print()
print('='*33)
print('*** Dados da Terceira Pessoa ***')
print('='*33)
nome3   = input('Nome  : ')
idade3  = input('Idade : ')
peso3   = input('Peso  : ')
altura3 = input('Altura: ')

print()
print('*'*33)
print('*** Dados Coletados ***')
print('*'*33)
print()

print('-'*50)
print('{:15} {:10} {:10} {:10}'.format('Nome', 'Idade', 'Peso', 'Altura'))
print('-'*50)
print('{:15} {:10} {:10} {:10}'.format(nome1, idade1, peso1, altura1))
print('{:15} {:10} {:10} {:10}'.format(nome2, idade2, peso2, altura2))
print('{:15} {:10} {:10} {:10}'.format(nome3, idade3, peso3, altura3))


