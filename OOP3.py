from os import system
system('clear')

class Animal:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def speak(self):
        return("I am an animal")

    def lissings(self):
        return(f"Каклй-то звук {self.name} и я слышу {self.voice}")
    
    def __str__(self) -> str:
        return(f"Animal {self.name} говорит {self.voice}")
    

class Cat(Animal):
    def __init__(self, name, voice, color):
        super().__init__(name, voice)
        self.color = color

    def lissings(self):
        return(f"Meow! I am {self.name} and my color is {self.color}")
    def __str__(self) -> str:
        return(f"Cat {self.name} and voice {self.voice} and color {self.color}")
    
class Dog(Animal):
    def __init__(self, name, voice, color):
        super().__init__(name, voice)
        self.color = color

    def lissings(self):
        return super().lissings()

    def __str__(self) -> str:
        return(f"Dog {self.name} and voice {self.voice} and color {self.color}")
    
cat=Cat("Barsik", "Meow", "Black")
cat1=Cat("Murzik", "Meow", "White")
cat2=Cat("Vaska", "Meow", "Gray")
cat3=Cat("Pushok", "Meow", "Brown")
dog=Dog("Sharik", "Woof", "Brown")
dog1=Dog("Tuzik", "Woof", "Black")
dog2=Dog("Rizhik", "Woof", "Gray")


# print(dog2) # STR
# print(dog1.lissings())
# print(dog.speak())
# print(cat1.lissings())
# print(cat2.lissings())
# print(cat3.lissings())

class A:
    def __init__(self,A):
        self.a=1        
        self.b=2


    def __str__(self) -> str:
        return(f"A {self.a} B {self.b}")

object_1=A(1) 

# print(object_1)
# print(object_1.b)

