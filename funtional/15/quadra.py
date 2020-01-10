
from main import a,b,c
import math
delt=pow(b,2)-4*a*c
if(delt>0):
    x1=(-b+(math.sqrt(delt)))/2*a
    x2=(-b-(math.sqrt(delt)))/2*a
    print('the roots are {} and {}'.format(x1,x2))
else:
    print('delta is less that 0')
