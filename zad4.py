import random
liczba = random.randint(1,49)
for i in range(6):
	print ("Zgadujesz poraz ", i+1)
	odp = input("jaka jest liczba od 1 do 49 wylosowano ")
	
if liczba ==int(odp):
	print ("Wygrana!!!")
else:
	print("Brak wygranej")
		
