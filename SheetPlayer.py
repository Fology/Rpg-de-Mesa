class Ficha:
    def __init__(self, name_person, name_player, class_p, race):
        self.name_person = name_person
        self.name_player = name_player
        self.class_p = class_p
        self.race = race
        self.experience = 0
        self.level = 1

    def xp_gained(self, xp):
        self.experience += xp
        self.lim_exp = 800
        if self.experience >= self.lim_exp:
            self.level += 1
            self.lim_exp *= 1.5

    def status(self, mod_class=0):
        self.life = 100 * mod_class
        self.mana = 100 * mod_class
        self.strength = 10 + mod_class
        self.dexterity = 10 + mod_class
        self.constitution = 10 + mod_class
        self.intelligence = 10 + mod_class
        self.wisdom = 10 + mod_class
        self.charisma = 10 + mod_class
        self.race_spell = mod_class
        self.race_effect = mod_class

    def Expertises(self):
        self.expertises = list
        self.expertises.append(self.race)

    def Equipments(self, weapon, armor, itens):
        self.weapon: list = weapon
        self.armor: list = armor
        self.itens: list= itens

    def Spells(self, spells):
        self.spell = list
        self.spell.append(spells)