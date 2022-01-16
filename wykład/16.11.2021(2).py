class Animal: 
    def _init_(self, name): 
        self.name

    def eat(self): 
        print('Eathing...')

class Dog(Animal):
    def _init_(self, name, kind): 
        super()._init_(name)
        self.kind = kind

class Cat(Animal): 
    def __init__(self, name, color): 
        super()._init_(name)
        self.color = color
    
class Wolf(Dog):
    def _init_(self, name, kind, environment):
            super()._init_(name, kind)
            self.environment = environment

    def eat(self): 
        print('Wolf is eating...')

wolf1 = Wolf('Zly wilk', "wilk", 'Las')
print(isinstance(wolf, Wolf))
print(isinstance(wokf, t))

#print(wolf1.name)
#print(wolf1.kind)
#print(wolf1.environment)
#wolf1.eat()
#print(Wolf.__mro__)

#class Monitor: 
#    def _init_(self, height, weight, color, is_standing): 
#        self.height = height
#        self.weight = weight
#        self.color = color
#       self.is_standing = is_standing
#
#    def power_on(self):
#        print('///')
#    def power_off(self): 
#        print('///')


#dog1 = Dog('burek', 'kundel')
#print(dog1.name)
#print(dog1.kind)
#god1.eat()
#
#cat1 = Cat('Mruczek','Rudy')
#print(cat1.name)
#print(cat1.color)
#cat1.eat()


#class Dog: 
#   def __init__(self, name, kind): 
#        self.name = name
#        self.kind = kind
#
#    def eat(self): 
#        print('Eating...')