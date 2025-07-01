import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from Basic_Fourier_analysis import Fourier_Analysis

# Time array over two periods
time = np.linspace(0, 2*np.pi, 1000)

# Define function
def x_of_t(t):
    return signal.square(2* np.pi * t / 1.5, duty=2/3)

# Create object
fa = Fourier_Analysis(x_of_t, 1.5, 60)

# Approximate function
approx = fa.series(time)
Contribute_harmonics = fa.harmonics_contribution()
print(Contribute_harmonics)

# Plot original vs approximation
plt.plot(time, x_of_t(time), label='Original Signal', linestyle='--')
plt.plot(time, approx, label='Fourier Approximation')
plt.legend()
plt.title("Fourier Series Approximation")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.grid(True)
plt.show()

