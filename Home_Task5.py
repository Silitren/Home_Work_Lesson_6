class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print(self.title)
        print("Рисуем ручкой")


class Pencil(Stationery):

    def draw(self):
        print(self.title)
        print("Рисуем карандашом")


class Handle(Stationery):

    def draw(self):
        print(self.title)
        print("Рисуем маркером")

start = Stationery("Набор")
start.draw()
a = Pen("Ручка")
a.draw()
b = Pencil("Карандаш")
b.draw()
c = Handle("Маркер")
c.draw()
