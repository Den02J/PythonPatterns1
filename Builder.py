
class Client:
    def __init__(self, builder):
        self.firstName = builder.firstName
        self.lastName = builder.lastName
        self.bank = builder.bank
        self.balance = builder.balance

    def __str__(self):
        return f"{self.firstName} {self.lastName}\n{self.bank}: {self.balance}"

    class Builder:
        firstName = None
        lastName = None
        bank = None
        balance = None

        def setFirstName(self, firstName):
            self.firstName = firstName

        def setLastName(self, lastName):
            self.lastName = lastName

        def setBank(self, bank):
            self.bank = bank

        def setBalance(self, balance):
            self.balance = balance

        def build(self):
            return Client(self)


if __name__ == "__main__":
    clientBuilder = Client.Builder()
    clientBuilder.setFirstName("Mario")
    clientBuilder.setLastName("Red")
    clientBuilder.setBank("Oshad")
    clientBuilder.setBalance(2060)

    client1 = clientBuilder.build()
    print(client1)

