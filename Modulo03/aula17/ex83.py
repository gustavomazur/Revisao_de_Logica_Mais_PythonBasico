expresao = str(input('Digite a expresão: '))
pilha = []
for simbolo in expresao:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbolo)
            break

if len(pilha) == 0:
    print('Sua expresão está Válida!')
else:
    print('Sua expresão está errada!')
