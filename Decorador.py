# Decorador sin Azucar Sintactico

def decorador(func):
    def envoltura():
        print('Esto se añade a mi función Original')
        func()
    return envoltura

def saludo():
    print('¡Hola!')

saludo = decorador(saludo) #Este es nuestro decorador sin Azucar Sintactico

saludo()


# Decorador con Azucar Sintactico

def decorador(func):
    def envoltura():
        print('Esto se añade a mi función Original')
        func()
    return envoltura

@decorador  #Este es nuestro decorador con Azucar Sintactico
def saludo():
    print('¡Hola!')

saludo()