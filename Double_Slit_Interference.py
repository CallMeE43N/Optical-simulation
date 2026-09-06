import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSCM

#This function without the width of the single slit.
#It's only for the simple double slit interference.

def Intensity(x,dis_lit,dis_screen,wave_length):
    #formulation: I(x) =  4*I0*cos^2(np.pi*dis_lit*x/wave_length*dis_screen)
    #default the value of I0 = 1.
    I0 = 1
    element = (np.pi * dis_lit * x) / (wave_length * dis_screen)
    intensity = 4 * I0 * np.cos(element)**2
    return intensity

#The default units of the parameters aremeter(m).
#dis_lit = 5e-4 m, dis_screen = 0.5 m, wave_length = 530 nm = 5.3e-7 m
dis_lit = 5e-4
dis_screen = 2
wave_length = 5.3e-7

wideth_screen = L = 1
x = np.linspace(-L/2,L/2,10000)
y = Intensity(x,dis_lit,dis_screen,wave_length)

s = slice(4950,5050)
y_plt = y[s]
x_plt = x[s]
print(np.size(y_plt))
print(np.size(x_plt))

dim2_array = np.array([y_plt,y_plt])

'''
print(dim2_array)
min = y.min()
max = y.max()
print(y.shape)
print(max)
print(min)
'''

#define the colormap,the values is from 0 to 1, and the colors is from black to green.
colors  = ["#061F06B5","#16FF16"]
custom_cmap = LSCM.from_list('black_green',colors)

fig,(ax2,ax1) = plt.subplots(1,2,figsize=(10,5))
im  = ax1.imshow(dim2_array, extent = [-55,55,0,50], cmap=custom_cmap, vmin = 1, vmax = 4, origin = 'lower',interpolation = 'nearest')
im  = ax1.imshow(dim2_array, extent = [-55,55,0,50], cmap=custom_cmap, vmin = 1, vmax = 4, origin = 'lower')
colorbar = fig.colorbar(im, ax=ax1, label='Value (0-1)')
ax1.set_xlabel('x(m)')
ax1.set_title('Double slit interference')

ax2.set_xlabel('x(m)')
ax2.set_ylabel('Intensity (W/m^2)')    
ax2.set_title('Double slit interference')
ax2.plot(x_plt,y_plt)
ax2.set_xlim(-0.00495,0.00505)
#ax2.set_xlim(-0.495,0.505)
#ax2.set_ylim(0,4)
ax2.set_aspect('auto')
ax2.grid(True)
plt.tight_layout()

plt.show()





    