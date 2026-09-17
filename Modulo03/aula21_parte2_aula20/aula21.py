#INTERACTIVE HELP
#COMANDO = help() -> função interna

#Python Console -> como fosse manual eu pesquiso conforme preciso
#exemplo
#def vai trazer um exemplo pra mim explicação
#quit sai

#outro exemplo de usar
help(print) #-> vai trazer o manual
print(input.__doc__)

#DOCSTRINGS
#parementro real
def contador(i, f, p):
    """
        -> Faz uma contagem e mostra na tela
        :param i: inicio da contagem
        :para f: fim da contagem
        :para p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


#oque está entre """.... """ > é meu docstring
#parementro formal
#contador(2, 10, 2)
#se eu execultar o hel(contador) -> vai me mostrar o meu docstring
help(contador)



#PAREMENTRO OPCIONAL
#def contador(a, b, c):-> sem parementro opcional
def soma(a, b, c=0):#->com parementro opcional
    #Eu posso colocar os 3 paremtros modo opcional
    #a = 0, b = 0, c = 0)
    s = a + b + c
    print(f'a soma de {a} + {b} + {c} = {s}')

soma(1, 2, 3) #-isso funciona passando 3 paramentros formal pro parmentro real
#-mais se eu passar dois parementros formal só
soma(1, 2)#-Erro né eu tenho que usar parementro opcional lá no def vai lá pra ver

#ESCOPO DE VARIAVEL
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'na função teste, x vale {x}')
#Programa principal

n = 2
print(n)
print(f'no Programa principal, n vale {n}')
teste()
print(f'no Programa principal, x vale {x}')


"""
O valor do n ir para função é valer o mesmo valor isso é chamado de escopo global 
Mais o x não funciona na fora da função só existe lá dentro então Programa principal não 
Consgue imprimir ele mais o n funciona pra todos os lugares por isso que da certo 
"""

"""se dentro da função
def contador(b):
        global a -> como eu fiz isso eu estou falando que o a dentro da função não é mais local é global 
        então o a meu que valia apenas 5 ele vira 8 e função que criava outra variavel a local não cria mais
        apenas usa a variavel a global 
      a = 8
      b+=4
      c = 2
      print(f'A dentro vale {a}')
      print(f'B dentro vale {b}')
      print(f'C dentro vale {c}')

a = 5
contador(a)
print(f'A dentro vale {a}')"""


'''na funcção
def eu colocar
return no lugar de print
exemplo 
def soma(a, b, c=0):
    s = a + b + c
    return s
    
eu posso agora trabalhar o s 
print(f'a minha soma vale tanto{s}
soma(1, 2, 3)
logicamente posso guarda isso em uma variavel também
r1 = soma(1, 2, 3) o return ele ia vim porque chamei a função soma né
então tudo que vem antes de soma igual print ou r1 etc... eu posso usar quanto quero der personalização dos resultados
eu só quero que ele me manda os resultado não escreva do jeito que ele isso eu que vou escolher '''

