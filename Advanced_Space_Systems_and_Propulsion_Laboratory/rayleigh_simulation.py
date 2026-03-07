from LightPipes import *
import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
wavelength = 1e-3  # mm (1 um)
size = 2500        # Bumped up to fit the 1800mm expanded beam
N = 2048           # Grid size
num_mirrors = 1    # Set to 1 so we can test the first bounce against the math
distance_per_segment = 100000000  # 100 km
aperture_radius = 50.0            # mm
tilt_angle = 0 

# 1. Initialize field
Field = Begin(size, wavelength, N)

# 2. Apodization (Gaussian)
X = np.linspace(-size/2, size/2, N)
Y = np.linspace(-size/2, size/2, N)
XX, YY = np.meshgrid(X, Y)
sigma = aperture_radius / 2
apod = np.exp(-(XX**2 + YY**2) / (2 * sigma**2))
Field.field *= apod

# Measure initial power AFTER apodization
powi = Power(Field)

# 3. Propagate (Testing just ONE 100km leg to match the math)
for n in range(num_mirrors):
    # Propagate to next mirror
    Field = Forvard(distance_per_segment, Field)
    # Apply mirror aperture
    Field = CircAperture(aperture_radius, 0, 0, Field)

# 4. Visualize and Calculate Simulated Efficiency
I = Intensity(0, Field)
powf = Power(Field)
perc = (powf / powi) * 100

plt.imshow(I, extent=[-size/2, size/2, -size/2, size/2], cmap='viridis')
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')
plt.title('Intensity After First Mirror')
plt.colorbar()
plt.show()

print(f"SIMULATED Efficiency: {perc:.4f}%")

# 5. Theoretical Rayleigh Math
w0 = sigma * np.sqrt(2) 
zR = (np.pi * w0**2) / wavelength
w_z = w0 * np.sqrt(1 + (distance_per_segment / zR)**2)
theoretical_transmission = 1 - np.exp(-2 * (aperture_radius / w_z)**2)
z_perc = theoretical_transmission * 100

print(f"THEORETICAL Efficiency: {z_perc:.4f}%")
