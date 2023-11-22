import numpy as np
import math

def binom_dis(n, x, p):
    return math.comb(n, x) * (p**x) * ((1-p)**(n-x))

def Pois_dis(x, t, k):
    return np.exp(-t*k)*(np.power(k*t, x)/math.factorial(x))

def Exp_dis(x, t):
    return t*np.exp(-t * x)

