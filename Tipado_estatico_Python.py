#Sintaxis Estatica para variables

a: int = 5
print(a)

b: str = 'Hola'
print(b)

c: bool = True
print(c)



#Sintaxis Estatica para funciones

def suma(a: int, b: int) -> int:
    return a + b

print(suma(1, 2))



#Sintaxis Estatica para funciones que termina siendo Dinamica

def suma(a: int, b: int) -> int:
    return a + b

print(suma('a', 'b'))



#Ejemplo de tipado con estructuras de Datos (Diccionarios, listas, tuplas)

from typing import Dict, List, Tuple

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45,
}

countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'peoble': '450000',
    },
    {
        'name': 'México',
        'peoble': '900000',
    },
    {
        'name': 'Colombia',
        'peoble': '50000000',
    },
]

numbers: Tuple[int, float, int] = (1, 0.5, 1)



#Podemos escribir otro ejemplo con diferente sintaxis

CoordinatesType = List[Dict[str, Tuple[int, int]]]

Coordinates: CoordinatesType = [
    {
        'coord1': (1, 2),
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1),
        'coord2': (2, 5)
    },
]


