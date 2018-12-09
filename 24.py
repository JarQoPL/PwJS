import random
slowa=("python","gdansk","dlaczego","gdynia","wsb")
word = random.choice(slowa)
print(word)
poprawnie = word;
print(
"""
		Witaj w grze 'Wygenerowane slowo'!
	Uporządkuj litery, aby odtworzyć prawidłowe słowo.
\n(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)\n
""")
print("Wygenerowane slowo ma liter:", len(poprawnie))
pomie=""
for x in range(0, 5):
	zgaduj = input("\nEkstra litera! Sprawdz czy slowo ja zawiera: ")
	if poprawnie.count(zgaduj)>0:
		print("tak")
	else:
		print("nie")
zgaduj = input("\nTwoja odpowiedź: ")
ktoraProba = 0
superWynik = 0
while zgaduj != poprawnie and zgaduj != "":
	print("Niestety, to nie to słowo.")
	ktoraProba += 1
	zgaduj = input("Twoja odpowiedź: ")
	if zgaduj == poprawnie:
		print("\nZgadza się! Zgadłeś!\n")
	else:
		if ktoraProba >= 3:
			print("\npierwsza litera to: " , poprawnie[0])
			print("ostatnia litera to: " , poprawnie[len(poprawnie)-1],"\n")
if ktoraProba < 3:
	superWynik += 1
	print("\n		Gratulacje!!! Udało Ci sie! Uzyskałeś wynik punktowy: ", superWynik)
print("....dziękuję za udział w grze.")
print("\n\n\nAby zakończyć wciśnij dwa razy enter")
