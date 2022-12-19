# 3) Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
salary = {
    'wage': 15000.00,
    'bonus': 8000.50
}

class Worker:

    def __init__(self, w_name, w_surname, w_position, w_income = salary):
        self.w_name = w_name
        self.w_surname = w_surname
        self.w_position = w_position
        self.w_income = w_income

class Position(Worker):

    def __init__(self, w_name, w_surname, w_position, w_income):
        super().__init__(w_name, w_surname, w_position, w_income)

    def get_full_name(self):
        print(f'{self.w_name} {self.w_surname}')

    def get_total_income(self):
        wage = self.w_income['wage']
        bonus = self.w_income['bonus']
        print(f'Заработная плата составляет: {wage + bonus} руб.')

p = Position('Сергей', 'Сиволонский', 'водитель', salary)
p.get_full_name()
p.get_total_income()

