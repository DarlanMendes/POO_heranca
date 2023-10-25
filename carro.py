

from veiculo_4_rodas import V_Quatro_Rodas
from veiculo_motorizado import Veiculo_Motorizado

class Carro( Veiculo_Motorizado, V_Quatro_Rodas):
    def __init__(self, marca, modelo, ano, cor, possui_placa, placa, potencia, tipo_combustivel,qtd_marchas, tipo_cambio,tanque_cheio,qtd_litros_tanque,rodas_novas, qtd_portas, possui_ar_condicionado):
        Veiculo_Motorizado.__init__(self,marca, modelo, ano,cor, possui_placa, placa,potencia, tipo_combustivel,qtd_marchas, tipo_cambio,tanque_cheio,qtd_litros_tanque)
        V_Quatro_Rodas.__init__(self,marca, modelo, ano, cor, possui_placa, placa, rodas_novas)
        self._qtd_portas = qtd_portas
        self._possui_ar_condicionado = possui_ar_condicionado

   
       
