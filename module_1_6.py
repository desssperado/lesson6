from operator import truediv

my_dict = {'Anton': 1989, 'Max': 1999, 'Liza': 2000}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Denis'))
my_dict.update({'Oled': 1995, 'Olga': 1993})
del my_dict['Liza']
print(my_dict.pop('Max'))
print(my_dict)

my_set = {1, 'Виноград', 34.324, 34.324, 1, 'Виноград'}
my_set = set(my_set)
print(my_set)
my_set.add(34), my_set.add((7, 8, 9))
my_set.remove(1)
print(my_set)





