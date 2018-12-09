import numpy as np
import matplotlib.pyplot as plt
print("rysujemy fnkcję y=ax+b")
liczba_a=int(input ("\nPodaj a: "))
liczba_b=int(input ("Podaj b: "))
x=np.arange(-10,10,1)
y=liczba_a*x+liczba_b
print("\nfunkcja ma postać y =",liczba_a,"x +",liczba_b)
plt.plot(x,y)
plt.show()
print("\n\n\nAby zakończyć wciśnij Enter")
