import csv
import unittest

class orderDataPrefixSubList(object):
#esta clase ordena la lista de prefijos para poder hacer mejor busquedas
    def _get_DataPrefix(self):
        listaOrdenada = []
        #leemos el archivo de prefijos esto tambien puede ser traidos desde
        #una BD siempre que los dejemos todos en una lista todo funciona
        with open('prefix.csv') as dataPrefix:
            data = csv.reader(dataPrefix)
            for reg in data:
                listaOrdenada.append(reg)
            dataPrefix.close()
        listaOrdenada.sort()
        return listaOrdenada

    def _get_DataInOrderSubList(self, listaOrdenada):
        nuevaLista = []
        cantidad = len(listaOrdenada) - 1
        ListaAux = []
        num = 0
    #creamos una lista con 9 elementos, uno para posible inicio de un profijo
        for x in range(1, 10):
            while ((int(listaOrdenada[num][0][0:1]) == x) and (cantidad > num)):
                ListaAux.append(listaOrdenada[num])
                num = num + 1
            nuevaLista.append(ListaAux)
            ListaAux = []
        return nuevaLista

    def _get_MicroSubList(self, nuevaLista):
        #maximo 11 digitos un prefijo que asistencia USA
        #creamos sub listas por cada digito segun la cantidad de
        #digitos tiene cada prefijo a buscar, y creamos una lista madre
        ListaParaBusqueda = []
        #print(len(nuevaLista))
        for z in range(len(nuevaLista)):
            subLista = nuevaLista[z]
            subLista1 = []
            subLista2 = []
            subLista3 = []
            subLista4 = []
            subLista5 = []
            subLista6 = []
            subLista7 = []
            subLista8 = []
            subLista9 = []
            subLista10 = []
            subLista11 = []
            for n in range(len(subLista)):
                if len(subLista[n][0]) == 1:
                    subLista1.append(subLista[n])
                elif len(subLista[n][0]) == 2:
                    subLista2.append(subLista[n])
                elif len(subLista[n][0]) == 3:
                    subLista3.append(subLista[n])
                elif len(subLista[n][0]) == 4:
                    subLista4.append(subLista[n])
                elif len(subLista[n][0]) == 5:
                    subLista5.append(subLista[n])
                elif len(subLista[n][0]) == 6:
                    subLista6.append(subLista[n])
                elif len(subLista[n][0]) == 7:
                    subLista7.append(subLista[n])
                elif len(subLista[n][0]) == 8:
                    subLista8.append(subLista[n])
                elif len(subLista[n][0]) == 9:
                    subLista9.append(subLista[n])
                elif len(subLista[n][0]) == 10:
                    subLista10.append(subLista[n])
                elif len(subLista[n][0]) == 11:
                    subLista11.append(subLista[n])
                else:
                    pass
            ListaParaBusqueda.append([subLista1, subLista2, subLista3,
                                       subLista4, subLista5, subLista6,
                                       subLista7, subLista8, subLista9,
                                       subLista10, subLista11])
        return ListaParaBusqueda

    def get_List(self):
        listaOrdenada = self._get_DataPrefix()
        nuevaLista = self._get_DataInOrderSubList(listaOrdenada)
        ListaParaBusqueda = self._get_MicroSubList(nuevaLista)
        return ListaParaBusqueda


class findPrefix(orderDataPrefixSubList):

    def __init__(self):
        # Realizamos la busqueda entre ambas listas por medio arboles
        # Numeros a probar en la busqueda
#        listCall = [132545684, 998221222, 5411425, 55554323, 54221321354,
 #                   34654321, 5411111122, 909999999, 1243234543, 6543212343]

        listCall = self._get_DBnumberCalls()
        ListaParaBusqueda = orderDataPrefixSubList.get_List(self)

        self.result = []
        tt = len(listCall)
        for call in range(tt):
            callbis = listCall[call]
            self.result.append(self._get_PrefixData(callbis, ListaParaBusqueda))

    def _get_DBnumberCalls(self):
        listaNumbers = []
        #leemos el archivo de prefijos esto tambien puede ser traidos desde
        #una BD siempre que los dejemos todos en una lista todo funciona
        with open('millon.csv') as dataPrefix:
            data = csv.reader(dataPrefix)
            for reg in data:
                listaNumbers.append(reg)
            dataPrefix.close()
        return listaNumbers

    def _get_PrefixData(self, callbis, ListaParaBusqueda):
        coincide = []
        encontro = False
        puntero = 1
        callbis = callbis[0]
        #busca solo el primer digito para filtrar la lista madre
        subListaMadre = ListaParaBusqueda[int(callbis[0]) - 1]
        index = 10
        while (not(encontro)) and (index >= 0):
            final = len(subListaMadre[index]) - 1
            while (puntero <= final) and (not(encontro)):
                mitad = int((puntero + final) // 2)
                if (subListaMadre[index] != []):
                    if (callbis.startswith(subListaMadre[index][mitad][0])):
                        coincide = subListaMadre[index][mitad]
                        encontro = True
                    elif (callbis[0:len(subListaMadre[index][mitad][0])] <
                                                subListaMadre[index][mitad][0]):
                        final = mitad - 1
                    else:
                        puntero = mitad + 1
                # Caso especial para el 0
                if (not(encontro)):
                    if (callbis.startswith(subListaMadre[index][0][0])):
                        coincide = subListaMadre[index][0]
                        encontro = True
            index = index - 1
            puntero = 1
        # caso especial del 1 solo de USA
        if (not(encontro)):
            try:
                if (callbis.startswith(subListaMadre[0][0][0])):
                    coincide = subListaMadre[0][0]
                    encontro = True
            except:
                coincide = "numero no existe en los prefijos"
        return coincide
"""
def main():
    datos = findPrefix()
    print(datos.result)

if __name__ == "__main__":
    main()
"""
class TestPythonSoftware(unittest.TestCase):

    def test_should_return_python_when_number_is_3(self):
        datos = findPrefix()
        cant=len(datos.result)
        self.assertEqual(1000000, cant)

if __name__ == '__main__':
    unittest.main()

