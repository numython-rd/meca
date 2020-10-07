# Numython R&D
import numpy as np

sxp = lambda sx,sy,sxy,theta: ((sx + sy)/2) + ((sx - sy)/2)*cos(2*theta) + sxy*sin(2*theta)
syp = lambda sx,sy,sxy,theta: ((sx + sy)/2) - ((sx - sy)/2)*cos(2*theta) - sxy*sin(2*theta)
sxyp = lambda sx,sy,sxy,theta: -( (sx - sy)/2 )*sin(2*theta) + sxy*cos(2*theta)

tp = lambda sx,sy,sxy: 0.5*np.arctan2(2*sxy, sx - sy)
tp_ = lambda sx,sy,sxy: 0.5*np.arctan( 2*sxy / ( sx - sy) ) 

smax = lambda sx,sy,sxy: ( (sx + sy)/2 ) + np.sqrt( ((sx - sy)/2)**2 + sxy**2 )
smin = lambda sx,sy,sxy: ( (sx + sy)/2 ) - np.sqrt( ((sx - sy)/2)**2 + sxy**2 )
tmax = lambda sx,sy,sxy: np.sqrt( ((sx - sy)/2)**2 + sxy**2 )
sprom = lambda sx,sy,sxy: (sx + sy)/2
ts = lambda sx,sy,sxy: 0.5*np.arctan2(- ( sx - sy ), 2*sxy)

def principal_stresses(sxx,syy,sxy):
	smax = ( (sxx + syy)/2 ) + np.sqrt( ((sxx - syy)/2)**2 + sxy**2 )
	smin = ( (sxx + syy)/2 ) - np.sqrt( ((sxx - syy)/2)**2 + sxy**2 )
	return smax, smin

def principal_directions(sxx,syy,sxy):
	tp1 =  0.5*np.arctan2(2*sxy, sxx - syy)
	tp2 = tp1 + np.pi/2
	return tp1, tp2

def maximum_shear_stresses(sxx,syy,sxy):
	tau_max = np.sqrt( ((sxx - syy)/2)**2 + sxy**2 )
	return tau_max

