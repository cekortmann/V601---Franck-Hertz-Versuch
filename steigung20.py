import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray

U20, h20, U140, h140 = np.genfromtxt('steigung.txt', unpack=True, skip_header=1)
plt.plot(U20, h20, 'xr', markersize=6 , label = 'Messdaten', alpha=0.5)
plt.xlabel(r'$U_{\mathrm{A}} \, / \, \mathrm{V}$')
plt.ylabel(r'$\mathrm{\alpha}$ Steigung')
plt.legend(loc="best")                  # legend position
plt.grid(True) 
plt.savefig('build/steigung20.pdf', bbox_inches = "tight")