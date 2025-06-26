import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

time = np.linspace(0, 2*np.pi, 1000)

def FST(start, stop):
     
      Fourier_series = 0
      
      for i in range(start, stop):
        sum = ((2/np.pi*i-1) * np.sin((4/3*np.pi*i-1)*time)) + ((2/np.pi*i) * np.sin((4/3*np.pi*i)*time))
        Fourier_series += sum

      plt.plot(Fourier_series)
      plt.title("Generated plots")
      plt.xlabel("Time(s)")
      plt.ylabel("y(t)")
      plt.grid(True)
      plt.legend()
      plt.show()


series1 = FST(1, 2)
series2 = FST(1, 5)
series3 = FST(1, 10)






    













