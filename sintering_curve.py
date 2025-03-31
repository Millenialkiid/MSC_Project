from google.colab import files
import numpy as np
import matplotlib.pyplot as plt

# Upload the file
uploaded = files.upload()

# Load data from the PZT.txt file
def load_data(filename):
    data = np.loadtxt(filename, delimiter='\t', skiprows=1)
    return data[:, 0], data[:, 1], data[:, 2]  # Time, Voltage, Current

t, v, i = load_data("Pzt.txt")

# Power calculation
power = v * i

# Material properties
density = 8000  # kg/m^3
dia = 6e-3  # m
h = 5.5e-3  # m

# Cross-sectional area
area = np.pi * (dia / 2.0) ** 2

# Electrical properties
cd = i / area  # Current density
E = v / h  # Electric field
sigma = cd / E  # Conductivity
ln_sigma = np.log(sigma)

# Volume and power per unit mass
vs = area * h
power_m = power / (vs * density)

# Inconel properties and Joule heating calculations
R_inconel = 1.31e-6  # ohm-m
density_inconel = 8113  # kg/m^3
h_inconel = 3.9e-3  # m
dia_inconel = 6.05e-3  # m

joule_inconel = (i ** 2) * R_inconel * h_inconel / (np.pi * (dia_inconel / 2.0) ** 2)
joule_inconel_m = joule_inconel / (h_inconel * np.pi * (dia_inconel / 2.0) ** 2 * density_inconel)

# Plotting
plt.figure(figsize=(12, 7.8))
plt.plot(t, power_m, label="Power per unit mass (3YSZ)")
plt.plot(t, joule_inconel_m, label="Joule heating in Inconel")

plt.xlabel("Time (seconds)")
plt.ylabel("Power per unit mass (W/kg)")
plt.title("Power per Unit Mass vs Time")
plt.legend()
plt.grid(True)

# Save and display plot
plt.savefig("FS_P_vs_time.png")
plt.show()

print("Plotting complete.")
