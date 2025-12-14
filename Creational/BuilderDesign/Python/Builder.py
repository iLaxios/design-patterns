class Car:

    def __init__(self):
        self.color : str|None = None
        self.engine : str|None = None
        self.transmission : str|None = None

    def __str__(self):
        return (
            f"Car(color={self.color!r}, engine={self.engine!r}, "
            f"transmission={self.transmission!r})"
        )


class CarBuilder:

    def __init__(self):
        self.car = Car()

    def addColor(self, color: str) -> 'CarBuilder':
        self.car.color = color
        return self
    
    def addEngine(self, engine: str) -> 'CarBuilder':
        self.car.engine = engine
        return self
    
    def addTransmission(self, transmission: str) -> 'CarBuilder':
        self.car.transmission = transmission
        return self
    

    def build(self):
        return self.car
    

if __name__ == "__main__" :

    carBuilder = CarBuilder()

    car = carBuilder.addColor("Blue").addEngine("V8").addTransmission("Manual").build()
    print(car)

        