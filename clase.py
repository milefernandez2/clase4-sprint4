
#Estructuras de control
#if condicion
#condicion es una expresión booleana que puede ser True o False
#si la condición es True se ejecuta el cuerpo del if


if 1 > 0:
    print("1 es mas grande")

#Más de una posibilidad

x=4
if x%2 == 0: #El módulo (%) es el resto de dividir a x por 2
    print(x, "es un numero par")
else: 
    print(x, "es un numero impar")

# x % n --> numeros enteros del 0 al n-1
# x % 2 --> 0 o 1
# x % 4 --> 0, 1, 2, 3


# Condiciones encadenadas elif

X=7
y=4
if x < y:
    print(x, "es menor que", y)
elif x > y:
    print(x, "es mayor que", y)
else:
    print(x, "y", y, "son iguales")

# condicion? valor1 : valor2
fruit = 'Apple'
isApple = True if fruit == 'Apple' else False
print(isApple)

#Ejemplo: (Para entender cuándo usar if, elif y else)
x=1
if x==1:
    print("x es igual a 1") #se imprime
if x!=2:
    print("x no es igual a 2") #se imprime
else:
    print("aaaa")

print("----------")

if x==1:
    print("x es igual a 1") #se imprime SÓLO esto
elif x!=2:
    print("x no es igual a 2") 
else:
    print("aaaa")

#Las condiciones pueden estar anidadas
x=7
y=7

if x==y:
    print(x, "y", y, "son iguales")
else:
    if x > y:
        print(x,"es mayor que", y)
    else:
        print(x,"es menor que", y)


#También podemos usar los operadores lógicos: (and, or, etc)

if x > 0 and x < 10:
    print(x, "esta entre 0 y 10")

#Lo de arriba es equivalente a:
if x > 0:
    if x < 10:
        print(x, "esta entre 0 y 10")

#While
n=10
while n > 0:
    print (n)
    n= n-1
print("Despeje") #Desde acá se imprime fuera del while
print(n)

#Break: corta la ejecución de un ciclo
n=10
while n > 0:
    print(n)
    if n == 2:
        print("llegué al 2")
        break
    n = n-1 #en python no existe n-- o n++ --> ponemos n = n-1 o n = n+1
print(n)

#Otra forma para no usar break(el cual no se recomienda usar, más que nada en condiciones anidadas):
n=10
continuar = True
while n > 0 and continuar:
    print(n)
    if n == 2:
        print("Llegué al 2")
        continuar = False
    n = n-1
print(n)

#For

palabra = "Argentina"

for p in palabra:
    print(p) # Imprime cada una de las letras de Argentina

for i in range(0,15):
    print(i) #Imprime números del 0 al 14

#for(let i = 0; i < 15; i++) --> equivalente de lo de recién en JavaScript

#Listas
lista = [15,15, "hola"]
for elem in lista:
    print(elem)

#Otra forma usando for con range
for i in range(0, len(lista)): #Se imprimen los lugares 0, 1 y 2
    print(lista[i])

