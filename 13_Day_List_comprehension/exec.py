"""Exercises: Day 13
Filter only negative and zero in the list using list comprehension
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtro = [i for i in numbers if i <= 0]
print(filtro)

"""Flatten the following list of lists of lists to a one dimensional list :
"""

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [number for row in list_of_lists for number in row]
print(flattened)

"""Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""
tuplas = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)] 
print(tuplas)


""" Flatten the following list to a new list:
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened = [i for row in countries for i in row]
print(flattened)

"""
Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': country.upper(), 'city': capital.upper()} 
        for row in countries 
        for (country, capital) in row]

print(output)

"""
Change the following list of lists to a list of concatenated strings:

"""

names = [[('Asabeneh', 'Yetaneh', '22')], [('David', 'Smith', '33')], [('Donald', 'Trump', '44')], [('Bill', 'Gates', '55')]]

fullnames = [f"Nombre: {first} Apellido: {last} Dni: {dni}" for [(first, last, dni)] in names]
print(fullnames)

# Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
