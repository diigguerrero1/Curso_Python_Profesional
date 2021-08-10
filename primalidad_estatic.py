def es_primo(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

def solicitud():
    solicitud = """Ingresa un número: """
    solicitud = input(solicitud)
    return int(solicitud)

def run():
    if es_primo(solicitud()) == True:
        print('Es un número primo')
    else:
        print('No es un número primo')

if __name__ == '__main__':
    run()