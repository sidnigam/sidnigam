def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)


add(2, 3, 4, 6, 5, 5, 6)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Toyota", model="RAV4")

print(my_car.color)