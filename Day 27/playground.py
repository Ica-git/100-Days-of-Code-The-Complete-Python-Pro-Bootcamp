
def add(*args):
    SUM = sum(args)
    return SUM

print(add(5,10,6,7,8,9))

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make = "Nissan", model = "GTR")
print(my_car.make, my_car.model)

