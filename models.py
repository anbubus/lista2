
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
        self.cor = nova_cor

    def mostra_cor(self):
        return self.cor
########################################################  
class Quadrado:
    def __init__(self, tamanholado):
        self.tamanholado = tamanholado

    def mudalado(self, novolado):
        self.tamanholado = novolado

    def valorlado(self):
        return self.tamanholado
    
    def area(self):
        return self.tamanholado*self.tamanholado
########################################################
class Retangulo:
    def __init__(self, LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB
    def mudaLado(self, nLadoA, nLadoB):
        self.LadoA = nLadoA
        self.LadoB = nLadoB
    def valorLado(self):
        return (self.LadoA , self.LadoB)
    def perimertro(self):
        return(2*self.LadoB+2*self.LadoA)
     
    def area(self):
        return(self.LadoB*self.LadoA)
    
########################################################
class Ponto:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def imprime_ponto(self):
        print(f'Ponto: ({self.x}, {self.y})')

class Retangulo:
    def _init_(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontra_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)
###########################################################
class Pessoa:
    def _init_(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            # A cada ano que a pessoa envelhece (idade < 21), ela cresce 0,5 cm.
            self.crescer(0.5 * anos)

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros

    def _str_(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} kg, Altura: {self.altura} cm"


##################################################################################
class ContaCorrente:
    def _init_(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado. Saldo atual: R${self.saldo:.2f}')
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado. Saldo atual: R${self.saldo:.2f}')
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def _str_(self):
        return f"Conta: {self.numero_conta}, Correntista: {self.nome_correntista}, Saldo: R${self.saldo:.2f}"

#########################################################################
class TV:
    def _init_(self):
        self.ligada = False
        self.canal = 1  # Inicializa no canal 1
        self.volume = 10  # Inicializa com volume 10

    def ligar_desligar(self):
        self.ligada = not self.ligada
        if self.ligada:
            print("TV ligada.")
        else:
            print("TV desligada.")

    def mudar_canal(self, novo_canal):
        if self.ligada:
            if 1 <= novo_canal <= 100:
                self.canal = novo_canal
                print(f"Canal alterado para {novo_canal}.")
            else:
                print("Canal fora da faixa válida (1-100).")
        else:
            print("A TV está desligada. Ligue a TV para mudar o canal.")

    def aumentar_volume(self):
        if self.ligada:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume aumentado para {self.volume}.")
            else:
                print("Volume máximo atingido.")
        else:
            print("A TV está desligada. Ligue a TV para ajustar o volume.")

    def diminuir_volume(self):
        if self.ligada:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume diminuído para {self.volume}.")
            else:
                print("Volume mínimo atingido.")
        else:
            print("A TV está desligada. Ligue a TV para ajustar o volume.")

    def status(self):
        print(f"Status da TV: Ligada: {self.ligada}, Canal: {self.canal}, Volume: {self.volume}")



##########################################################################################
class Tamagoshi:
    def __init__(self, name, hunger, health, age):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.age = age

    def show_health(self):
        print(self.health) 
    
    def show_hunger(self):
        print(self.hunger)

    def show_age(self):
        print(self.age) 
    
    def change_name(self, new_name):
        self.name = new_name

    def getolder(self, years):
        self.age += years 

    def eat(self, food):
        self.hunger += food

    def change_health(self, health):
        self.health = health

    def humor(self):
        return (self.hunger+self.health)/2
    def _str_(self):
        return f"{self.nome} - Fome: {self.fome}, Tédio: {self.tedio}, Humor: {self.humor()}"
    ######################################################################################

import random
class Bichinho:
    def _init_(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)
        self.tedio = random.randint(0, 100)

    def comer(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        return (self.fome + self.tedio) / 2

    def _str_(self):
        return f"{self.nome} - Fome: {self.fome}, Tédio: {self.tedio}, Humor: {self.humor()}"
##########################################################################################
class Macaco:
    def _init_(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def ver_bucho(self):
        print(f"{self.nome} tem no estômago: {', '.join(self.bucho)}")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo {', '.join(self.bucho)}.")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada no estômago.")


##########################################################
class BombaCombustivel:
    def _init_(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        if valor > 0:
            litros_abastecidos = valor / self.valor_litro
            if litros_abastecidos <= self.quantidade_combustivel:
                self.quantidade_combustivel -= litros_abastecidos
                print(f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
            else:
                print("Quantidade de combustível insuficiente na bomba.")
        else:
            print("O valor do abastecimento deve ser maior que zero.")

    def abastecer_por_litro(self, litros):
        if litros > 0:
            valor_a_pagar = litros * self.valor_litro
            if litros <= self.quantidade_combustivel:
                self.quantidade_combustivel -= litros
                print(f"Valor a pagar: R${valor_a_pagar:.2f}")
            else:
                print("Quantidade de combustível insuficiente na bomba.")
        else:
            print("A quantidade de litros deve ser maior que zero.")

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
        print(f"Valor do litro de {self.tipo_combustivel} alterado para R${novo_valor_litro:.2f}.")

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
        print(f"Tipo de combustível alterado para {novo_tipo_combustivel}.")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível alterada para {nova_quantidade:.2f} litros.")

    def status(self):
        print(f"Bomba de {self.tipo_combustivel}: Valor/Litro: R${self.valor_litro:.2f}, Quantidade de Combustível: {self.quantidade_combustivel:.2f} litros")


#####################################################################################
class ContaInvestimento:
    def _init_(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100  # A taxa de juros é fornecida como uma porcentagem

    def adicione_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros

    def obter_saldo(self):
        return self.saldo


###################################################################################
class Funcionario:
    def _init_(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario
    def aumentarSalario(self, porcentagem):
        self.salario *= porcentagem

