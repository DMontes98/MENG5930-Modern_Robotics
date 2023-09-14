import numpy as np
import matplotlib.pyplot as plt

# Given parameters
SHP = 500 # hp
altitude = 15000 # ft
prop_diameter = 6 # ft
blade_activity_factor = 100
integrated_design_lift_coefficient = 0.15
rotational_speed = 1800 # rpm
S_body = 13 # ft^2
F_scrubbing = 0.95

# Constants
R = 1716 # Gas constant, ft-lbf/(lbm*R)
gamma = 1.4 # Specific heat ratio
T_0 = 518.67 # Standard sea level temperature, R
P_0 = 2116.22 # Standard sea level pressure, lb/ft^2
rho_0 = 0.0023769 # Standard sea level density, lbm/ft^3

# Atmospheric properties at altitude
T = T_0 - 0.00356 * altitude # Temperature, R
P = P_0 * (T / T_0) ** (gamma / (R * 0.00356)) # Pressure, lb/ft^2
rho = P / (R * T) # Density, lbm/ft^3

# Velocity range
v = np.arange(50, 401, 50) # mph

# Blade parameters
blade_chord_length = 0.25 * prop_diameter
blade_length = blade_activity_factor * blade_chord_length
aspect_ratio = blade_length / blade_chord_length

# Calculate thrust, thrust HP, and efficiency for each velocity
installed_thrust = np.zeros_like(v)
thrust_hp = np.zeros_like(v)
installed_efficiency = np.zeros_like(v)

for i in range(len(v)):
    # Calculate pitch ratio and F/M
    pitch_ratio = 0.3 # Assume a constant pitch ratio of 0.3 for simplicity
    f_m = v[i] * 5280 / (rotational_speed * prop_diameter)
    # Calculate thrust coefficient and power coefficient
    thrust_coefficient = (2 * integrated_design_lift_coefficient) / (np.pi * aspect_ratio * blade_activity_factor)
    power_coefficient = (2 * np.pi * blade_activity_factor * (pitch_ratio ** 3)) / ((1 + np.sqrt(1 + (4 * ((np.pi * blade_activity_factor) ** 2) * (f_m ** 2)))) * (f_m ** 2))

fig, ax1 = plt.subplots()
ax1.plot(v, installed_thrust, 'b')
ax1.set_xlabel('Speed mph')
ax1.set_ylabel('Installed Thrust', color='b')
ax1.tick_params('y', colors= 'b')
ax2 = ax1.twinx()
ax2.plot(v, thrust_hp, 'r')
ax2.set_ylabel('Thrust HP', color='r')
ax2.tick_params('y', colors='r')
#ax3 = ax2.twinx()
#ax3.plot(v, installed_efficiency, 'c')
#ax3.set_ylabel('Installed Efficiency', color='c')
#ax3.tick_params('y', colors='c')
plt.title('Propeller Performance')
plt.show()
