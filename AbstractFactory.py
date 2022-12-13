from abc import abstractmethod, ABCMeta


class Bank(metaclass=ABCMeta):
    def __init__(self):
        """"""

    @abstractmethod
    def show(self): pass


class Account(metaclass=ABCMeta):
    def __init__(self):
        """"""

    @abstractmethod
    def show(self): pass


class PrivatBank(Bank):
    def show(self):
        print("This is PrivatBank")


class MonoBank(Bank):
    def show(self):
        print("This is MonoBank")


class SalaryAccount(Account):
    def show(self):
        print("This is SalaryAccount")


class SavingsAccount(Account):
    def show(self):
        print("This is SavingsAccount")


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def createBank(self) -> Bank: pass

    @abstractmethod
    def createAccount(self) -> Account: pass


class PrivatBankFactory(AbstractFactory):
    @staticmethod
    def createBank() -> Bank:
        return PrivatBank()


class MonoBankFactory(AbstractFactory):
    @staticmethod
    def createBank() -> Bank:
        return MonoBank()


class SalaryAccountFactory(AbstractFactory):
    @staticmethod
    def createAccount() -> Account:
        return SalaryAccount()


class SavingsAccountFactory(AbstractFactory):
    @staticmethod
    def createAccount() -> Account:
        return SavingsAccount()


if __name__ == "__main__":
    bankFactory1 = MonoBankFactory
    bankFactory2 = PrivatBankFactory

    bank1 = bankFactory1.createBank()
    bank1.show()
    bank2 = bankFactory2.createBank()
    bank2.show()

    accountFactory1 = SavingsAccountFactory
    accountFactory2 = SalaryAccountFactory

    account1 = accountFactory1.createAccount()
    account1.show()
    account2 = accountFactory2.createAccount()
    account2.show()
