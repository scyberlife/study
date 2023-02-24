class One:
    def __init__(self, name):
        self.name = name

class Two:
    def __init__(self, age):
        self.age = age

class Three:
    def run(self):
        return 'run'

class Four:
    def fly(self):
        return 'fly'

class Five(One, Two, Three, Four):
    def __init__(self, name, age):
        One.__init__(self, name)
        Two.__init__(self, age)
    def jump(self):
        return 'jump'