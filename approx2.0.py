

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy import signal


#The class is a blueprint for the object

class Fourier_Analysis:

    #This init method constructs the object
    
    def __init__(self, X_of_t, fundamental_period, frequency_multiple_N):

        #The first error, after i have created the attributes here, i did not assign values to my attributes.

        time = np.linspace(0, 2*np.pi, 1000)
        self.X_of_t
        self.fundamental_period
        self.frequency_multiple_N
        omega = 2*np.pi*frequency_multiple_N
       
        #These methods construct and calculate the coefficiencts
        # Now all these methods are with in the constructor and are therefore not accesible outside the scope of the constructor.
        
        def construct_a_n(self, t, n):
            return X_of_t(t)*np.cos((n*omega*t)/fundamental_period)
        
        def construct_b_n(self, t, n):
            return X_of_t(t)*np.sin((n*omega*t)/fundamental_period)
        
        def coeff_a_n(self, n):
            result, error = quad(construct_a_n, 0, fundamental_period, args=(n,))
            return result * (1/fundamental_period)
        
        def coeff_b_n(self, n):
            result, error  = quad(construct_b_n, 0, fundamental_period, args=(n,))
            return result * (1/fundamental_period)
        
        def a_0(self):
            return quad(X_of_t, 0, fundamental_period)
        
        #here, there are some logical errors, the series sum has not been initialize, the functions are being treated like variales and the return function isin the loop, it itrates one as a result.
        
        def series(self, time, n):
            for n in range(frequency_multiple_N):
                series_sum += a_0/2 + coeff_a_n*np.cos((2*np.pi*n*time)/fundamental_period) + coeff_b_n*np.sin((2*np.pi*n*time)/fundamental_period)
                return series_sum
            















        
