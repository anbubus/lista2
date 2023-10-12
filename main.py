import models

#Bola
cor = input("Informe a cor da bola: ")
circunferencia = input("Informe a circunferencia da bola: ")
material = input("Informe o material da bola: ")

bola = models.Bola(cor, circunferencia, material)
print("a bola é da cor "+ bola.mostra_cor())
cor = input("Informe outra cor da bola: ")
bola.troca_cor(cor)
print("a bola é da cor "+ bola.mostra_cor())

###################################################

#Quadrado
quadrado = models.Quadrado(12)
print("valor do lado: " + quadrado.valorlado())
quadrado.mudalado(11)
print("valor do lado: " + quadrado.valorlado())
print("valor da area: " + quadrado.area())

###################################################
#Retangulo

lado_a = float(input("Informe o comprimento do local (metros): "))
lado_b = float(input("Informe a largura do local (metros): "))

area_local = lado_a * lado_b

retangulo = models.Retangulo(lado_a, lado_b)

area_piso = 0.25  # Área de um piso em metros quadrados
area_rodape = 0.05  # Área de um rodapé em metros quadrados

quantidade_pisos = area_local / area_piso
quantidade_rodapes = 2 * (lado_a + lado_b) / 0.25  # 2 rodapés por metro linear

print(f"Para cobrir o local, você precisará de {quantidade_pisos:.0f} pisos e {quantidade_rodapes:.0f} rodapés.")
##################################################
#Ponto e Retangulo

def menu():
    print("1. Criar um retângulo")
    print("2. Encontrar o centro do retângulo")
    print("3. Sair")

retangulos = []

while True:
    menu()
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        x = float(input("Digite a coordenada x do ponto inicial do retângulo: "))
        y = float(input("Digite a coordenada y do ponto inicial do retângulo: "))
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        ponto_inicial = models.Ponto(x, y)
        retangulo = models.Retangulo(ponto_inicial, largura, altura)
        retangulos.append(retangulo)
    elif escolha == 2:
        for i, retangulo in enumerate(retangulos):
            print(f"Centro do Retângulo {i + 1}:")
            centro = retangulo.encontra_centro()
            centro.imprime_ponto()
    elif escolha == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")
##################################################
#Pessoa
pessoa = models.Pessoa("João", 18, 70, 170)

print(pessoa)
pessoa.envelhecer()  # A pessoa envelhece 1 ano e cresce 0,5 cm.
pessoa.engordar(5)
pessoa.crescer(2)
print(pessoa)

#################################################
#ContaCorrente
minha_conta = models.ContaCorrente(numero_conta="12345", nome_correntista="João")
print(minha_conta)

minha_conta.deposito(100)
minha_conta.saque(30)

minha_conta.alterar_nome("João Silva")
print(minha_conta)
################################################
#TV
minha_tv = models.TV()
minha_tv.status()

minha_tv.ligar_desligar()
minha_tv.mudar_canal(5)
minha_tv.aumentar_volume()

minha_tv.ligar_desligar()
minha_tv.mudar_canal(150)
minha_tv.diminuir_volume()
##############################################
#Tamagoshi
def run_tamagoshi():
    tamago = models.Tamagoshi("Tamago", 10, 20, 0)
    while True:
        print("\nEscolha uma ação:\n")
        print("1. Alimentar seu bichinho\n")
        print(f"2. mudar o nome de {tamago.name}\n")
        print(f"3. Ver a fome de {tamago.name}\n")
        print(f"4. Ver a saúde de {tamago.name}\n")
        print(f"5. Ver a idade de {tamago.name}\n")
        print(f"6. Ver o humor de {tamago.name}\n")
        print("7. Sair")

        escolha = int(input("Opção: "))

        if escolha == 1:
            print("Escolha um alimento: \n Maca(diminui em 1 a fome e aumenta a saude em 2)\n fatia de bolo(diminui em 5 a fome e diminui a saude em 3) \n feijoada(diminui a fome em 10 e aumenta a vida em 5)")
            alimento = input(f"\nDigite o alimento para : {tamago.name} \n Maca=1 | Fatia de bolo=2 | Feijoada=3\n")
            
            if alimento == 1:
                tamago.eat(1)
                tamago.change_health(2)
            elif alimento == 2:
                tamago.eat(5)
                tamago.change_health(-3)
            if alimento == 3:
                tamago.eat(10)
                tamago.change_health(5)
            else:
                print("Opção inválida. Tente novamente.")
                break
        elif escolha == 2:
            new_name = input("\n Informe o nome nome:\n")
            tamago.change_name(new_name)
        elif escolha == 3:
            tamago.show_hunger()
        elif escolha == 4:
            tamago.show_health()
        elif escolha == 5:
            tamago.show_age()
        elif escolha == 6:
            print(tamago.humor())
        elif escolha == 7:
            break
        else:
            print("Opção inválida. Tente novamente.")

