
from veiculo import Veiculo


class Veiculo_Sem_Motor(Veiculo):
    def __init__(self,marca,modelo,ano,cor,possui_placa,placa, possui_marcha, qtd_marchas):
        Veiculo.__init__(self, marca,modelo,ano,cor,possui_placa,placa)
        self._possui_motor = possui_marcha
        self._qtd_marchas = qtd_marchas
        self._marcha_atual=0
    def mudar_macha(self, comando_marcha):
        if comando_marcha == "acima" and self._marcha_atual<self._qtd_marchas:
            self._marcha_atual+=1
            print (f"Passou para a marcha", )
        else:
            if self._marcha_atual==0:
                print('Não é possível diminuir a marcha')
 