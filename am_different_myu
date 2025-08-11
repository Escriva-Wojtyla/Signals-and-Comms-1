import numpy as np
import matplotlib.pyplot as plt

fs = 100000
t = np.linspace(0, 1, int(fs*1))

a_c = 2
a_m = 2
f_c = 10
f_m = 1

# Values of μ to test
myu_values = [0.5, 1.0]

fig, axes = plt.subplots(len(myu_values), 1, figsize=(10, 8))

for i, myu in enumerate(myu_values):
    carrier = a_c * np.cos(2 * np.pi * f_c * t)
    message = a_m * np.cos(2 * np.pi * f_m * t)
    mod = 1 + myu * message
    modulated = carrier * mod

    # Plot with your preferred color scheme
    axes[i].plot(t, carrier, color='blue', label="Carrier Signal")
    axes[i].plot(t, message, "--", color='green', alpha=0.7, label="Message signal")
    axes[i].plot(t, modulated, color='green', alpha=0.7, label="AM signal")

    axes[i].set_xlabel("Time(s)")
    axes[i].set_ylabel("Amplitude")
    axes[i].set_title(f"AM signal (μ = {myu})")
    axes[i].legend()
    axes[i].grid(True)

plt.tight_layout()
plt.show()
