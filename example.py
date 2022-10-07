import csv

fields = ['Nombre', 'Facultad', 'Año', 'Promedio']

rows = [['Carlos', 'Ingenieria', '2021', '9.0'],
        ['Daniel', 'Psicologia', '2021', '9.1'],
        ['Juliana', 'Psicologia', '2020', '9.3'],
        ['Cecilia', 'Ingenieria', '2022', '9.5'],
        ['Pepe', 'Medicina', '2022', '7.8'],
        ['Sara', 'Administracion', '2020', '9.1']]

filename = "Universidad.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
