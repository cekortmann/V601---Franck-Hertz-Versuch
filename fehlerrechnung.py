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

def mittelwert(u1, u2, u3, u4, u5, u6, u7):
    return 1/7*(u1/5+u2/5+u3/5+u4/5+u5/5+u6/5+u7/5)

u1 = ufloat(35,1)
u2 = ufloat(34,1)
u3 = ufloat(37,1)
u4 = ufloat(33,1)
u5 = ufloat(36,1)
u6 = ufloat(34,1)
u7 = ufloat(34,1)

print('Mittelwert Messung 2:', mittelwert(u1, u2, u3, u4, u5, u6, u7))

sktm = ufloat(6.94, 0.08)
def V(skt):
    return skt / sktm

print(V(35))
print(V(37))
print(V(38))

def mittelV(v1, v2, v3):
    return 1/3*(v1+v2+v3)

v1 = ufloat(4.98, 0.06)
v23 = ufloat(5.26, 0.06)
v4 = ufloat(5.41, 0.06)
print('Mittelwert V fh2', mittelV(V(37), V(38), V(42)))

def ej(E):
    return E*1.602*10**(-19)

E1 = ufloat(5.62, 0.06)
h = 6.62607*10**(-34)
def nu (E): 
    return E/h

c = 2.99792*10**8
def lambd (nu):
    return c/nu

print('lambda fh2', lambd(nu(ej(E1))))