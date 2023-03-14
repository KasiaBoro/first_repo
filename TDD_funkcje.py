Def przywitanie(imie, nazwisko, wiek):
	print(‘siema’, imie)
	If wiek >=18:
		print(‘Szanowny’, nazwisko)
x = input(‘ Podaj imie, nazwisko i wiek – oddziel spacja ’).split()

przywitanie(x[0], x[1], int(x[2]))
#while true:
#	pin = ‘1234’
# while True:
#	x = input(‘Wprowadz pin’)
#	if x ==pin:
#	przywitanie()
#	break
#print(‘Kolejna instrukcja’)

#x = 0
#while x < 5:
#	print(‘Jakas akcja’)
#	x +=1
