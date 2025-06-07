import matplotlib.pyplot as plt
import pandas as pd
from linear_regression import linear_regression
import numpy as np

r_int_fitting = pd.read_csv('Data/Solar Panel Fitting R_int.csv')
power_v_resistance = pd.read_csv('Data/Power vs Resistance.csv')

R = np.array(r_int_fitting['R']) # Resistance in ohms
V = np.array(r_int_fitting['V']) # Voltage in ohms

dR = R*0.01 # Ohms
dV = 0.1 # Volts

dI = np.sqrt((dV/R)**2 + ((V*dR)/R**2)**2) # Current Error in A

plt.figure(1)
R_int, dR_int, Vbat, dVbat = linear_regression(r_int_fitting['I '], r_int_fitting['V'], dI, dV)
plt.xlabel('Current [A]')
plt.ylabel('Voltage [V]')

R_int = abs(R_int)

x = power_v_resistance['R']+ 10 # Dummy variable that makes finding error in power easier
dR = 0.1*power_v_resistance['R']
dx = np.sqrt(dR**2 + (dR_int+10)**2)# The error is the same as that of the load resistance of the solar panel

dPdVbat = np.absolute(2*Vbat*(1/x - 10/(x**2)))
dPdx = np.absolute(Vbat**2 * (-1/(x**2) + 20/(x**3)))

dP = np.sqrt((dPdVbat * dVbat**2) + (dPdx * (dx+1))**2)

plt.figure(2)
max_power = max(power_v_resistance['P'])
max_resistance_index = power_v_resistance.idxmax()
max_resistance = power_v_resistance.iloc[max_resistance_index['P']]['R']

plt.scatter(max_resistance, max_power, color='gold', marker='*', edgecolors='black', linewidths=1, s=150,
            label=f'{max_power} mW at {max_resistance} \u03A9', zorder=1)

plt.errorbar(power_v_resistance['R'], power_v_resistance['P'], yerr=dP, linestyle='', capsize=2, zorder=0)
plt.xlabel(r" Resistance $[\Omega]$")
plt.ylabel("Power [mW]")
plt.legend()

for i in range(2):
    plt.figure(i+1)
    plt.savefig(f"Plots/Project3Fig{i+1}.png")

print(f"The max maximum power is {max_power} +/- {dP.iloc[max_resistance_index['P']]} mW and it occurs when the resistance is {max_resistance} +/- {dR_int} \u03A9.")
plt.show()