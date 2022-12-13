
class PrivatBank:
    def __init__(self):
        """Empty constructor"""

    @staticmethod
    def show():
        print("This is Privat Bank")


class MonoBank:
    def __init__(self):
        """Empty constructor"""

    @staticmethod
    def show():
        print("This is Mono Bank")


def createBank(name):

    factory_dict = {
        "privat": PrivatBank,
        "mono": MonoBank
    }
    return factory_dict[name]


if __name__ == '__main__':
    bank1 = createBank("mono")
    bank2 = createBank("privat")

    bank2.show()
    bank1.show()


