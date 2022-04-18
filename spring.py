#The modules used here is matplotlib,numpy,Vpython
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from vpython import *
"""
The three modules
"""

wall=box(pos=vector(0,1,0),size=vector(0.2,3,2),color=color.yellow) 
floor=box(pos=vector(6,-0.6,0),size=vector(14,0.2,4),color=color.yellow)
Mass=box(pos=vector(9,0,0),velocity=vector(1,0,0),size=vector(1,1,1),mass=1.0,color=color.red)
pivot=vector(0,0,0)
spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.4,constant=1,thickness=0.1,coils=20,color=color.green)
eq=vector(9,0,0)
"""
Using V Python to draw the objects required to visualize the physics phenonmena
"""
  
t=0
dt=0.001
while (t<50):
    rate(1000)
    acc=(eq-Mass.pos)*(spring.constant/Mass.mass)
    Mass.velocity=Mass.velocity+acc*dt
    Mass.pos=Mass.pos+Mass.velocity*dt
    spring.axis=Mass.pos-spring.pos
    KE=0.5*Mass.mass*(Mass.velocity.x)**2
    PE=0.5*spring.constant*(eq.x-Mass.pos.x)**2
    t=t+dt
"""
The functions mentioned above are used to model the equation for  a small time dt
Here the velocity is added with a*dt which equates to v
KE and PE are to put parameters on the motion of the spring
"""

def f(x):
  print(x.value)
  slider(bind=f,vertical=False,min=0, max=10,step=1,value=5,length=200,width=10)
"""
The function of the spring movement
"""





