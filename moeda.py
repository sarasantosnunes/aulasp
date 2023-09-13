
# crie um modulo chamado moeda.py que tenha as funções 
# incorporadas aumentar(),dimuinir (),dobro(),e metade().
# faça tambem um programa que importa esse modulo e use algumas 
# dessas funções rie modulo teste.py 






def aumentar(preço,taxa):
    res = preço + (preço * taxa/100)
    return res

def dimuinir (preço,taxa):
    res = preço - (preço *  taxa/100)
    return res

def dobro(preço):
    res = preço * 2
    return

def metade(preço):
    res = preço/2
    return res