# operadores lógicos

# and

'''renda_acima_5mil = True 
nome_limpo = False

if renda_acima_5mil and nome_limpo:
    print('Financimento Aprovado')
else:
    print(' Financiamento negado')''' 


  # or 
renda_acima_5mil = True
nome_limpo = False 


if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento negado') 


    idade_lucas = 21
    idade_carolina = 19



# OPERADOR OR 
if idade_lucas >= 18  or idade_carolina:
     
    print('Financiamento Aprovado')
else:
    print('Financiamento negado')  
idade_lucas = 21 
idade_carolina = 17 



# OPERADOR OR 

if idade_lucas >= 18 or idade_carolina >= 18:
   print('pelo menos um dos dois e maior de idade')
else: 
   print('lucas e carolina não são maiores de idade')

# OPERADOR AND 

if idade_lucas >= 18 and idade_carolina >= 18:
    print ('lucas e carolina são maiores de idade')   
else:
    print('pelo menos um dos dois e maior de idade')    



# FOR 

# IMPRIMIR DE 1 A 5 

for numero in range (1,20,2):
    print(numero)

lojas = ['rio','sampa','belo','curitiba',]    
    
for loja in lojas:
    print(loja)    
    print('Acabou for ')

for i in range(4):
    print(i)
    print(lojas[i])   


# FOR PRA STRINGS 

for letra in ' google':
    print (letra)

palavra = ' google '

for letra in palavra: 
    print (letra + ' esta dentro da palavra google')         