# Numython R&D
# static_failure.py
import numpy as np
from .stress_analysis import *

def seqv(sxx,syy,sxy):
    """
    Von Mises equivalent stress
    """
    return np.sqrt(sxx**2 - sxx*syy + syy**2 + 3*sxy**2)

def sf_vonmises(sxx,syy,sxy,Sy):
    """
    Get safety factor (n) using Von Mises criteria
    """
    return Sy/seqv(sxx,syy,sxy)
    
def sf_tresca(sxx,syy,sxy,Sy):
    """
    Get safety factor (n) using Tresca criteria
    """
    sA, sB = principal_stresses(sxx,syy,sxy)
    sF = 0 # third principal stress
    ord_ps = np.sort([sA,sB,sF])[::-1]
    s1,s2,s3 = ord_ps
    return Sy/(s1 - s3)
    
