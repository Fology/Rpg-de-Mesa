class Ficha:
    def __init__(self, nome_personagem, nome_jogador, classe, raca, subclasse="NoN"):
        self.nome_personagem = nome_personagem
        self.nome_jogador = nome_jogador
        self.classe = classe
        self.subclasse = subclasse
        self.raca = raca

    def mostra(self):
        return (f'O nome do player é {self.nome_jogador} e seu personagem é o/a {self.nome_personagem} da raça {self.raca}.'
                f'\nEle é da classe {self.classe} e subclasse {self.subclasse}')


fology = Ficha('Fology', 'Gabriel', 'Ladino', "Elfo")

print(fology.mostra())
