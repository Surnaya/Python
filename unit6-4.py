class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Car {self.name} rides'

    def stop(self):
        return f'Car {self.name} stopped'

    def turn_right(self):
        return f'Car {self.name} turned right'

    def turn_left(self):
        return f'Car {self.name} turned left'

    def show_speed(self):
        return f'Car {self.name} speed is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'Car {self.name} speed is {self.speed}'
        if self.speed > 60:
            print("Over speed")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Car {self.name} speed is {self.speed}')
        if self.speed > 40:
            return f'Over speed'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

bmw = SportCar(120, 'Red', 'BMW', False)
kia = TownCar(70, 'White', 'Kia', False)
gaz = WorkCar(50, 'Grey', 'GAZ', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(bmw.turn_left())
print(ford.stop())
print(kia.show_speed())
print(gaz.show_speed())
