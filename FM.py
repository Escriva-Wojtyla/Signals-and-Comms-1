import numpy as np
import matplotlib.pyplot as plt

fs = 10000
t = np.linespace(0, 0.01, int(fs*0.01))

a_c = 2
a_m = 2
myu = 0.25
f_c = 10
f_m = 1


carrier = a_c * np.cos(20*np.pi*t)
message = a_m * np.cos(2*np.pi*t)
mod = 1 +  myu * message
mudulated = carrier * mod

plt.figure(figsize=(10,6))
plt.plot(t, carrier, label="Cariier Signal")
plt.plot(t, message, "---", alpha=0.4, label="Message signal")
plt.plot(t, modulated, ":", alpha=0.5, label="AM signal")

plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("AM signal)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


