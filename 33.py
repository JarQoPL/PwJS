import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0.0,2.0,0.01)
y=np.sin(2.0*np.pi*x)
plt.plot(x,y,'r:',linewidth=6)
plt.xlabel('Czas')
plt.ylabel('Pozycja')
plt.title('Nasz pierwszy wykres')
plt.grid(True)
plt.plot(x,y)
plt.show()
print("\n\n\nAby zakończyć wciśnij Enter")

