import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

class Fourier_Analysis:

# This constructs the object, which is a function.
    def __init__(self, X_of_t, fundamental_period, frequency_multiple_N):
        self.X_of_t = X_of_t
        self.T = fundamental_period
        self.N = frequency_multiple_N
        self.omega = 2 * np.pi / self.T

#This construct the integrand functions used to compute the coeffecients, a and b
    def construct_a_n(self, t, n):
        return self.X_of_t(t) * np.cos(n * self.omega * t)

    def construct_b_n(self, t, n):
        return self.X_of_t(t) * np.sin(n * self.omega * t)
    
#Computes the coeffecients, using the quad function from the scipy.integrate lib. 
    def coeff_a_n(self, n):
        result, _ = quad(self.construct_a_n, 0, self.T, args=(n,))
        return result * (2 / self.T)

    def coeff_b_n(self, n):
        result, _ = quad(self.construct_b_n, 0, self.T, args=(n,))
        return result * (2 / self.T)

    def a_0(self):
        result, _ = quad(self.X_of_t, 0, self.T)
        return result * (1 / self.T)

#This compute the approximation, given the Number of harmonics, self.N
    def series(self, time):
        a0 = self.a_0()
        s = (a0 / 2)
        for n in range(1, self.N + 1):
            an = self.coeff_a_n(n)
            bn = self.coeff_b_n(n)
            s +=  an * np.cos(n * self.omega * time) + bn * np.sin(n * self.omega * time)
        return s
    #added this on 1st July 2025
    def harmonics_contribution(self):
        average_power = 7.11  # Initialize
        n = 1        # Start from 1 to avoid division by zero
        # I have already calulated the average power and multiplied by .98 to get 6.96
    
        while average_power <= 6.969:
            term = (1/(np.pi*n)) * np.sin(4/3*np.pi*n)
            average_power += term
            n += 1      # Increment by 1 to go to next term

        return n -1 
    
 










    













