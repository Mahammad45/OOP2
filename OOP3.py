from os import system
system('clear')

# Есть 2 вида наследования 
# 1: Наследования
# 2: Множественное наследования
# Описания
# Наследования - это когда класс наследует все атрибуты и методы у родителя



# 1: Наследования
# class Animal:
#     def __init__(self, name, voice) -> None:
#         self.name = name
#         self.voice = voice

#     def lisetening(self):
#         return f"Какой-то звук"

#     def __str__(self) -> str:
#         return f"{self.name} говорит {self.voice}"


# class Cat(Animal):
#     def __init__(self, name, voice, color) -> None:
#         super().__init__(name, voice)
#         self.color = color

#     # def lisetening(self):
#     #     return f"{self.name} говорит {self.voice}"

#     def __str__(self) -> str:
#         return super().__str__()
    
# class Dog(Animal):
#     def __init__(self, name, voice, color) -> None:
#         super().__init__(name, voice)
#         self.color = color

#     def lisetening(self):
#         return f"{self.name} говорит {self.voice}"

#     def __str__(self) -> str:
#         return super().__str__()

# cat1 = Cat("Barsik", "meow", "black")
# dog1 = Dog("Riley", "woof", "brown")
# print(cat1.lisetening())
# print(dog1.lisetening())
# print(dog1)


# 2: Множественное наследования
class A:
    def __init__(self,name) -> None:
        self.name = name

class B(A):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age

class C(A):
    def __init__(self, name, ) -> None:
        super().__init__(name)

class D(B):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color = color
