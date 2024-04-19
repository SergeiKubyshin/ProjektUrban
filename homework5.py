# список
my_list = ['яблоко', 'груша', 'слива', 'вишня', 'виноград', 'абрикос']
print('List: ', my_list)
print('First: ', my_list[0], 'Last: ', my_list[-1]) # вывод первого и последнего элемента
print('Sublist: ', my_list[2:4]) # подсписок с 3 по 5
my_list[4] = 'чебурашка' # изменение значения 3 элемента
print('Modified list: ', my_list)
# словари
my_dict = {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
print('Dictionary: ', my_dict)
print('Translation: ', my_dict.get('orange'))
my_dict['kiwi'] = 'Киви' # добавление нового элемента в словарь
print('Modified dictionary: ', my_dict)
