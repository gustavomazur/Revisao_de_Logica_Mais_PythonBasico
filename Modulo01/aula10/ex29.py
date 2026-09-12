carro = int(input('Velocidade do seu carro: '))

if carro >= 80:
     print('você foi multado A multa vai custar R$7,00 por cada km acima do limite')
     multa = (carro - 80) * 7
     print('A multa vai custar R${:.2f}'.format(multa))
else:
    print('Passou com segurança boa viagem')
