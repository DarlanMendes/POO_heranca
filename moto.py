
from veiculo_sem_motor import Veiculo_Sem_Motor
from veiculo_2_rodas import V_Duas_Rodas
class Moto(Veiculo_Sem_Motor, V_Duas_Rodas):
    def __init__(self,marca, modelo, ano,cor, possui_placa, placa,possui_marcha, qtd_marchas,rodas_novas, tipo_quadro):
        Veiculo_Sem_Motor.__init__(self,marca, modelo, ano,cor, possui_placa, placa,possui_marcha,qtd_marchas)
        V_Duas_Rodas.__init__(self,marca, modelo, ano,cor, possui_placa, placa,rodas_novas)
        self._tipo_quadro= tipo_quadro