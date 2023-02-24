class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def info(self):
        return self.name

    def health(self):
        return f'{self.health_points * 2}'

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

    def phrase(self):
        return 'fly in the True_phrase'

    def gen_x(self):
        pass

    def crit(self):
        return f'{self.damage ** 2}'

class SoilHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
    soil = 'Soil'
    damage = False
    fly = False
    def health(self):
        fly = True
        return f'{self.health_points ** 2} {fly}'

class FlyHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
    flyy = 'Flyy'
    damage = False
    fly = False
    def health(self):
        fly = True
        return f'{self.health_points ** 2} {fly}'

class Villian(SoilHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        SoilHero.__init__(name, nickname, superpower, health_points, catchphrase)
    people = 'monster'

h1 = SuperHero('Sergei', 'Sergei2', 'sleep', 100, 'hello')
h2 = SoilHero('Sergei', 'Sergei2', 'sleep', 100, 'hello')
h3 = FlyHero('Sergei', 'Sergei2', 'sleep', 100, 'hello')
print(h1, h1.info(), h1.health(), len(h1), h2, h2.phrase(), h2.health(), h3, h3.health(), h3.crit())