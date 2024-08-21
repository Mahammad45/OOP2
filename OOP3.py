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
    def __init__(self, name) -> None:
        # Конструктор класса A, инициализирующий объект с атрибутом name
        self.name = name  # Сохраняем значение name в атрибуте объекта

class B(A):
    def __init__(self, name, age) -> None:
        # Конструктор класса B, который наследует от класса A
        super().__init__(name)  # Вызов конструктора родительского класса A для инициализации name
        self.age = age  # Сохраняем значение age в атрибуте объекта

class C(A):
    def __init__(self, name, age) -> None:
        # Конструктор класса C, который также наследует от класса A
        super().__init__(name)  # Вызов конструктора родительского класса A для инициализации name
        self.age = age  # Сохраняем значение age в атрибуте объекта

class D(B):
    def __init__(self, name, age, color) -> None:
        # Конструктор класса D, который наследует от класса B
        super().__init__(name, age)  # Вызов конструктора родительского класса B для инициализации name и age
        self.color = color  # Сохраняем значение color в атрибуте объекта
