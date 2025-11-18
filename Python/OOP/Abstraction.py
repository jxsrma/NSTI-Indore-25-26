from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def engineStart(self):
        pass


class petrolVehical(Car):

    def engineStart(self):
        print("Starting the engine with Petrol")
        print("Engine Started")


class electricVehical(Car):

    def engineStart(self):
        print("Motor started")


if __name__ == "__main__":
    TataP = petrolVehical()
    TataE = electricVehical()

    TataP.engineStart()
    TataE.engineStart() 