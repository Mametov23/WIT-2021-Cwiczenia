class dog: 
    def __init__(self, name, kind): 
        self.name = name 
        self.kind = kind
    
    def walk(self): 
        print('Ok, ide')

    def brak(self):
        print('Hau hau')

#dog1 = dog('Burek', 'Kundel')
#dog1.walk()
#dog1.bark()


class cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self): 
        print('Meow meow')

#cat1 = cat ('Mruczek', 'Rudy')
#print(cat1.color)
#cat1.meow()

#cat2 = cat('Filemon', 'Czarny')
#print(cat2.name)
#cat2.meow()


class Human: 
    def _init_(self, name, height, weight): 
        self.name = name
        self.height = height
        self.weight = weight

    def drink_milk(self): 
        print('Drink milk...')

noworodki = {}
human1 = Human('A', 50, 3.5)
human2 = Human('B', 60, 4)
human3 = Human('C', 45, 3)

noworodki['A'] = human1
noworodki['B'] = human2
noworodki['C'] = human3

for name, human, in noworodki.items(): 
    #print(name, vars(human))
    human.drink_milk()