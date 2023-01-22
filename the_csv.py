#1. Odczytać pliku csv z zapisem poszczególnych pól

path = 'C:\\Users\\vdi-student\\Desktop\\first_repo\\rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik_csv:
    content = plik_csv.readlines()

print(type(content))
print(len(content))
print(content)
print(content[4])

dane = 'mama.tata.pies'
print(dane)
dane2 = dane.split('.')
print(dane2)

#with open('C:\\Users\\vdi-student\\Desktop\\first_repo\\rozliczenie.csv', 'r') as plik_csv: