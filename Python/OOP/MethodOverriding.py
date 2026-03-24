class Animal:
    def __init__(self, name):
        self.Name = name

    def speak(self):
        print(self.Name, "Speak")


class Cat(Animal):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name)

    def detail(self):
        print(f"Name: {self.Name}\nColor: {self.color}")

    def speak(self):
        print(f"{self.Name} Meow")


class Cheeta(Cat):
    def __init__(self, name, color, speed):
        self.speed = speed
        super().__init__(name, color)

    def detail(self):
        print(f"Name: {self.Name}\nColor: {self.color}\nspeed: {self.speed}")

    def speak(self):
        print(f"{self.Name} Meow")


Coco = Animal("Coco")

Coco.speak()

Momo = Cat("Momo", "White")
Momo.detail()



def beating(cat):
    cat.speak()
    
beating(Momo)