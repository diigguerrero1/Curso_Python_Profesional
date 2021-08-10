# Reglas de Closures:
#    1. Debemos tener una nested function
#    2. La nested function debe referencia un valor de un scope superior
#    3. La función que envuelve a la nested function debe tambien retornarla

# Ejemplo del ejercicio:
# Hola 3 -> HolaHolaHola
# Diego 2 -> DiegoDiego
# Platzi 4 -> PlatziPlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes acceder texto"
        return string * n
    return repeater

def run():
    repeat_3 = make_repeater_of(3)
    print(repeat_3('Hola'))
    repeat_2 = make_repeater_of(2)
    print(repeat_2('Diego'))
    repeat_4 = make_repeater_of(4)
    print(repeat_4('Platzi'))

if __name__ == '__main__':
    run()