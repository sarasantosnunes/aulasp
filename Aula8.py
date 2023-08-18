# print realiza uma tarefa
# retun calcula e retorna um valor 

'''def cliente1(nome):
    print(f'ola {nome}') 



def cliente2(nome):
    return f'ola{nome}'

x = cliente2('maria')
y = cliente2('jose')

print(x)
print(y)'''


# criar uma função que soma varios numeros 


'''def soma(*numeros):
     resultado = 0 
     for num in numeros:
          resultado += num
     return resultado     


x = soma (2,3,4,7)

print(x)


#define função

def somador(valor1,valor2):
    soma = valor1 + valor2 
    return soma '''

#define soma

'''res = somador (3,4)
print (f'valor e {res}')


#declaração da função 

def imprime_msg(nomepessoa):
    print(f' o usuario {nomepessoa}  escreveu uma ,mensagem')'''


#chamado a função
'''nome = input('digite seu nome:')    
imprime_msg(nome)'''


#criar uma função que armaneza numeros e string
# varios argumentos 

def agencia(**carro):
    return carro


print(agencia( marca='gol'))
print(agencia( marca='fiat', cor='azul',motor=1.0))
print(agencia( marca='siena',cor='branca',motor=1.0,placa=1444))

#qual e o numero fatorial de quatro de 4 

# 4*3*2*1 = 24 

import math 
print (math.factorial(4))

fatorial =  4*3*2*1
print(floor(2.7))






