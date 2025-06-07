import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linearFunc(x, intercept, slope):
    y = intercept + (slope * x)
    return y


def linear_regression(x_data, y_data, x_err, y_err, print_stuff=False, plots=True, supress_err_fit=False):
    a_fit, pcov = curve_fit(linearFunc, x_data, y_data, sigma=np.sqrt(x_err**2 + y_err**2), absolute_sigma=False, full_output=False)

    inter = a_fit[0]
    slope = a_fit[1]

    perr = np.sqrt(np.diag(pcov))

    d_inter = perr[0]
    d_slope = perr[1]

    plt.errorbar(x_data, y_data, xerr=x_err, yerr=y_err, fmt='k.', capsize=2)

    yfit = inter + slope*x_data
    yfit2 = (inter+d_inter) + (slope+d_slope)*x_data
    yfit3 = (inter-d_inter) + (slope-d_slope)*x_data

    if plots is True:
        plt.plot(x_data, yfit, label=f"y={slope:.2e}+/-{d_slope:.1e}x + "
                                     f"{inter:.2e}+/-{d_inter:.1e}", color='r', linestyle='-')

        if supress_err_fit is False:
            plt.plot(x_data, yfit2, color='g', linestyle='--', label='uncertainty')
            plt.plot(x_data, yfit3, color='g', linestyle='--')

        plt.legend()

    if print_stuff is True:
        print(f'slope = {slope:.2e}, with uncertainty {d_slope:.1e}')
        print(f'intercept = {inter:.2e}, with uncertainty {d_inter:.1e}')

    return slope, d_slope, inter, d_inter
