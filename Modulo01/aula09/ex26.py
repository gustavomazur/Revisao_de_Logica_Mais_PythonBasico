frase = str(input('Digite uma frase: ')).strip()
print('A letra A parece {} vezes na frase.'.format(frase.lower().count('a')))
print('A primeira posição da letra a apareceu {}'.format(frase.lower().find('a')+1))
print('A ultima posicção de a apareceu {}'.format(frase.lower().rfind('a')+1))
