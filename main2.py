class Coke:
    pass

class Soda:
    pass


class VendingMC:
    def __init__(self):
        self.coke = []
        self.soda = []

    def get_coke(self, n_coke):
        for _ in range(n_coke):
            self.coke.append(Coke())

    def get_soda(self, n_soda):
        for _ in range(n_soda):
            self.soda.append(Soda())

    def sell_coke(self):
        if len(self.coke) == 0:
            return None
        return self.coke.pop()

    def sell_soda(self):
        if len(self.soda) == 0:
            return None
        return self.soda.pop()


class Customer:
    def __init__(self, name):
        self.name = name
        self.drink = None

    def buy_coke(self, vm):
        self.drink = vm.sell_coke()
        if self.drink is None:
            print(self.name + " : 콜라 없음")
        else:
            print(self.name + " : 콜라 구매 성공")

    def buy_soda(self, vm):
        self.drink = vm.sell_soda()
        if self.drink is None:
            print(self.name + " : 소다 없음")
        else:
            print(self.name + " : 소다 구매 성공")


# 실행
vm = VendingMC()
vm.get_coke(2)
vm.get_soda(1)

print("=== 자판기 시작 ===")

c1 = Customer("손님1")
c2 = Customer("손님2")

c1.buy_coke(vm)
c2.buy_soda(vm)
c1.buy_coke(vm)
c2.buy_coke(vm)

print("=== 종료 ===")