class Calk:
    def __init__(self,numberone ,numbertwo):
        self.numberone = numberone
        self.numbertwo = numbertwo

    def add(self):
        return self.numberone + self.numbertwo

    def sub(self):
        return self.numberone - self.numbertwo

    def mull(self):
        return self.numberone * self.numbertwo

    def truediv(self):
        return self.numberone / self.numbertwo


on =Calk(15 ,45)
print(on.add())
print(on.sub())
print(on.mull())
print(on.truediv())