class Veiculo:
    def __init__(self, marca, modelo, ano,cor, possui_placa, placa):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
        self._possui_placa = possui_placa
        self._placa = placa
        self._velocidade=0

    def get_info(self):
        print(f'Marca:{self._marca}  Modelo:{self._modelo}  Ano:{self._ano} Velocidade:{self._velocidade}km/h  Cor: {self._cor} {"Placa:" ,self._placa if self._possui_placa else "Veiculo não possui placa"}')
    
    def set_placa(self,possui_permissao, nova_placa):
        if self._possui_placa:
            if possui_permissao:
                self._placa=nova_placa
            else:
                print('Você precisa ter permissão para trocar a placa!')
        else:
            print('Este veículo não tem placa!')

    def acelerar(self, acrescimo_velocidade):
        if acrescimo_velocidade> 0:
            print(f'Veículo sendo acelerado em {acrescimo_velocidade} km/h')
            self._velocidade += acrescimo_velocidade
            print(f'O veículo atingiu a velocidade de {self._velocidade} km/h')
        else:
            print('Aceleração negativa inválida!')
    def freiar(self):
        if self._velocidade > 0:
            print(f'Veículo inicia frenagem em {self._velocidade} km/h')
            for velocidade in range(self._velocidade,-2, -2):
                if velocidade<=0:
                    break
                print(f'O veículo está parando em {velocidade} km/h')
                
                    
            self._velocidade=0
    def virar_direcao(self,direcao):
       print(f'O veículo está virando à {direcao}')