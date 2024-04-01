import random

class Moeda:
    def __init__(self, jogadorUm, jogadorDois):
        self.faceMoeda = ["Cara" , "Coroa"]
        self.jogadorUm = jogadorUm
        self.jogadorDois = jogadorDois
        
    def lancarMoeda(self, escolhaJogador1, escolhaJogador2):
        print("Moeda lançada!")
        faceSorteada =  random.choice(self.faceMoeda)
        
        print(f"Deu {faceSorteada}!")
        if faceSorteada == escolhaJogador1:
            print(f"{self.jogadorUm} venceu!")
        elif faceSorteada == escolhaJogador2:
            print(f"{self.jogadorDois} venceu!")
            
class Jogadores:
    def __init__(self, jogadorUm, jogadorDois):
        self.jogadorUm = jogadorUm
        self.jogadorDois = jogadorDois
        
    def sortearEscolha(self):
        listaJogadores = [self.jogadorUm, self.jogadorDois]
        random.shuffle(listaJogadores)
        self.jogadorUm = listaJogadores[0]
        self.jogadorDois = listaJogadores[1]
        
    def escolher(self):
        while True:
            try:
                escolha1 = int(input(f"{self.jogadorUm}, digite 1 para 'Cara' e ou 2 para 'Coroa': "))
                if escolha1 == 1 or escolha1 == 2:
                    break
                else:
                    print("Por favor, digite apenas 1 ou 2.")
            except ValueError:
                print("Por favor, digite um número inteiro.")
                
        escolha2 = ""
        if escolha1 == 1:
            escolha1 = "Cara"
            escolha2 = "Coroa"
        elif escolha1 == 2:
            escolha1 = "Coroa"
            escolha2 = "Cara"
            
        return escolha1, escolha2

print("Bem vindo ao jogo 'Cara ou Coroa'! \nSiga os passos para jogar! \n 1- Você vai definir o nome dos jogadores. \n2- Na base do sorteio, um dos dois jogadores escolherão entre 'Cara' ou 'Coroa'. A opção que sobrar ficará com o jogador que não foi sorteado! \n3- A moeda será lançada e definirá quem vai vencer o jogo! \n4- Digite 1 para jogar novamente. Se não, digite 0! \nDivirtam-se!\n")

while True:
    jogadores = Jogadores(input("Digite o nome de um jogador: "), input("Digite o nome de outro jogador: "))
    jogadores.sortearEscolha()
    escolhaJogadorUm, escolhaJogadorDois = jogadores.escolher()
    
    moeda = Moeda(jogadores.jogadorUm, jogadores.jogadorDois)
    moeda.lancarMoeda(escolhaJogadorUm, escolhaJogadorDois)
    
    jogo = ""
    while jogo != "S" and jogo != "N":
        jogo = input("\nDeseja jogar novamente? Digite 'S'. Se não, digite 'N' para finalizar o programa: ")
        jogo = jogo.upper()
        if jogo != 'S' and jogo != 'N':
            print("ERRO! Digite corretamente!")
    if jogo == 'N':
        print("Programa Finalizado! Obrigado por jogar este jogo!")
        break
    else:
        print("Jogo Reiniciado!")