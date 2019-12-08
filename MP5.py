import numpy as np

import matplotlib.pylab as plot

n = np.linspace(0,199,200)

s = input("Input your function, x(n):") 
         
def x(n): 
    
    evaluate = eval(s)
    return evaluate
      

for i in range(0,200):
    
    if i==0:
        y = (-1.5*x(n))+(2*x(n+1))-(0.5*x(n+2))
        
      
    elif i==199:
        y = (1.5*x(n))-(2*x(n-1))+(0.5*x(n-2))
        
    else:
        y = (0.5*x(n+1))-(0.5*x(n-1))
        



plot.plot(x(n), 'g-', label = 'range of n' )
plot.legend()
plot.plot(y, 'r-', label = 'Values Y(n) given X(n)')
plot.legend()
plot.grid()
plot.show()

