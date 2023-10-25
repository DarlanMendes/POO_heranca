from veiculo_4_rodas import V_Quatro_Rodas
from veiculo_motorizado import Veiculo_Motorizado
class Caminhonete(V_Quatro_Rodas,Veiculo_Motorizado):
    def __init__(self,marca, modelo, ano,cor, possui_placa, placa,potencia, tipo_combustivel,qtd_marchas, tipo_cambio,tanque_cheio,qtd_litros_tanque,rodas_novas,capacidade_carga, carga):
        V_Quatro_Rodas.__init__(self, marca, modelo, ano, cor, possui_placa, placa,rodas_novas)
        Veiculo_Motorizado.__init__(self,marca, modelo, ano,cor, possui_placa, placa,potencia, tipo_combustivel,qtd_marchas, tipo_cambio,tanque_cheio,qtd_litros_tanque)
        self._capacidade_carga= capacidade_carga
        self._carga = carga
    def adicionar_carga(self,qtd_carga):
        if qtd_carga+ self._carga> self._capacidade_carga:
            print("Operação negada. A carga maxima do caminhonete seria ultrapassada")
        elif qtd_carga + self._carga == self._capacidade_carga:
            self._carga += qtd_carga
            print("A carga máxima foi atingida")
        else: 
            print(f"Caminhonete abastecida com carga {qtd_carga}. Agora a caminhonete possui {self._carga} kg de carga")