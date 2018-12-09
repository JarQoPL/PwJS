import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
mi, sigma=100,15
x=mi+sigma*np.random.randn(500000)
sigma**2   #średnie odchylenie standardowe
n, bins, patches=plt.hist(x,50,density=True,facecolor='green',alpha=0.75)#przezroczystosc0,75
bincenters=0.5*(bins[1:]+bins[:-1])#ustalamy granice skrajne i dzielimy przez 2
y=mlab.normpdf(bincenters,mi,sigma)
l=plt.plot(bincenters, y,'r--',linewidth=1)
plt.show()
print("\n\n\nAby zakończyć wciśnij Enter")
