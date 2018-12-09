import numpy as np
import matplotlib.pyplot as plt

liczba_a=int(input ("Podaj a: "))
xr=np.arange(-10,10,0.5)
x=[i for i in xr if i<=0]
x1=[i for i in xr if i>=0]
y=[(i/(-3))+liczba_a for i in xr if i<=0]
y1=[(i*i)/3 for i in xr if i>=0]
plt.xlabel('Nazwa osi X')
plt.ylabel('Nazwa osi Y')
plt.title('Tytuł Wykresu ')
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()
