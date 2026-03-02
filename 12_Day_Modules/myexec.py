"""Write a function which generates a six digit/character random_user_id.
  print(random_user_id()) 
  '1ee33d'"""

import random 
import string 

def random_user_id(): 
    caracteres = string.ascii_lowercase + string.digits 
    iduser = ''.join(random.choice(caracteres) for _ in range(6)) 
    return iduser 
print(random_user_id()) 

"""Modify the previous task. 
Declare a function named user_id_gen_by_user. 
It doesn’t take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
"""

def user_id_gen_by_user():
    caracteres = string.ascii_lowercase + string.digits
    nCharacters = int(input("Ingrese el largo de caracteres: "))
    nIDS = int(input("Ingrese el total de IDS: "))

    ids = []

    for _ in range(nIDS):
        iduser = ''.join(random.choice(caracteres) for _ in range(nCharacters))
        ids.append(iduser)

    print("\n === Lista de IDs generados === ")
    for i, uid in enumerate(ids, start=1):
        print(f"ID {i:<3} |   {uid}")
    
user_id_gen_by_user()

"""
Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
"""

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = f"RGB ({r}, {g}, {b})"
    return rgb
print(rgb_color_gen())

"""
Exercises: Level 2
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
Write a function generate_colors which can generate any number of hexa or rgb colors.
"""

def list_of_hexa_colors(n=6): 
    colores = [] 
    for _ in range(n): 
        r = random.randint(0, 255) 
        g = random.randint(0, 255) 
        b = random.randint(0, 255)  
        color = "#{:02x}{:02x}{:02x}".format(r, g, b) 
        colores.append(color) 
    return colores
print(list_of_hexa_colors(6))

def list_of_rgb_colors():
    colors = []
    for _ in range(n):
        r = random.randint(0, 255) 
        g = random.randint(0, 255) 
        b = random.randint(0, 255) 
        colors.append((r, g, b))
    return colors
print(list_of_rgb_colors)

def generate_colors(color=type, n=6):
    colores = [] 

    if color_type == 'hexa':
        for _ in range(n): 
            r = random.randint(0, 255) 
            g = random.randint(0, 255) 
            b = random.randint(0, 255) 
            color = "#{:02x}{:02x}{:02x}".format(r, g, b) 
            colores.append(color) 
            
    elif color_type == 'rgb': 
        for _ in range(n): 
            r = random.randint(0, 255) 
            g = random.randint(0, 255) 
            b = random.randint(0, 255) 
            colores.append((r, g, b))  
    
    else: 
        raise ValueError("color_type debe ser 'hexa' o 'rgb'") 
    return colores


"""
Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
"""

def shuffle_list(lista):
    lista_copia = lista[:]
    random.shuffle(lista_copia)
    return lista_copia

def unique_random_numbers():
    return random.sample(range(10), 7)
