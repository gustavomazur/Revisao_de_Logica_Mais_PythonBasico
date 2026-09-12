texto = 'Teste funcionou'

print(f'Testando print {texto}')

def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim')

contador(2, 1, 7)

nome = ['gustavo', 'matheus']

for cada in nome:
    print(cada)

