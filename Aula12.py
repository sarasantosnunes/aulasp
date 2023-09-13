class Carro: 
    def __init__(self,velMax,ligado,cor):
       self.velMax = velMax
       self.ligado = ligado
       self.cor = cor 
       

    def Mostrar(Self):
     print('Velocidade maxima:' + str(Self.velMax)) 
     print('cor .........:' + Self.cor ) 
     estado = 'sim' if Self.ligado else 'N'
     print('ligado........:'+ estado)
     print('.........................')  



c1 = Carro(200,False,'preto')
c2 = Carro(120,False,'branco')  
c3 = Carro(300,False,'vermelho')  

c1.Mostrar()
c2.Mostrar()
c3.Mostrar()
