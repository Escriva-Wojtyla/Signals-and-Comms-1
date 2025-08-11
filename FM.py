import numpy as np
import matplotlib.pyplot as plt

fs = 100000
t = np.linspace(0, 1, int(fs*1))

f_c = 10  # Carrier frequency

# Carrier signal
carrier = np.cos(2 * np.pi * t * f_c)

# Two FM-modulated signals
message = np.cos(2 * np.pi * t * f_c + 6 * np.pi * t * t)  # Quadratic phase term
message_2 = np.cos(2 * np.pi * t * f_c + 6 * np.sin(2 * np.pi * t))  # Sinusoidal phase term

fig, axes = plt.subplots(4, 1, figsize=(10, 10))

# Graph 1: Carrier
axes[0].plot(t, carrier, color='darkblue', label="Carrier Signal")
axes[0].set_xlabel("Time(s)")
axes[0].set_ylabel("Amplitude")
axes[0].set_title("Carrier Signal (for FM1)")
axes[0].legend()
axes[0].grid(True)

# Graph 2: FM signal 1
axes[1].plot(t, message, color='darkgreen', label="FM signal 1")
axes[1].set_xlabel("Time(s)")
axes[1].set_ylabel("Amplitude")
axes[1].set_title("FM signal 1")
axes[1].legend()
axes[1].grid(True)

# Graph 3: Carrier
axes[2].plot(t, carrier, color='darkblue', label="Carrier Signal")
axes[2].set_xlabel("Time(s)")
axes[2].set_ylabel("Amplitude")
axes[2].set_title("Carrier Signal (for FM2)")
axes[2].legend()
axes[2].grid(True)

# Graph 4: FM signal 2
axes[3].plot(t, message_2, color='darkred', label="FM signal 2")
axes[3].set_xlabel("Time(s)")
axes[3].set_ylabel("Amplitude")
axes[3].set_title("FM signal 2")
axes[3].legend()
axes[3].grid(True)

plt.tight_layout()
plt.show()


