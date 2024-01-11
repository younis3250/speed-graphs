# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:53:06 2023

@author: PMLS
"""

import numpy as np
import matplotlib.pyplot as plt

# Given parameters
m = 68.1  # mass of the object (Kg)
c = 12.5  # drag coefficient kg/s
g = 9.8   # acceleration due to gravity (m/s^2)

# Observed data
time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
observed_speeds = np.array([10.00, 16.30, 23.00, 27.50, 31.00, 35.60, 39.00, 41.50, 42.90, 45.00, 46.00, 45.50, 46.00, 49.00, 50.00])

# Polynomial models
poly2_coefficients = np.polyfit(time, observed_speeds, 2)
poly4_coefficients = np.polyfit(time, observed_speeds, 4)

# Calculate speeds using the analytical model
analytical_speeds = (g * m / c) * (1 - np.exp(-c / m * time))

# Calculate terminal velocity
terminal_velocity = g * m / c

# Plot the results
plt.plot(time, observed_speeds, label='Observed speeds', marker='o')
plt.plot(time, analytical_speeds, label='Analytical model', linestyle='--')
plt.plot(time, np.polyval(poly2_coefficients, time), label='Poly2 model', linestyle='-.')
plt.plot(time, np.polyval(poly4_coefficients, time), label='Poly4 model', linestyle=':')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.legend()
plt.show()

# Print results
print("1:", analytical_speeds)
print("2:",f"Terminal Velocity (analytical): {terminal_velocity:.2f} m/s")
print("3:",f"Terminal Velocity (poly2): {np.polyval(poly2_coefficients, time[-1]):.2f} m/s")
print("4:",f"Terminal Velocity (poly4): {np.polyval(poly4_coefficients, time[-1]):.2f} m/s")
