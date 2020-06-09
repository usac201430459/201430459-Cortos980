#Se crea una funcion que compruebe si el numero es par o impar. La salida de la funcion sera la operacion correspondiente a las reglas de la secuencia de Collatz
def prueba_par(num):                #La funcion tiene como parametro de entrada cualquier numero n
    if num%2 == 0:                  #Se usa el residuo para saber si el numero es par
        salida = int(num/2)         #Se aplica la operacion correspondiente. El numero que se convierte a entero para presentar mejor la informacion.
    else:                           #El else es para los numeros impares
        salida = int(num*3+1)       #Se aplica la operacion correspondiente. El numero que se convierte a entero para presentar mejor la informacion.

    return(salida)                  #Se devuelve el numero luego de haber sido operado


#Se crea una funcion que determine la secuencia de Collatz a partir de un numero cualquiera. La salida de esta funcion es una lista.
def collatz(numero):                    #La funcion tienen como parametro el numero con el que inicia la secuencia
    salida = []                         #Se crea una lista en blanco donde se guardara la secuencia de collatz que se genara
    salida.append(numero)               #Se agrega el valor del numero inicial.
    while numero > 1:                   #Se usa un ciclo while que comprueba que el numero (que se esta reescribiendo constantemente) es mayor a uno, esto por las condiciones de la secuencia de collatz
        numero = prueba_par(numero)     #Se hace uso de la funcion creada anteriormente y el valor que devuelve la funcion se utiliza para reescribir la variable numero.
        salida.append(numero)           #Se agrega a la lista cada valor obtenido con la funcion
    
    return(salida)


terminacion_carnet = 459    #Se crea una variable para la terminacion del carnet. Mi carnet es 201430459
inicio = 2                  #Se crea una variable con el valor de inicio de las secuencias

secuencias=[]                   #Se crea una lista vacia donde se almaenaran todas las secuencias que se generaron en el rango

for i in range(inicio,terminacion_carnet+1): #Se hace un ciclo for que recorra todos los valores definidos en el rango. Se suma uno para que pueda alcanzar el ultimo valor deseado (459)
    secuencias.append(collatz(i))              #Se agrega a la lista las series generadas por cada numero del rango


archivo = open('collatz.txt','w')   #Se abre/crea el archivo donde se va a guardar el resultado. Se usa 'w' para sobreescribir el archivo
for i in secuencias:                #Se usa un ciclo for recorrer las secuencias generadas.
    archivo.write(str(i)+'\n')      #Se agrega al archivo las secuencias generadas. Se usa un salto de linea ('\n') para cumplir con el formato establecido.

archivo.close()                     #Se cierra el archivo
