class Equipment():
    def __init__(self):
        return print("If you want to add a weapon, call the method (Weapon), if armor (Armor)\n"
                     "(Weapon) name, damage, weigth, cost, upgrade(if there is) \n"
                     "(Armor) piece, name, damage, weigth, cost, upgrade(if there is)")

    def Weapon(self,name ,tipe ,damage, weigth, cost, upgrades=None):
        pass

    def Armor(self, piece, tipe, name, defense, weigth, cost, upgrade=None):
        pass

    def Iten(self, name, use):
        pass

gato = Equipment()