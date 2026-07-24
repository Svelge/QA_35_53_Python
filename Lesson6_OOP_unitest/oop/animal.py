class Animal:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        return "..."

# далее класс объекта наследует Энимал и его правило введения имени
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.name, "says", dog.make_sound())
print(cat.name,"says",cat.make_sound())

class Fish(Animal):
    pass

fish = Fish("Nemo")
print(fish.name,"says",fish.make_sound())


