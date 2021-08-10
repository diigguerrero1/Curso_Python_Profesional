#Local Scope corresponde al alcance de las variables dentro
#de una función:

def my_func():
    y = 5
    print(y)

my_func()

#Resultado my_func() = 5


#Global Scope corresponde al alcance de las variables dentro de todo
# el programa:

y = 5

def my_func():
    print(y)

def my_other_func():
    print(y)

my_func()
my_other_func()

#Resultado my_func() = 5
#Resultado my_other_func() = 5  


#Ejemplo 2 Global Scope:

z = 5

def my_func():
    z = 3
    print(z)

my_func()
print(z)

#Resultado my_func = 3
#Resultado z global = 5


#Ejemplo 3 Global Scope:

z = 5

def my_func():
    z = 3

    def my_other_func():
        z = 2
        print(z)

    my_other_func()

    print(z)

my_func()
print(z)

#Resultado my_func(my_other_func()) = 2
#Resultado my_func() = 3
#Resultado z global = 5