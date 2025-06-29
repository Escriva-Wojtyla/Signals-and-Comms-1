










        
#here's how I am using it

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy import signal
from Basic_Fourier_analysis import Fourier_Analysis



time =  np.linspace(0, 2*np.pi, 1000)
function = signal.square(2*np.pi*time, duty=2/3) 




Approximation = Fourier_Analysis(function, 1.5, 10)
Approximation.construct_a_n()
Approximation.construct_b_n()
Approximation.coeff_a_n()
Approximation.coeff_b_n()
Approximation.a_0()
Approximation.series()

## This is the error I am getting









##PS C:\Users\Admin\downloads> python analysis.py
## The errors Traceback (most recent call last):



  ##/ File "C:\Users\Admin\downloads\analysis.py", line 15, in <module>
    
    
#Approximation = Fourier_Analysis(function, 1.5, 10)
                    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 #File "C:\Users\Admin\downloads\Basic_Fourier_analysis.py", line 16, in __init__
 #   self.X_of_t
#AttributeError: 'Fourier_Analysis' object has no attribute 'X_of_t'
#PS C:\Users\Admin\downloads>##

