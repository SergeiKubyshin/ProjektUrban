def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params() #без параметров

print_params(b = 25, c = 5)

print_params(23,b = 25, c = 23)

print_params(b = 25)

print_params(c = [1,2,3])

values_list = [1, 'ok', True]
values_dict = {'a':5, 'b':'home', 'c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'Finger']

print_params(*values_list_2, 42)
