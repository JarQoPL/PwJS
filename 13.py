cena = float(input("wprowadź cenę samochodu:         "))
prowizja =1450
podatek = round((cena*0.19),2)
oplataRejestracyjna = round((cena*0.005),2)
dostawa = 1200
print("\nCena auta bez opłat:		",round((cena),2))
print("Podatek 19% wynosi:              ",podatek,)
print("Opłata rejestracyjna 0,5% wynosi: ",oplataRejestracyjna,)
print("Prowizja:                        ",prowizja,)
print("Dostawa:                         ",dostawa,)
print("\ncena samochodu razem:           ",round((cena+podatek+oplataRejestracyjna+dostawa+prowizja),2),"zł")
input("\n\nAby zakończyć wciśnij dwa razy Enter")
