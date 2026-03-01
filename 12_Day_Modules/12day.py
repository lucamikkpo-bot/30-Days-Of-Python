import random
import string

def generar_contraseña():
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for _ in range(6))
    return contraseña   
print("Tu contraseña generada es:", generar_contraseña())

def user_id_gen_by_user():
    caracteres = string.ascii_letters + string.digits
    num_caracteres = int(input("Ingrese el número de caracteres para la ID: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    
    ids_generados = []
    for _ in range(num_ids):
        id_generada = ''.join(random.choice(caracteres) for _ in range(num_caracteres))
        ids_generados.append(id_generada)
    
    return ids_generados

def rgb_color_gen():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())

def list_of_hexa_colors(n):
    import random
    hexa_colors = []
    for _ in range(n):
        color = '#'
        for _ in range(6):
            color += random.choice('0123456789abcdef')
        hexa_colors.append(color)
    return hexa_colors
print(list_of_hexa_colors(3))

def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]
print(list_of_rgb_colors(3))

def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst  
