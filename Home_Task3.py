class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname


    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


test = Position ('Иван', 'Иванов', 'Инженер', '20000', '1000')
print(test.get_full_name(), test.get_total_income())
test = Position ('Петров', 'Петрович', 'Электромонтер', '13000', '2000')
print(test.get_full_name(), test.get_total_income())