#NúMERO UNO
segundos = int(input('Escriba la cantidad de segundos: '))

días = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60 )
segundos = segundos % (60 * 60)
minutos = segundos // 60
segundos = segundos // 60

print('Dias: {} - Horas:{} - Minutos: {} - Segundos: {}'.format(días, horas, minutos, segundos))


#NúMERO DOS

def triangulo (x) :
    for i in range(0, x, 1) :
        for j in range (0, i+1, 1) :
            print ("*", end="")
        print ("")
    print (" \n") 

    for i in range(x, 0, -1) :
        for j in range (0, i, 1) :
            print ("*", end="")
        print ("")
    print (" \n") 
    
    for i in range(x, -1, -1) :
         for j in range (i) :
            print (" " , end="")
         for k in range(i, x) :
            print ("*", end="")
         print("")
    print (" \n")     

    for i in range(x-1, -1, -1) :
        for j in range (x - i - 1) :
            print (" " , end="")
        for k in range(i + 1) :
            print ("*", end="")
        print("")

x=int (input ("Introduce un numero: "))
triangulo (x)

#NúMERO TRES

from datetime import date
from datetime import datetime

def calcular_edad_agnios(fecha_nacimiento) :
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado

fecha_nacimiento_juan = date(1977, 7, 12)
edad = calcular_edad_agnios(fecha_nacimiento_juan)

print(f'La edad de juan es de {edad} años.')

    
#NúMERO CUATRO

entrada = ('10', '20', '40', '5','70' )

resultado = ''.join(entrada)

print(type(resultado))
print(102040570)

#NúMERO CINCO

tupla = '[(), (), (X,), (a, b), (a, b, c, (d)]'

print(tupla)  
print(len(tupla))    

print()

tupla = [t for t in tupla if t]

print(tupla)
print(len(tupla))  


#NúMERO SEIS

import statistics
import numpy

tupla = '((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32))'
print(tupla)

mean = sum(tupla)/float(len(tupla))
print(mean)


#NúMERO SIETE

invoices = {}
collected = 0
remains = 0
more = ''
while more != 'T':
    if more == 'A':
        key = input('Introduce el número de la factura: ')
        cost = float(input('Introduce el coste de la factura: '))
        invoices[key] = cost
        remains += cost
    if more == 'P':
        key = input('Introduce el número de la factura a pagar: ')
        cost = invoices.pop(key, 0)
        collected += cost
        remains -= cost
    print('Recaudado:', collected)
    print('Pendiente de cobro: ', remains)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')


#NúMERO OCHO

import random
 
valor = ["A","2","3","4","5","6","7","J","Q","K"]
color = ["espadas","copas","oros","bastos"]
baraja = []
 
for v in valor:
    for c in color:
        carta = "{} de  {}".format(v,c)
        baraja.append(carta)
random.shuffle(baraja)
print(baraja)
 
jug = []
jug1 = []
 
jug.extend([baraja.pop(), baraja.pop()])
jug1.extend([baraja.pop(), baraja.pop()])