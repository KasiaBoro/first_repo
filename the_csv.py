1.odczytac plik csv z zapisem poszczegolnych pol
path = 'C:\\Users\\vdi-student\\Desktop\\first_repo\\rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik_csv:
	content = plik_csv.readlines()
for i in range(len(content)):
	content[i] = content[i].replace('\n', '')
	content[i] = content[i].split(';')
#2. obliczenie sredniej wyplaty
total = 0
for i in range(1, len(content)):

	total += int(content)):
average = total/len(content)-1)
print('Srednia wynosi', round(average, 2), 'zlotych')
print(f'Srednia wynosi {round(average, 2)} zlotych')

#3. obliczenie liczby kobieta na macierzynskim
total = 0
for i in range(1, len(content)):
	if content[i][4] == 't' and content[i][3] == 'k':
		total +=1
print(total)