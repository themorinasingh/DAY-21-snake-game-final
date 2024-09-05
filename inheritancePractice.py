class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")

class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"

    def bark(self):
        super().bark()
        print("Hello Good Sir, How do you do?")


doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")

sparky.bark()