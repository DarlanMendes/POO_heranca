from caminhao import Caminhao
from carro import Carro
from bicicleta import Bicicleta
from caminhonete import Caminhonete
carro_teste = Carro('Volkswagen', 'Gol 1.0', 1998,'Vermelho',True,'HWZ9050','97cv','gasolina',5,'mecânico',True,300,True,4,True)

carro_teste.abastecer(30)
carro_teste.virar_direcao('Direita')
carro_teste.acelerar(20)
carro_teste.passar_marcha('acima')
carro_teste.acelerar(20)
carro_teste.freiar()
carro_teste.get_info()

bicicleta_teste = Bicicleta('Caloi', 'Cross22', 2020, 'Azul',False,None,True,20,True, '29')
bicicleta_teste.acelerar(5)
bicicleta_teste.freiar()
bicicleta_teste.pedalar()
bicicleta_teste.get_info()

caminhonete_teste= Caminhonete('Ford', 'D-20', 1992, 'cinza',True, 'HZO-9090', '70cv','Diesel', 6, 'Manual', True, 300, True, 200, 20)
caminhonete_teste.acelerar(40)
caminhonete_teste.freiar()
caminhonete_teste.get_info()

caminhao_teste = Caminhao('Ford','C100',2005, 'branco', True, 'ZVA-4050', '300cv', 'Diesel', 12, 'Automatico', False, 500, True, 2000, 300)
caminhao_teste.abastecer(20)
caminhao_teste.acelerar(25)
caminhao_teste.freiar()
caminhao_teste.get_info()