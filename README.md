# algoritmoBusqueda
ejemplo Busqueda

Algoritmo de Busqueda Binaria.
Funcionamiento: Procesa la base de prefijos telefonicos y genera una estructura similar a un arbol mediante listas de listas, pudiendo de esta forma realizar una busqueda binaria de cada numero telefonica al cual se llamo solo recorriendo una ves la lista de numeros llamados.

Se logro solo recorrer una ves la base de numeros llamadas en este ejemplo 1 millon,mediante busqueda binaria acortando su busqueda a unas pocas consultas por numero dentro de los prefijos.

Se deja configurado unittest el cual arroja un tiempo de prueba de 119 segundos en el equipo de prueba. Este tiempo corresponde a lectura, ordenamiento y armado de un arbol mediante listas de listas, de 63.996 prefijos, busqueda de del millon de numeros telefonicos en el arbol de prefijos, posterior armado de una lista de un millon de campos con la correspondencia de los numeros y sus correspondiente prefijo mas exacto posible.


Se adjunta:
prefix.csv arhivo con los prefijos globales mas de 60 mil prefijos telefonicos.

millon.csv archivo con los numeros de llamadas gnerado aleatoriamente.

busquedaBiClass.py aplicacion que realiza la busqueda entralazando las dos listas.

generarNumeros.py aplicacion para generar un archivo con numeros aliatorios.

NOTA: Se podria mejorar los tiempos de procesamiento realizando estos calculos mediante hilos.
