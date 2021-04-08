class Car:

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return print(f"Машина {self.name} начила движение")

    def stop(self):
        return print(f"Машина {self.name} оставновилась")

    def turn(self):
        vect = input("Введите направление движения: ")
        return print(f"Машина {self.name} движется в направлении {vect}")

    def show_speed(self):
        return print(f"Ваша скорость: {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return print(f"Машина {self.name} движется с превышением скорости")


class SportCar(Car):

    def show_speed(self):
        if self.speed > 200:
            return print(f"Поздравляю вы попали в аварию")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f"Машина {self.name} цвета {self.color} движется с превышением скорости")


class PoliceCar(Car):

    def police(self):
           return print("Вас не любят")


a = TownCar("Kia", 90, "Black")
a.go()
a.turn()
a.show_speed()
a.stop()
b = SportCar("Lambo", 230, "Red")
b.go()
b.turn()
b.stop()
b.show_speed()
c = PoliceCar("Ford", 80, "White")
c.go()
c.turn()
c.show_speed()
c.stop()
c.police()
f = WorkCar("Lada", 70, "Baklajan")
f.go()
f.turn()
f.show_speed()
f.stop()