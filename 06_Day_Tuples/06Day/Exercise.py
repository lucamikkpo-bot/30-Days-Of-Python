""" Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members """

empty = tuple()
boys = ('Benicio', 'Mateo')
girls = ('Martina', 'Laura')
sons = boys + girls
print("I have:", len(sons))
tupleado = list(sons)
tupleado.append('Lucas')
tupleado.append('Ana')
print(tupleado)

family_members = tuple(tupleado)
print(family_members)


"""Exercises: Level 2
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_stuff_lt list
Delete the food_stuff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country"""

list(family_members)
print(family_members)

siblings = family_members[0:4]
parents = family_members[-2:]

fruits = ('Manzana', 'Naranja', 'Banana')
vegetables = ('Lechuga', 'Tomate', 'Batata')
animal_products = ('Pollo', 'Milanesa', 'Churrasco')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp[4:5])
print(food_stuff_tp[:3])
print(food_stuff_tp[6:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden') 
check_one = 'Estonia' in nordic_countries
print(check_one)
check_two = 'Iceland' in nordic_countries
print(check_two)

