import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
# Function to calculate the derivative of the pendulum's motion
def pendulum(y, t, L, mass, damping):
    theta, omega = y
    dydt = [omega, -(g / L) * np.sin(theta) - damping * omega]
    return dydt
# Simulate and plot the pendulum for different variations
def simulate_pendulum(lengths, masses, initial_positions, damping):
    for L in lengths:
        for m in masses:
            for theta_0 in initial_positions:
                # Initial conditions
                y0 = [theta_0, 0.0]
                # Time points
                t = np.linspace(0, 10, 1000)
                
                # Solve the ODE for the pendulum
                sol = odeint(pendulum, y0, t, args=(L, m, damping))
                
                # Extract theta values from the solution
                theta = sol[:, 0]
                
                # Plot the pendulum's motion
                plt.figure()
                plt.plot(t, theta)
                plt.xlabel('Time (s)')
                plt.ylabel('Angle (radians)')
                plt.title(f'Pendulum (L={L}m, m={m}kg, θ0={theta_0}rad, damping={damping})')
                plt.grid()
                plt.show()

# Define the variations
lengths = [1.0, 1.5, 2.0]  # Lengths of the pendulum (meters)
masses = [0.1, 0.2, 0.3]    # Masses of the pendulum's bob (kilograms)
initial_positions = [0.1, 0.5, 1.0]  # Initial positions (radians)
damping = 0.1  # Damping coefficient (proportional to damping force)

# Simulate and plot the pendulum with variations
simulate_pendulum(lengths, masses, initial_positions, damping)