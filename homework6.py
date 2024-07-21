my_dict = {'Dmitry': 2002, 'Anton': 2001, 'Denis': 2003, 'Sveta': 1998}
print(my_dict)
print(my_dict.get('Dmitry'))
print(my_dict.get('Nikita'))
my_dict.update({'Vasya': 2006,
                'Masha': 1987})
del my_dict ['Denis']
print(my_dict)

#-------------------------------------------------------------------------------

my_set = {True, True, True, False, False, 2,3,3,3,2, 'home', 'home', 'mice' }
print(my_set)
my_set.add((5,6))
my_set.discard('mice')
print(my_set)