run_tamagoshi()

##############################################
#Macacos
def interacao_macacos():
    macaco1 = models.Macaco("Macaco1")
    macaco2 = models.Macaco("Macaco2")

    while True:
        print("\nEscolha uma ação:")
        print("1. Alimentar Macaco1")
        print("2. Alimentar Macaco2")
        print("3. Ver bucho do Macaco1")
        print("4. Ver bucho do Macaco2")
        print("5. Macaco1 come Macaco2")
        print("6. Sair")

        escolha = int(input("Opção: "))

        if escolha == 1:
            alimento = input("Digite o alimento para Macaco1: ")
            macaco1.comer(alimento)
        elif escolha == 2:
            alimento = input("Digite o alimento para Macaco2: ")
            macaco2.comer(alimento)
        elif escolha == 3:
            macaco1.ver_bucho()
        elif escolha == 4:
            macaco2.ver_bucho()
        elif escolha == 5:
            macaco1.comer(macaco2.nome)
        elif escolha == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")

interacao_macacos()

##############################################
#BombaCombustivel
bomba = models.BombaCombustivel("Gasolina", 5.00, 1000)
bomba.status()

bomba.abastecer_por_valor(50)
bomba.abastecer_por_litro(10)

bomba.alterar_valor(5.50)
bomba.alterar_combustivel("Diesel")
bomba.alterar_quantidade_combustivel(800)

bomba.status()
##############################################
#ContaInvestimento
conta_poupanca = models.ContaInvestimento(saldo_inicial=1000.00, taxa_juros=10)

for _ in range(5):
    conta_poupanca.adicione_juros()

saldo_final = conta_poupanca.obter_saldo()
print(f"Saldo final após a aplicação de juros: R${saldo_final:.2f}")

#############################################
#Funcionario
funcionario1 = models.Funcionario("João", 3000.00)
funcionario2 = models.Funcionario("Maria", 3500.00)

print(f"Funcionário 1 - Nome: {funcionario1.obter_nome()}, Salário: R${funcionario1.obter_salario():.2f}")
print(f"Funcionário 2 - Nome: {funcionario2.obter_nome()}, Salário: R${funcionario2.obter_salario():.2f}")

##############################################
#fazenda 
def interagir_com_fazenda(fazenda):
    print("O que você quer fazer na fazenda?")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir a todos os bichinhos")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        quantidade_comida = int(input("Quanta comida você quer dar a todos os bichinhos? "))
        for bichinho in fazenda:
            bichinho.comer(quantidade_comida)
    elif escolha == "2":
        tempo_brincadeira = int(input("Quanto tempo você quer brincar com todos os bichinhos? "))
        for bichinho in fazenda:
            bichinho.brincar(tempo_brincadeira)
    elif escolha == "3":
        for bichinho in fazenda:
            print(bichinho)
    elif escolha == "4":
        print("Até a próxima!")
        return False
    else:
        print("Escolha inválida. Tente novamente.")

    return True

# Exemplo de uso da fazenda de bichinhos
quantidade_bichinhos = int(input("Quantos bichinhos você quer na sua fazenda? "))
fazenda_de_bichinhos = []

for i in range(quantidade_bichinhos):
    nome_do_bichinho = input(f"Dê um nome ao bichinho {i + 1}: ")
    fazenda_de_bichinhos.append(models.Bichinho(nome_do_bichinho))

continuar_interacao = True
while continuar_interacao:
    continuar_interacao = interagir_com_fazenda(fazenda_de_bichinhos)