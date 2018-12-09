import random
slowa = ("python","gdańsk","dlaczego","gdynia","wsb")
word = random.choice(slowa)
print(word)
poprawnie = word
pomie =""
while word:
	position = random.randrange(len(word))
	pomie += word[position]
	word = word[:position] + word[(position + 1):]
	
#print (pomie)
print (
"""
		Witaj w grze 'Wymieszane litery'!  
	Uporządkuj litery, aby odtworzyć prawidłowe słowo.
	\n(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)\n
""")
print("Zgadnij, jakie to słowo:", pomie)
i=-1
punkty = len(poprawnie)
zgaduj = input("\nTwoja odpowiedź: ")
while zgaduj != poprawnie and zgaduj != "":
	print("Niestety, to nie to słowo.")
	print("Podpowiedź pierwszych liter wyrazu- ", poprawnie[i+1])
	i+=1
	punkty -=1
	zgaduj = input("Twoja odpowiedź: ")

if zgaduj == poprawnie:
	print("\n		Zgadza się! Zgadłeś!\n",)
	print("Punkty dodatkowe")
	print(punkty)
print(".....dziękuję za udział w grze.")

print("\n\n\nAby zakończyć wciśnij dwa razy enter")
