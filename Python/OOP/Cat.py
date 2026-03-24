class Cat:
    legs = 4

    @classmethod
    def speak(cls):
        print("Meow",cls.legs)

    @staticmethod
    def age(year):
        print("Cat's age is", 2025-year)

    def __init__(self, catName):
        self.name = catName
        print(f"{catName} Object Created")

    def tellYourName(self):
        print(f"My name is {self.name}")


if __name__ == "__main__":

    Coco = Cat("Coco")
    Momo = Cat("Momo")
    Billu = Cat("Billu")

    Coco.tellYourName()
    Momo.tellYourName()
    Billu.tellYourName()
    print(Coco.name)
    print(Coco.legs)
    print(Cat.legs)

    Coco.legs = 3
    print(Coco.legs)

    Cat.legs = 2
    print(Cat.legs)

    Cat.age(year=2023)

    Cat.speak()
