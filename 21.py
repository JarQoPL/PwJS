import random

cyfra1 = int(input("podaj początkową liczbę:	"))
cyfra2 = int(input("podaj końcową liczbę:		"))
cyfra3 = int(input("podaj odstęp między liczbami:	"))
print("\nWyselekcjonowane liczby to:")
for suma in range(cyfra1,cyfra2,cyfra3):
	print (suma)
input("\n\nAby zakończyć wciśnij dwa razy Enter")
