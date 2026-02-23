""" Exercises: Day 8
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries """

dog = {'name':'toby', 'breed':'shihtzu', 'legs':4, 'age':9}
student_dict = {'first_name':'lucas', 'last_name':'pugliese', 'gender':'man', 'age':28, 'marital status':'married', 'skills':['programming'], 'country':'argentina', 'city':'buenos aires', 'address':'siempreviva'}
print(len(student_dict))
print(student_dict['skills'])
student_dict['skills'] = ['football']
print(student_dict['skills'])
keys = student_dict.keys()
values = student_dict.values()
print(keys)
print(values)

lista = student_dict.items()
print(lista)
student_dict.pop('age')
student_dict.values
del dog
