import numpy as np
import matplotlib.pyplot as plt

fs = 1000000
t = np.linspace(0, 1, int(fs*1))

a_c = 2
a_m = 2
myu = 0.25
f_c = 10
f_m = 1


carrier = a_c * np.cos(2*np.pi*f_c*t)
message = a_m * np.cos(2*np.pi*f_m*t)
mod = 1 +  myu * message
modulated = carrier * mod

plt.figure(figsize=(10,6))
plt.plot(t, carrier, color='blue', label="Carrier Signal")     # solid blue line
plt.plot(t, message, "--", color='green', alpha=0.7, label="Message signal")  # dashed green line
plt.plot(t, modulated, ":", color='green', alpha=0.7, label="AM signal")        # dotted red line


plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("AM signal")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()








