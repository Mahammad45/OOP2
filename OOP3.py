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
        return(f"Animal {self.name} and voice {self.voice}")
    
    pass