# listas 
#ARMAZENAR MAIS DE UMA INFORMAÇÃO EM VARIAVEIS
# MANTER A SEQUENCIA DOS DADOS EM UMA VARIAVEL 


cidade1 = 'rio de janeiro'
cidade2 = ' são paulo '
ciadade3 = ' salvador'



                  # itens                
cidades = ['brasil', ' america', ' cuba']
     #         0                   1             2
 

#cidades.append('santa catarina')
# cidades.remove('salvador')
#cidades.insert(2,'manaus ')
#cidades.pop(0)
cidades.sort()

print(cidades)



numeros = [2,3,4,5]
letras = ['a','b','c','d',]


#final = nemeros + letras 
numeros.extend(letras)
print(numeros )

#            0                   1
itens = [['item1','item2'],['item3','item4',]]
#           0        1       0      1

print(itens[1][0])