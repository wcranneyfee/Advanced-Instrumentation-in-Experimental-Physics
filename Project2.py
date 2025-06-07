import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np


R_0 = 0.3
T_0 = 23

def linear_func(x,a):
    return R_0*(1 + a*(x-T_0))

def fit_resistance_curve(x_data, y_data):
    popt, _ = curve_fit(linear_func, x_data, y_data)
    y_fit = linear_func(x_data, *popt)

    plt.plot(x_data, y_fit, '--', color='red', label=f"alpha = {popt[0]:.3e}")


def format_csv(filepath: str, x_label: str, fig_num: int):
    plt.figure(fig_num)
    df = pd.read_csv(filepath)
    df = df.groupby(x_label)['Resistance'].agg(Resistance='mean', std='std').reset_index()

    plt.errorbar(df[x_label], df['Resistance'], capsize=3, yerr=df['std'], color='black')
    plt.scatter(df[x_label], df['Resistance'], color='black')

    plt.ylabel(r'Resistance $\Omega$')
    if x_label == "Temp":
        fit_resistance_curve(df["Temp"], df["Resistance"])
        plt.legend()
        plt.xlabel('Temperature [K]')

    else:
        plt.xlabel('Magnetic Field Strength [T]')

    filename = filepath.split('/')[1]
    plt.savefig(f"Plots/{filename}.png")

fig_num = 1
format_csv('Data/cooling_experiment', 'Temp', fig_num)
fig_num += 1
format_csv('Data/heating_experiment', 'Temp', fig_num)
fig_num += 1
format_csv('Data/TEMP_3.TXT', 'Temp', fig_num)
fig_num += 1
format_csv('Data/negative_field', 'Tesla', fig_num)
fig_num += 1
format_csv('Data/positive_field', 'Tesla', fig_num)
fig_num += 1
format_csv('Data/positive_field_2', 'Tesla', fig_num)
fig_num += 1
format_csv('Data/MAG_1.TXT', 'Tesla', fig_num)

plt.show()