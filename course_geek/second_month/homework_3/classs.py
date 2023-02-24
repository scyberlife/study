
class Hero:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
class Hero_super(Hero):
    def __init__(self, name, ability):
        super().__init__(name, ability)
    def __str__(self):
        return f'{self.name} {self.ability}'

    def pokaz(self):
        return f'{self.name} it is super_hero'