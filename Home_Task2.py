class Road:


    def __init__(self, length, width):
        self._length = length
        self._width = width


    def mass_asfalt(self):
        return self._length * self._width * 25 * 5


a = Road (int(input("Введите длину: ")), int(input("Введите ширину: ")))
print(f"Масса требуемого асфальта: {a.mass_asfalt()}")