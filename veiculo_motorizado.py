from veiculo import Veiculo

class Veiculo_Motorizado(Veiculo):
    def __init__(self,marca, modelo, ano,cor, possui_placa, placa,potencia, tipo_combustivel,qtd_marchas, tipo_cambio,tanque_cheio,qtd_litros_tanque):
        Veiculo.__init__(self,marca, modelo, ano,cor, possui_placa, placa)
        self._potencia = potencia
        self._tipo_combustivel = tipo_combustivel
        self._qtd_combustivel=0;
        self._qtd_marchas = qtd_marchas
        self._tipo_cambio = tipo_cambio
        self._marcha_atual= 0
        self._tanque_cheio=tanque_cheio
        self._qtd_litros_tanque=qtd_litros_tanque

    def passar_marcha(self, comando_marcha):
        if comando_marcha == "acima" and self._marcha_atual<self._qtd_marchas:
            self._marcha_atual+=1
            if self._marcha_atual == 0:
                print("Em marcha neutra")
            else:
                print (f"Passou para a marcha", )
        else:
            if self._marcha_atual<0:
                print('Não é possível diminuir a marcha')
            elif self._marcha_atual==0:
                print("Marcha a ré engatada")
            else:
                self._marcha_atual-=1
    def abastecer(self, qtd_litros):
        if not self._qtd_combustivel == self._qtd_litros_tanque and (self._qtd_litros_tanque - self._qtd_litros_tanque<=qtd_litros):
            self._qtd_combustivel+=qtd_litros
            print(f'Você abasteceu {qtd_litros} litros de {self._tipo_combustivel}')
        else:
            print (f'O tanque excederá o limite se abastecido com essa quantidade de {self._tipo_combustivel}.')