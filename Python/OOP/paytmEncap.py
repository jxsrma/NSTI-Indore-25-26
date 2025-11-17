class UPIApp:
    def __init__(self, balance: float, name: str, pan: str, pin):
        self.Name = name
        self._PAN = pan
        self.__Balance = balance
        self.__PIN = pin

    def __getBalance(self):
        return self.__Balance

    def __setBalance(self, newBal: float):
        self.__Balance = newBal
        return True

    def deposit(self, amount: float):
        self.__setBalance(self.__getBalance()+amount)
        print(
            f"Amount {amount} Deposited in {self.Name}'s account\nNew Balance {self.__getBalance()}")

    def withdrawl(self, amount: float):
        if self.__getBalance() >= amount:
            EnteredPIN = int(input("Please Enter PIN: "))
            if EnteredPIN == self.__PIN:
                self.__setBalance(self.__getBalance()-amount)
                print(
                    f"Amount {amount} Withdrawl from {self.Name}'s account\nNew Balance {self.__getBalance()}")
            else:
                print("Incorrect PIN, Please Try Again")
        else:
            print("Insufficient Balance")

    def checkBalance(self):
        print(f"{self.Name}'s Account Balance: ", self.__getBalance())


Paytm = UPIApp(5000, "Jash", "OASD8791U", 8866)

# print(Paytm.__Balance) #Because it is Private
# print(Paytm.Name)
# Paytm.Name = "Ram"

# print(Paytm.Name)
# print(Paytm._PAN)

Paytm.deposit(500)
Paytm.checkBalance()

Paytm.withdrawl(2)
Paytm.checkBalance()

Paytm.withdrawl(300)
