# Importing libraries 
import matplotlib.pyplot as plt 
import numpy as np 
import math 

# Placing the plots in the plane 
plot1 = plt.subplot2grid((4, 4), (0, 0), colspan=2) 
plot2 = plt.subplot2grid((3, 3), (0, 2), rowspan=3, colspan=2) 
plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2) 

# Using Numpy to create an array x 
x = np.arange(1, 10) 

# Plot for square root 
plot2.plot(x, x**0.5) 
plot2.set_title('Square Root') 

# Plot for exponent 
plot1.plot(x, np.exp(x)) 
plot1.set_title('Exponent') 

# Plot for Square 
plot3.plot(x, x*x) 
plot3.set_title('Square') 

# Packing all the plots and displaying them 
plt.tight_layout() 
plt.show() 
