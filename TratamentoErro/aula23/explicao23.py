
'''
um comando que funcionaria o nome não é erro
é exeção -> exemplo
print(x)
NomeERROR

n = int(input('Digite um valor: '))
print(n)
Mais se eu digitar OITO -> vai dar uma exeção
ValueERROR -> ERRO de valor

a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(r)
mais se no a eu digito 8 e no b eu digito 0 vai me dar
uma exeção ZeroDivisionError
ZeroDivisionError -> erro de divisão por zero

'2' -> TypeERROR

lst=[3,6,4]
print(lst[3])
3? -> IndexERROR

import uteis #mais se ele não existe
import uteis não for encontrado vai dar
uma exção também
ModuleNotFoundError

try:
    operação
execept:
    falhou

    o mesmo try pode der varios execept

'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__class__}')
except (ValueError, TypeError):
    print(f'Tivemos um problem com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário prefeiru não informar os dados!')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito Obrigado!')
