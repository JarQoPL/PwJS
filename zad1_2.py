import random

cyfra1 = int(input("podaj pierwszą liczbę:		"))
cyfra2 = int(input("podaj drugą liczbę:		"))
cyfra3 = int(input("podaj odstęp między liczbami:	"))
print("\nWyselekcjonowane liczby to:")
for i in range(cyfra1,cyfra2,cyfra3):
	print (i)
input("\n\nAby zakończyć wciśnij dwa razy Enter")
