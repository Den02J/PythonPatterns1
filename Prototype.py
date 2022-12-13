
from abc import ABCMeta, abstractstaticmethod


class IPrototype(metaclass=ABCMeta):

    @abstractstaticmethod
    def clone():
        """Clone method"""


class BankClient(IPrototype):

    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def clone(self):
        return type(self)(
            self.first_name,
            self.last_name,
            self.balance
        )

    def __str__(self):
        return f"{id(self)}\nFirst name: {self.first_name}\nLast name: {self.last_name}\nBalance: {self.balance}\n"


if __name__ == '__main__':

    client1 = BankClient("Mark", "Claw", 1050)
    client2 = client1.clone()

    print(client1)
    print(client2)
