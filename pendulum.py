#The modules used here is matplotlib,numpy,Vpython
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
from vpython import *
#Three modules

#Parameters to control for Simple Pendulum: Theta,Length
g = 9.81 # gravity

while True:
  try:
    l = int(input("Enter the length for the Pendulum (range between 10 and 50): "))  #length of pendulum arm
    if (l < 10 or l>51):
      raise ValueError("The length of Pendulum should be between 10 - 50!")
    
    m = int(input("Enter the mass of the Pendulum (range between 1 and 10): "))  #mass of pendulum weight
    if (m < 1 or m>10):
      raise ValueError("The mass of the Pendulum should be between 1 - 10!")
    break
  except ValueError as ve:
    print(ve)
"""
Paramters set for the Pendulum
Here is a try except block to handle the excpetions such as adding values beyond the range for the 2 parameters
"""

bob=sphere(pos=vector(5,2,0),radius=m/10,color=color.blue)
pivot=vector(0,10,0)
roof=box(pos=pivot,size=vector(10,0.5,10),color=color.green)
rod=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.red)
"""
Using Vpython, we are able visualize the physical phenomena
The bob, rod is the rope moving the pendulum,pivot is used to keep the pendulum
"""
#Rope Equation & Constraints
t=0 # time 
dt=0.01 # time interval 
l=mag(bob.pos-pivot) # length of pendulum
cs=(pivot.y-bob.pos.y)/l # calculation of cos(theta) 
theta=acos(cs) # angle with vertical direction
vel=0.0 # angular velocity
"""
Here the equation is drawn for the pendulum
There are small units of time that are taken of the rope
The angle to made by the rod/rope to the pivot is a cos theta by vector resolution in a 2-d Plane
"""
#Bob Equation and constraints
while (t<100):
  rate(100) # maximum 100 calculations per second
  acc=-g/l*sin(theta) # updating of angular acceleration
  theta=theta+vel*dt # updating of angular position
  vel=vel+acc*dt # updating of angular velocity
  bob.pos=vector(l*sin(theta),pivot.y-l*cos(theta),0) # cal. position
  rod.axis=bob.pos-rod.pos # updating other end of rod of pendulum
  t=t+dt # updating time
"""
rate(100)=>Here the bob is given a calcultaion time per second, this is used to reduce the time dt so as to make the motion more continous
than discrete points
acc=> Used to show the bob resolution and the vector resolution 
"""






