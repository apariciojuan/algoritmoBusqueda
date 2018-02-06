import random
import csv
# Sirve para generar un cvs con numeros aliatorios de hasta 11 digitos
with open('10millones.csv', 'w', newline='') as dataPrefix:
    data = csv.writer(dataPrefix, delimiter=' ',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    # Limita cantidad de numeros aca hay 10 millones
    for x in range(10000000):
        aliatorio = random.randrange(0, 10000000000)
        data.writerow([aliatorio])


