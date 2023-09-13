carros = ['BMW X6', 'BMWI5', 'BMWI8']
escolhaUsuario = input("Informe um carro")
for carro in carros:
    if escolhaUsuario.upper() == carro.upper:
        print("Este carro está disponível")
    else:
        print("Desculpe, este carro não está disponível")