from fastapi import FastAPI

app = FastAPI()

class Coke:
    pass

class Soda:
    pass

class VendingMC:
    def __init__(self):
        self.coke = []
        self.soda = []

    def get_coke(self, n):
        for _ in range(n):
            self.coke.append(Coke())

    def get_soda(self, n):
        for _ in range(n):
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
    def __init__(self):
        self.drink = None

    def buy_coke(self, vm):
        self.drink = vm.sell_coke()
        if self.drink is None:
            return "콜라 없음"
        return "콜라 구매 완료"

@app.get("/")
def home():
    vm = VendingMC()
    vm.get_coke(3)

    customer = Customer()
    result = customer.buy_coke(vm)

    return {"result": result}
