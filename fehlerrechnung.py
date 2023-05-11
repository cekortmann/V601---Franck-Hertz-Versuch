import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  

def p(T):
    return 5.5*10**7*np.exp(-6876/T)

def w(p): 
    return 0.0029/p

print('Dampfdruck')
print(p(297.35))
print(p(413.35))
print(p(434.05))
print(p(435.25))
print(p(447.95))
print(p(449.35))
print(' ')
print('mittlere Weglänge')
print(w(p(297.35)))
print(w(p(413.35)))
print(w(p(434.05)))
print(w(p(435.25)))
print(w(p(447.95)))
print(w(p(449.35)))