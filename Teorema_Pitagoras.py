import os 

def conversor(func):    
    def wrapper():
        try:
            menu_unidades = """ 
                ¿Que tipo de unidad de medida usaras?

                1 -> milimetros
                2 -> centimetros
                3 -> metros
                4 -> pulgadas 
                
                Escribe el número del tipo de medida: """
            unidad_medida = int(input(menu_unidades))
            if unidad_medida > 4:
                raise ValueError('No se puede ingresar un tipo de unidad inexistente')
        except ValueError as ve:
            print(ve)
            return False
            
        if unidad_medida == 1:
            unidad = 'Milimetros'
        elif unidad_medida == 2:
            unidad = 'Centimetros'
        elif unidad_medida == 3:
            unidad = 'Metros'
        elif unidad_medida == 4:
            unidad = 'Pulgadas'

        try:
            menu1 = """ 
                ¡Recuerda muy bien los nombres de los lados del triangulo!

                1 -> Hipotenusa
                2 -> Cateto Opuesto
                3 -> Cateto Adyacente 
                
                Escribe el número del primer tipo de lado que tienes: """
            opcion1 = int(input(menu1))
            if opcion1 > 3:
                raise ValueError('No existe la opción que escribiste')
        except ValueError as ve:
            print(ve)
            return False

        print('')

        try:
            menu_long1 = """Escribe la longitud del primer lado: """
            longitud1 = float(input(menu_long1))
        except ValueError:
            print('No se puede agregar la longitud de manera alfabetica, escribela de manera numerica')
            return False

        try:
            menu2 = """
                1 -> Hipotenusa
                2 -> Cateto Opuesto
                3 -> Cateto Adyacente 
                
                Escribe el número del segundo tipo de lado que tienes: """
            opcion2 = int(input(menu2))
            if opcion2 > 3:
                raise ValueError('No existe la opción que escribiste')
        except ValueError as ve:
            print(ve)
            return False

        print('')

        try:
            menu_long2 = """Escribe la longitud del segundo lado: """
            longitud2 = float(input(menu_long2))
        except ValueError:
            print('No se puede agregar la longitud de manera alfabetica, escribela de manera numerica')
            return False

        func(opcion1, opcion2, longitud1, longitud2, unidad)
    
    return wrapper

@conversor
def conversion(lado1, lado2, long1, long2, unidad):
    if lado1 == 1 and lado2 == 2 or lado1 == 2 and lado2 == 1:
        respuesta = (long1**2 - long2**2)**0.5
        respuesta = round(respuesta, 4)
        print('')
        print('*' * 100)
        print('')
        print(f'Tu Cateto Adyacente tiene {respuesta} {unidad}')
    elif lado1 == 1 and lado2 == 3 or lado1 == 3 and lado2 == 1:
        respuesta = (long1**2 - long2**2)**0.5
        respuesta = round(respuesta, 4)
        print('')
        print('*' * 100)
        print('')
        print(f'Tu Cateto Opuesto tiene {respuesta} {unidad}')
    elif lado1 == 2 and lado2 == 3 or lado1 == 3 and lado2 == 2:
        respuesta = (long1**2 + long2 **2)**0.5
        respuesta = round(respuesta, 4)
        print('')
        print('*' * 100)
        print('')
        print(f'Tu Hipotenusa tiene {respuesta} {unidad}')
    

def run():
    print('')
    print('¡Hola! Con este programa podras calcular el teorema de pitagoras de un triangulo Rectangulo')
    print('')
    print('*' * 100)
    conversion()
    


if __name__ == '__main__':
    os.system('cls')
    run()

