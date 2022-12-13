
class BankClient:
    __instance = None
    balance = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        pass

    def increaseBalance(self):
        self.balance += 1

    def showBalance(self):
        print(self.balance)


if __name__ == '__main__':
    client1 = BankClient()
    client1.increaseBalance()
    client1.showBalance()

    client2 = BankClient()
    client2.increaseBalance()
    client2.showBalance()

    print(id(client1))
    print(id(client2))


