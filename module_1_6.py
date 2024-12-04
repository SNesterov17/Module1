     # работа со словарями
my_dict = {'Slava': 1965, 'Olga': 1966, 'Oleg': 1964}
print(my_dict)
print(my_dict['Oleg'])
my_dict['Inga'] = 1967
print(my_dict['Inga'])
my_dict.update({'Semen': 1973, 'Artur': 1980})
del my_dict['Slava']
print(my_dict.get('Slava'))
print(my_dict)
     # работа с множествами
my_set = {1, 2, 7, 15, 'tea', 23,  34, 2, 23}
print(my_set)
my_set.update([17, 'шмель'])
my_set.remove('tea')
print(my_set)