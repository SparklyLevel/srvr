class Transport:
    def __init__(self, fuel, title):
        self.fuel_capacity = fuel
        self.title = title

    def __str__(self) -> str:
        return f'крута {self.fuel_capacity} {self.title}'


class Car(Transport):
    def __init__(self, fuel: int, title: str, SScolor: str, HappyWheels: str):
        super().__init__(fuel, title)
        self.color = SScolor
        self.wheelsResin = HappyWheels

    def Bibika(self):
        print('woaw')


class Boat(Transport):
    def __init__(self, fuel: int, title: str, bColor: str, seatMaterial: str):
        super().__init__(fuel, title)
        self.color = bColor
        self.assMaterial = seatMaterial
