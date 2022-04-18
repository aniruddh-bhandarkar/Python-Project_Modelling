"""
Python code to animate wave motion and view different plots as they propagate in time.
Credit: University of Wyoming, 2017
Modified: Aniruddh Pravin Bhandarkar
"""
# Importing required libraries 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# important variables in any simulation (step in seconds)
step = 0.05
numstep = 1000

# change to see the wave vary with amplitude
#amp = 1.0

print(" Welcome to the Simple Harmonic Motion (Simulation)")  
print(" Equation being simulated in amp*np.sin(2*np.pi*freq*t) in 1000 steps")

while True: 
  try:#try and except block to ensure that values of the frequency of the waves and amplitude of the wave is within certain thresholds
    freq = int(input(" Enter the frequency of the wave  (range between 1 and 2): "))  #frequency of the wave
    if (freq < 1 or freq > 3):
      raise ValueError(" The steps should be between 1 - 2!")
    
    amp = float(input(" Enter the amplitude of the wave  (range between 0.5 and 2): "))  #amplitude of the wave
    if (amp < 0.5 or amp>2):
      raise ValueError(" The amplitude of the wave should be between 0.5 - 2!")
    break
  except ValueError as ve:
    print(ve)

# Defining a function to compute the y values for plotting
def data_gen():
    # time variable starting at 0 seconds
    t = 0
    # plotting 1000 points iteratively
    ctr = 0
    for ctr in range(numstep):
        # calculating the y value for each wave at a given time (1 Hz)
        y1 = amp*np.sin(2*np.pi*freq*t)
        # SHM wave with twice the frequency
        y2 = amp*np.sin(2*np.pi*freq*2*t)
        # SHM wave with a damping coefficient i.e. damped sine wave
        # (decay OR damping constant = 0.4)
        y3 = amp*np.sin(2*np.pi*freq*t) * np.exp(-t*0.4)
        # moving through time in 0.05 second intervals i.e. stepping through time
        t += step
        yield t, y1, y2, y3


# create a figure with three subplots and set the size of the window
fig, (ax1, ax2, ax3) = plt.subplots(3,1,figsize=(10,20))

# initializations to set the limits for each axis and introduce a grid
for ax in [ax1, ax2, ax3]:
    ax.set_ylim(-(amp+0.2), (amp+0.2))
    # change this for a simulation of a certain number of seconds (10 as of now)
    ax.set_xlim(0, 10)
    ax.grid()
    # introducing gridlines at each number between 1 and 10
    ax.set_xticks(np.arange(1,11))

# data arrays to store the values for plotting
# time in the X axis and values of the wave in the Y axis
xdata, y1data, y2data, y3data = [], [], [], []

# intialize three line objects (one in each subplot)
line1, = ax1.plot(xdata, y1data, color='g')
line2, = ax2.plot(xdata, y2data, color='c')
line3, = ax3.plot(xdata, y3data, color='r')
line = [line1, line2, line3]

# setting the title for each subplot 

ax1.set_title('SHM wave with frequency of Hz {}'.format(freq),size=10)
ax2.set_title('SHM wave with frequency of Hz {}'.format(2*freq), size=10)
ax3.set_title('Damped sine wave with decay constant of 0.4', size=10)

# labeling the x axis as time in seconds and setting the fontsize
ax3.set_xlabel('Time (s)', size=15)

# defining a function to obtain the data values
def calculate(data):
    # update the data
    x, y1, y2, y3 = data
    xdata.append(x)
    y1data.append(y1)
    y2data.append(y2)
    y3data.append(y3)

    # update the data of both line objects
    line[0].set_data(xdata, y1data)
    line[1].set_data(xdata, y2data)
    line[2].set_data(xdata, y3data)
    return line

ani = animation.FuncAnimation(fig, calculate, data_gen, blit=False, interval=50, repeat=False)
plt.show()