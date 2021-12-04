"""
def respuesta (nombre, edad) : 
    print('Tu nombre es ' + nombre + ' y tu edad es ' , edad , ' años')

nombre = input('Introduce tu nombre: ')
edad = int(input('Introduce tu edad: '))

respuesta(nombre, edad)

def cambiarString (sentencia, palabra1, palabra2) : 
    print('La frase original era: ' + sentencia + '' + ' y la nueva frase es: ' + sentencia.replace(palabra1, palabra2))


sentencia = input('Introduce tu frase: ')
palabra1 = input('Introduce la palabra a cambiar: ')
palabra2 = input('Introduce la palabra nueva a mostrar: ')

cambiarString(sentencia, palabra1, palabra2)


def numerosParImpar(num):
    if num%2 == 0:
        print('El num es par')
    else:
        print('el num es impar')

num = int(input('Ingrese un numero: '))

numerosParImpar(num)


mydict = {
    'name': 'Daniel',
    'age': 30,
}

for value in mydict:
    print(mydict[value])
"""

def calculadoraBasica(num1, num2, operador):
    if operador == '+':
        return num1+num2
    elif operador == '-':
        return num1-num2
    elif operador == '*':
        return num1*num2
    elif operador == '/':
        return num1/num2
    else:
        return 'No hay operacion incluida para ese operador introducido...'

num1 = int(input('Introduzca primer numero: '))
num2 = int(input('Introduzca segundo numero: '))
operador = input('Introduzca operador: ')

print('El resultado retornado es: ', calculadoraBasica(num1, num2, operador))