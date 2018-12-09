rachunek =float(input("wpisz kwotę rachunku:	 "))
print ("Kwota bez napiwku to:	",round((rachunek),2))# gdyby wpisano za duzo miejsc po kropce to skroci do dwoch
print("Napiwek 15% wynosi:	",round((rachunek*0.15),2))
print("Napiwek 20% wynosi:	",round((rachunek*0.20),2))
print("\n\nLub napiwki zaokrąglone do pełnych jednostek waluty-bez przecinka")
print("Napiwek 15% wynosi:	",round((rachunek*0.15),))
print("Napiwek 20% wynosi:	",round((rachunek*0.20),))
input("\n\nAby zakończyć wciśnij dwa razy Enter")
