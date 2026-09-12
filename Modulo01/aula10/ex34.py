salario = float(input('Qual o seu salario? '))

if salario >= 1250.00:
    salario_novo = salario + (salario * 15 / 100)
    print('Salario novo R${}'.format(salario_novo))
else:
    salario_novo = salario + (salario * 10 / 100)
    print('Salario novo R${:.2f}'.format(salario_novo))

