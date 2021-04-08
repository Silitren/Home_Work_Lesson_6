import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']


    def running(self, __color):
        index = 0
        while index < 3:
            print(self.__color[index])
            if index == 0:
                time.sleep(7)
            elif index == 1:
                time.sleep(2)
            else:
                time.sleep(8)
            index += 1

zapusk = TrafficLight()
zapusk.running(0)
