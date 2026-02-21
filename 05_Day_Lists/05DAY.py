empty = []

full = ['manzana', 'banana', 'sandia', 'pera', 'naranja']

print(len(full))

print(full[0])
print(full[2])
print(full[-1])

mixed_data_types = ['lucas', 29, 1.74, 'married', 'siempreviva123' ]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[2])
print(it_companies[-1])

it_companies.append('MercadoLibre')
it_companies.insert(3, 'Fernet')
it_companies[1] = it_companies[1].upper()
resultado = " #; ".join(it_companies)
print(it_companies)
print(resultado)

check = 'Facebook' in it_companies
print(check)

clon = it_companies.copy()
clon.sort()
print(clon)
clon.sort(reverse=True)
print(clon)

#del clon[:2]
#print(clon)
#del clon[4:]
#print(clon)
#del clon[2:4]
#print(clon)

clon.pop(0)
clon.pop(2)
clon.pop(-1)
print(clon, " hola")

#del it_companies
#print(it_companies)

"""Exercises: Level 2
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
Find the middle country(ies) in the countries list
Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
n = len(ages)
mid = n // 2
median = (ages[mid] + ages[~mid] / 2)
print("La media es:", median)
print(ages)

min_age = min(ages)
max_age = max(ages)
print("Edad minima: ", min_age)
print("Edad maxima: ", max_age)

ages.append(min_age)
ages.append(max_age)

promedio = sum(ages) / len(ages)
print(promedio)

rango = max(ages) - min(ages)
print(rango)

comparacion = abs(min_age - promedio) and abs(max_age - promedio)
print(comparacion)

n = len(countries_list) 
mid = n // 2 
if n % 2 == 0: 
    middle = countries[mid-1:mid+1]
else: 
    middle = [countries[mid]]
print("País(es) del medio:", middle)

n = len(countries_list) 
mid = (n + 1) // 2

first_half = countries[:mid] 
second_half = countries[mid:] 
print("Primera mitad:", first_half) 
print("Segunda mitad:", second_half)

first, second, third, *scandic_countries = countries_list
print("Primer país:", first) 
print("Segundo país:", second) 
print("Tercer país:", third) 
print("Scandic countries:", scandic_countries)
