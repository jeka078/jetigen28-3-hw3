class Bank():
    def __init__(self, name, balanse):
        self.name = name
        self.balanse = balanse

    def moneyX(self):
        add = int(input('Введите сумму которую хотите добавить на свой счёт: '))
        self.balanse += add
        print(f'Счёт пополнен на: {self.balanse}')

    def kill(self):
        return self.balanse == int(0)

    def __jackpot(self):
        self.balanse *= 10

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Баланс: {self.balanse}'

    def __unite_balanse(self, other):
        self.balanse += other.balanse


me = Bank(name="Daniel", balanse=100)
you = Bank(name="Eldar", balanse=100)

me._Bank__unite_balanse(you)

print(me.balanse)
print(you.balanse)




class Gs(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_balanse(self):
        return self._balanse

    def set_balanse(self, balanse):
        self._balanse = balanse


class Property(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)

    @property
    def gotname(self):
        return f'I\'m {self.name}'

    @property
    def gotbalanse(self):
        return f'balanse: {self.balanse}'

a = Property("Victor", 200)
b = Gs("igor", 100)
print(a.gotbalanse)
print(a.gotname)
print(b.kill())
print(b.set_balanse(120))