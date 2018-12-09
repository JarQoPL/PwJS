import random
liczba = random.randint(1,49)
print("Wylosowano liczbę: ",liczba)
for i in range(6):
	print ("\nZgadujesz po raz ", i+1)
	odp = input("jaka jest liczba od 1 do 49 wylosowano ")
	#print ("Podałeś: ",odp)
	if liczba ==int(odp):
		print ("\nHura!!!! ",liczba, "jest liczbą wylosowaną!! Zgadłem!!!")
		break	
	elif i==5:
		print("\nwylosowano: ",liczba)	
	if liczba > int(odp):
		print ("	No niestety ",odp," to za mała liczba")
	else:
		print("	No niestety ",odp," to za duża liczba")	
	
input("\n\nAby zakończyć wciśnij dwa razy Enter")
		
