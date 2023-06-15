class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def sounding(self):
        print(f'{self.sound}!!')

croc = Animal('crocodile', 'snap!')
croc.sounding()