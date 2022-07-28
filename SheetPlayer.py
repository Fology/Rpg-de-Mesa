class Ficha:
    def __init__(self, nome_personagem, nome_jogador, classe, raca, subclasse="NoN"):
        self.nome_personagem = nome_personagem
        self.nome_jogador = nome_jogador
        self.classe = classe
        self.raca = raca
        self.subclasse = subclasse

    def mostra(self):
        a = (f'O nome do player é {self.nome_jogador} e seu personagem é o/a {self.nome_personagem} da raça {self.raca}.'
                f'\nEle é da classe {self.classe} ')
        if self.subclasse != "NoN":
            b = (f'e subclasse {self.subclasse}')
            print(a + b)
        else:
            print(a)


fology = Ficha('Fology', 'Gabriel', 'Ladino', "Elfo", "Guerreiro")

fology.mostra()
