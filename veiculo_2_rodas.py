
from veiculo import Veiculo


class V_Duas_Rodas(Veiculo):
    def __init__(self,marca,modelo,ano,cor,possui_placa,placa, rodas_novas): 
        Veiculo.__init__(self,marca,modelo,ano,cor,possui_placa,placa) 
        self._numero_rodas = 4
        self._rodas_novas = rodas_novas

    def mudar_rodas(self):
        if self._rodas_novas == True:
            print("As rodas estão bens!Não é necessária a troca.")
        else:
            self._rodas_novas == True
            print("Rodas trocadas. Agora o veículo possui novas rodas.")