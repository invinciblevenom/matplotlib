from pylab import *
from numpy import *
import matplotlib.pyplot as plt

p_min= 10**5
p_max= 10*10**5
v_max = 0.5
r=4
γ=1.4

## process 1-2
p1= p_min
v1= v_max
v2 = v1/r
c1 = p1*v1

##process 2-3
c2 = c1*(v2**(γ-1))
p3= p_max
v3= (c2/p3)**(1/γ)

##process 3-4
c3= p3*v3

## process 4-1
c4= p1*v1**γ
v4= (c4/c3)**(1/(γ-1))

##plotting
##process 1-2
v= linspace(v1,v2,30)
p= c1/v
plt.plot (v,p, 'r-')

##process2-3
v= linspace(v3,v2,30)
p= c2/v**γ
plt.plot(v,p, 'b-')

##process 3-4
v= linspace(v3,v4,30)
p= c3/v
plt.plot(v,p, 'k-')

## process 4-1
v= linspace(v4,v1,30)
p= c4/v**γ
plt.plot(v,p, 'g-')

plt.show()
