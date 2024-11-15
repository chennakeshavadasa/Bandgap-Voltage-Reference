# Importing necessary libraries
import math

# Constants
Vt = 26.38953e-3  # Thermal voltage in volts
dvbedt = -1.71313e-3  # Change in Vbe with temperature in volts per degree
dvtdt = 8.888286e-5  # Change in Vt with temperature in volts per degree
Vbe = 0.74029  # Base-emitter voltage in volts
ln8 = math.log(8)  # Natural log of 8

# Get user inputs for Itotal and Vref
Itotal_uA = float(input("Enter the total current (Itotal) in µA: ")) * 1e-6  # Convert from µA to A
Vref = float(input("Enter the desired Vref (in Volts): "))

# Set an initial guess for Ibias and define a tolerance level
Ibias = Itotal_uA / 2  # Initial guess for Ibias
tolerance = 1e-12  # Tolerance for convergence
max_iterations = 1000  # Max iterations to prevent infinite loops

# Iterative approach to find the correct Ibias
for _ in range(max_iterations):
    # Calculate R1 and R3 based on the current Ibias guess
    R1 = Vt * ln8 / Ibias
    R3 = -(R1 / ln8) * (dvbedt / dvtdt)
    
    # Calculate the contribution of Vbe/R3
    Vbe_R3 = Vbe / R3
    calculated_Itotal = Ibias + Vbe_R3  # Recalculate total current with current Ibias guess
    
    # Check if the calculated total current is within the tolerance level of desired Itotal
    if abs(calculated_Itotal - Itotal_uA) < tolerance:
        break  # Found the correct Ibias
    
    # Adjust Ibias using a simple feedback mechanism
    Ibias += (Itotal_uA - calculated_Itotal) / 2  # Adjust Ibias for next iteration

# Convert final Ibias to µA for display
Ibias_uA = Ibias * 1e6

# Calculate R10 required to achieve the desired Vref with the found Ibias
R10 = Vref / Itotal_uA  # R10 in Ohms

# Calculate R3/2
R3_half = R3 / 2

# Display results
print(f"R1 = {R1:.12f} Ohms")
print(f"R3 = {R3:.12f} Ohms")
print(f"R3 / 2 = {R3_half:.12f} Ohms")
print(f"IR3 = {Vbe_R3 * 1e6:.12f} µA")  # Display IR3 in µA
print(f"Bias current (Ibias) = {Ibias_uA:.12f} µA")
print(f"Total current (Itotal) = {calculated_Itotal * 1e6:.12f} µA")  # Display calculated Itotal in µA
print(f"R10 = {R10:.12f} Ohms to achieve Vref = {Vref} Volts")
