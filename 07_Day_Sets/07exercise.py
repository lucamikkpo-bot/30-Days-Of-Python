"""Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard"""

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


print(len(it_companies))
it_companies.add('Twitter')
new_companies = 'Mercado Libre', 'Uala', 'Astropay'
print(it_companies.union(new_companies))
it_companies.remove('IBM')
diferencia = it_companies.difference(new_companies)
print(diferencia)


"""Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely"""


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_B = A.union(B)

A.union(B)
A.intersection(B)
A.issubset(B)
A.isdisjoint(B)

A.update(B) 
B.update(A)
print("A:", A, "B:", B)

A.symmetric_difference(B)
del A_B

""" Exercises: Level 3
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words. """

age = [22, 19, 24, 25, 26, 24, 25, 24]

set_age = set(age)
print(type(set_age))

print(len(age))
print(len(set_age))
# set is bigger because the duplicates.

texto = 'La diferencia radica entre su mutabilidad/inmutabilidad, sobre su ordenamiento, si permite duplicados o no y su tipo.'
palabras = texto.split()
unique_words = set(texto)
print("Las palabras unicas son:", unique_words)
print(len(unique_words))
