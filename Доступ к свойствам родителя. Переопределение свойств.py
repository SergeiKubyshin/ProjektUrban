class Vehicle:
    def __init__(self, owner):
        self.owner = owner
        self.__model = 'Toyota Mark II'
        self.__engine_power = 500
        self.__color = 'blue'
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']


    def get_model(self): # возвращает строку: "Модель: <название модели транспорта>"
        def __str__(self):
            return f'{self.__model}'
        print('Модель: ', self.__model)


    def get_horsepower(self): # возвращает строку: "Мощность двигателя: <мощность>"
        def __str__(self):
            return f'{self.engine_power}'

        print('Мощность: ', self.__engine_power)

    def get_color(self): # возвращает строку: "Цвет: <цвет транспорта>"
        def __str__(self):
            return f'{self.__color}'

        print('Цвет: ', self.__color)
    def print_info(self): # - распечатывает результаты методов
        print(f'Модель: {self.__model}  Мощность:  {self.__engine_power} Цвет: {self.__color} Владелец: {self.owner}')
    def set_color(self, new_color): #- принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на: {new_color}')


class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Den')
vehicle1.print_info()
vehicle1.get_model()
vehicle1.get_color()
vehicle1.get_horsepower()
vehicle1.set_color('red')
vehicle1.set_color("GREEN")


# Изначальные свойства
#vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
# vehicle1.set_color('Pink')
# vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
#vehicle1.print_info()

