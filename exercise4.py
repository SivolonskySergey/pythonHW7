# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} start moving')

    def stop(self):
        print(f'{self.name} stop moving')

    def turn(self, direction):
        print(f'{self.name} turn {direction}')

    def show_speed(self):
        print(f'{self.name} has a speed {self.speed} km/h')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        print(f'{self.name} has a speed {self.speed} km/h')


class SportCar(Car):
    def init(self, speed, color, name, is_police):
        super().init(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        print(f'{self.name} has a speed {self.speed} km/h')


class PoliceCar(Car):
    def init(self, speed, color, name, is_police):
        super().init(speed, color, name, is_police)

t = TownCar(61, 'gray', 'VAZ', False)
t.show_speed()
print(t.color)
t.go()
t.turn('left')
t.stop()
w = WorkCar(41, 'blue', 'Toyota', False)
w.show_speed()
print(w.color)

p = PoliceCar(70, 'white', 'Camry', True)
p.show_speed()
print(p.color)
p.go()
p.turn('left')
p.stop()
print(p.is_police)