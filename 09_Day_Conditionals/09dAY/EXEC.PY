""" Exercises: Level 1
Get user input using input(“Enter your age: ”). 
If user is 18 or older, give feedback: You are old enough to drive. 
If below 18 give feedback to wait for the missing amount of years. Output: """

age_required = 18
age = int(input("Enter your age: "))
residual = age_required - age
if age == 18 or age > 18:
    print("You are old enough to drive.")
else:
    
    print("You need", residual, "years to learn to drive.")

"""Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
Output: """

my_age = int(input("Mi edad: "))
your_age = int(input("Tu edad: "))
if my_age > your_age:
    diferencia = my_age - your_age
    if diferencia == 1:
        print("Soy mayor por 1 año")
    else:
        print("Soy mayor que tu por", diferencia, "años.")
elif your_age > my_age:
    diferencia = your_age - my_age
    if diferencia == 1:
        print("Sos mayor que yo por 1 año")
    else:
        print("Sos mayor que yo por", diferencia, "años.")
else:
    print("Tenemos la misma edad.")

"""Get two numbers from the user using input prompt. 
If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3 """

a = input("Primer numero: ")
b = input("Segundo numero: ")

if a > b:
    print("A es mayor que B")
elif b > a:
    print("A es menor que B")
else:
    print("A y B son iguales")

"""Exercises: Level 2
Write a code which gives grade to students according to theirs scores:
```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
"""

student_score = int(input("Ingrese su puntaje: ")) 
if student_score >= 90 and student_score <= 100: 
    print("Tu puntaje es de", student_score, "y sos grado A.") 
elif student_score >= 80 and student_score <= 89: 
    print("Tu puntaje es de", student_score, "y sos grado B.") 
elif student_score >= 70 and student_score <= 79: 
    print("Tu puntaje es de", student_score, "y sos grado C.") 
elif student_score >= 60 and student_score <= 69: 
    print("Tu puntaje es de", student_score, "y sos grado D.") 
elif student_score >= 0 and student_score <= 59: 
    print("Tu puntaje es de", student_score, "y sos grado F.") 
else: 
    print("Puntaje inválido. Debe estar entre 0 y 100.")

""" Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn. 
December, January or February, the season is Winter. 
March, April or May, 
the season is Spring June, July or August, the season is Summer
"""
month = input("Ingrese el mes: ")
autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']

if month in autumn:
    print("Estas en autumn!")
elif month in winter:
    print("Estas en winter!")
elif month in spring:
    print("Estas en spring!")
elif month in summer:
    print("Estas en summer!")
else:
    print("El mes ingresado no es correcto.")


"""
fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
check = input("Ingrese su fruta: ")
if check not in fruits:
    fruits.append(check)
    print(", ".join(fruits))
elif check in fruits:
    print("La fruta ya está en la lista.")
else:
    print("Boludo")
    

"""
    * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'),
* if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
* if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - 
for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
"""


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person: 
    skills = person['skills'] 
    middle_index = len(skills) // 2 
    print("La habilidad del medio es:", skills[middle_index])
if 'Python' in skills: 
    print("Sí, la persona tiene la habilidad de Python.") 
else: 
    print("No tiene la habilidad de Python.") 
if skills == ['JavaScript', 'React']: 
    print("Es un desarrollador front end.") 
elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']): 
    print("Es un desarrollador backend.")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']): 
    print("Es un desarrollador fullstack.") 
else: 
    print("Título desconocido.") else: print("El diccionario no tiene la clave 'skills'.") 
