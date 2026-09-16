#Link = https://youtu.be/ezfr9d7wd_k?si=1Ca2RP1jPuxBDa7S

def bobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
print('-' * 30)
valores = [6, 3, 9, 1, 0, 2]
bobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores: {valores} temos {s}')

soma(5, 2)
soma(5, 2, 4)



def lin():
    print('-' * 30)

lin()
print('Curso Em video')
lin()

def mensagem(msg):
    print(msg)

lin()
mensagem('Testanto')
lin()

#def soma(a, b):
    #soma = a + b
    #return soma

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A+B = {s}')


a = int(input('Primeiro valor A: '))
b = int(input('Segundo valor A: '))
soma(a, b)

def contador(*num):
    print(num)

print('-=' * 30)
contador(1, 10, 1)
contador(2, 1, 7)
contador(3, 7, 0)
print('-' * 30)



