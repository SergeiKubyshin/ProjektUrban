class House:
    def __init__(self, name, number_of_flours):
        self.name = name
        self.number_of_flours = number_of_flours


    def go_to(self, new_flour):
        self.new_flour = new_flour
        a = 0
        while a < self.new_flour:
            a += 1
            print(a)


        if self.new_flour > self.number_of_flours or self.number_of_flours < 1:

            print(f'Такого этажа в {self.name} нет')
        else:
            print(f'Я живу в {self.name} на {self.new_flour} этаже')

h1 = House('Горский', 18)
h2 = House('Домик в деревне', 2)
print('Название ЖК:', h1.name, ',количество этажей:', h1.number_of_flours)
print('Название ЖК:',h2.name, ',количество этажей:',h2.number_of_flours)
h1.go_to(5)
h2.go_to(10)




