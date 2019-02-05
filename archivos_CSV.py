import csv
# Open csv for writing ( = create file if not exist)
doc = open("archivoW.csv", "w")

doc_csv_w = csv.writer(doc)
lista = ['Pedro', 99836]

# Writing data to CSV
doc_csv_w.writerow(lista)
# Closing CSV file
doc.close()

# Writing data to CSV example #2
doc = open("archivoW.csv", "w")

doc_csv_w = csv.writer(doc)
lista = [['Pedro', 99836], ['Uno', 1000], ['Dos', 2000], ['Tres', 4000], ['Quatro', 5000]]

# Writing data to CSV
doc_csv_w.writerow(lista)
# Closing CSV file
doc.close()

# Writing to CSV in cycle example
doc = open("archivoW.csv", "w", newline='')

doc_csv_w = csv.writer(doc)
lista = [['Pedro', 99836], ['Uno', 1000], ['Dos', 2000], ['Tres', 4000], ['Quatro', 5000]]

# Writing data to CSV
for x in lista:
    doc_csv_w.writerow(x)
# Closing CSV file
doc.close()

# Read CSV file
doc = open('archivoW.csv', 'r')

doc_csv = csv.reader(doc)

for(nombre, numero) in doc_csv:
    print(nombre, numero)

doc.close()
