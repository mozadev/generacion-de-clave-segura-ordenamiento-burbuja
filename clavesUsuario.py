usuarios=[]
claves=[]
import random
for i in range(10):
    usuarios.append("2022-0"+str(i+1))

import random# inclusión de librería


NUMEROS = list('0123456789')
MAYUSCULAS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
MINUSCULAS = list('abcdefghijklmnopqrstuvwxyz')
SIMBOLOS = list('!"#$%&/()=?¡')

#longitud = int(input('De cuantos caracteres deseas que sea tu contraseña?: '))
mayusculas = input('Deseas usar mayusculas S/N: ')
minusculas = input('Deseas usar minusculas S/N: ')
numeros = input('Deseas usar numeros S/N: ')
especiales = input('Deseas usar caracteres especiales S/N: ')

password = ''
alfabeto = []

if (numeros.upper() == 'S'):
    alfabeto = alfabeto + NUMEROS
if (mayusculas.upper() == 'S'):
    alfabeto = alfabeto + MAYUSCULAS
if (minusculas.upper() == 'S'):
    alfabeto = alfabeto + MINUSCULAS
if (especiales.upper() == 'S'):
    alfabeto = alfabeto + SIMBOLOS


for x in range(10):
    password=''
    while len(password) < 6:
        i = random.randint(0, len(alfabeto) - 1)
        letra = str(alfabeto[i])
        password = password + letra
    claves.append(password)


print(usuarios)
print(claves)

def burbuja(lista,clave):
    for i in range(len(clave) - 1):
        for j in range(len(clave) - 1 - i):
            if(clave[j] > clave[j + 1]):
                aux = clave[j + 1]
                clave[j + 1] = clave[j]
                clave[j] = aux

                aux2 = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = aux2

burbuja(usuarios,claves)
print("ordenando")
print(usuarios)
print(claves)