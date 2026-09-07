import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as lscm

'''                   The essential parameters of the experiment             '''
'''                         Phenomenon: Missing Orders                       '''

#The wavelength of the light:                   wavelength-->lambda = 640 nm (6.4e-7 m)
#The distance between the two slits:            d-->d = 0.5 mm               (5e-4 m)
#The distance between the screen and the slits: D-->D = 1 m
#The width of the slits:                        w-->w = 0.02 mm              (2e-5 m)

#The ligth intensity is defaultly set to 1

'''        formulation : I = I0 * (sin(alpha) / alpha) ^ 2 * cos^2(beta)      '''

#The single slit parameter:  alpha-->alpha = (pi * w * x) / (lambda * D)
#The double slit parameter:  beta --> beta = (pi * d * x) / (lambda * D)

'''    ========Python========numpy========   ========Python========numpy========    '''

lam = 6.4e-7 #(m)
d = 5e-3 #(m)
D = 2 #(m)
w = 2e-5 #(m)
I0 = 1
L = 1 #(m) length of the screen

def intensity(x,lam,d,D,w,I0):

    alpha = (np.pi * w * x) / (lam * D)
    beta = (np.pi * d * x) / (lam * D)
    I = I0 * (np.sin(alpha) / alpha)  ** 2 * np.cos(beta) ** 2

    return I

x1 = np.linspace(-L/2,L/2,1000)   # 1000 points
y1 = intensity(x1,lam,d,D,w,I0)
y1_tile = np.tile(y1,(2,1))
y1_slice = y1_tile[0:2,450:550]
print(y1_slice.shape)
print(y1_tile.shape)


x2 = np.linspace(-L/2,L/2,10000)  # 10000 points
y2 = intensity(x2,lam,d,D,w,I0)
y2_tile = np.tile(y2,(2,1))
y2_slice  = y2_tile[0:2,4500:5500]
print(y2_slice.shape)
print(y2_tile.shape)


x3 = np.linspace(-L/2,L/2,100000) # 100000 points
y3 = intensity(x3,lam,d,D,w,I0)
y3_tile = np.tile(y3,(2,1))
y3_slice  = y3_tile[0:2,45000:55000]
print(y3_slice.shape)
print(y3_tile.shape)

'''         ========Python========Matplotlib========   ========Python========Matplotlib========         '''

fig,axes = plt.subplots(3,3,figsize = (10,7))

colors = ["#350606B5","#BE080EB5"]
color_map = lscm.from_list('Dark_to_light',colors)

#1000 points
axes[0,0].plot(x1,y1,linewidth = 1)
axes[0,0].set_title('1000 points')
axes[0,0].set_xlabel('x (m)')
axes[0,0].set_ylabel('I (W/m^2)')
axes[0,0].set_xlim(-L/2,L/2)

im1 = axes[0,1].imshow(y1_tile,cmap=color_map,extent=[-500,500,0,200],origin='lower',interpolation='nearest')
colorbar1 = fig.colorbar(im1,ax=axes[0,1],label='I (W/m^2)')
axes[0,1].set_title('The whole screen')
axes[0,1].set_xlabel('Position')

im1 = axes[0,2].imshow(y1_slice,cmap=color_map,extent=[-50,50,0,20],origin='lower',interpolation='nearest')
colorbar1_ = fig.colorbar(im1,ax=axes[0,2],label='I (W/m^2)')
axes[0,2].set_title('The center of the screen')
axes[0,2].set_xlabel('Position')

#10000 points
axes[1,0].plot(x2,y2,linewidth = 1)
axes[1,0].set_title('10000 points')
axes[1,0].set_xlabel('x (m)')
axes[1,0].set_ylabel('I (W/m^2)')
axes[1,0].set_xlim(-L/2,L/2)

im2 = axes[1,1].imshow(y2_tile,cmap=color_map,extent=[-5000,5000,0,2000],origin='lower',interpolation='nearest')
colorbar2 = fig.colorbar(im2,ax=axes[1,1],label='I (W/m^2)')
axes[1,1].set_title('The whole screen')
axes[1,1].set_xlabel('Position')

im2 = axes[1,2].imshow(y2_slice,cmap=color_map,extent=[-500,500,0,200],origin='lower',interpolation='nearest')
colorbar2_ = fig.colorbar(im2,ax=axes[1,2],label='I (W/m^2)')
axes[1,2].set_title('The center of the screen')
axes[1,2].set_xlabel('Position')

#100000 points
axes[2,0].plot(x3,y3,linewidth = 1)
axes[2,0].set_title('100000 points')
axes[2,0].set_xlabel('x (m)')
axes[2,0].set_ylabel('I (W/m^2)')
axes[2,0].set_xlim(-L/2,L/2)

im3 = axes[2,1].imshow(y3_tile,cmap=color_map,extent=[-50000,50000,0,20000],origin='lower',interpolation='nearest')
colorbar3 = fig.colorbar(im3,ax=axes[2,1],label='I (W/m^2)')
axes[2,1].set_title('The whole screen')
axes[2,1].set_xlabel('Position')

im3 = axes[2,2].imshow(y3_slice,cmap=color_map,extent=[-5000,5000,0,2000],origin='lower',interpolation='nearest')
colorbar3_ = fig.colorbar(im3,ax=axes[2,2],label='I (W/m^2)')
axes[2,2].set_title('The center of the screen')
axes[2,2].set_xlabel('Position')

fig.suptitle('Intensity of the light at different resolutions',fontsize=16)
plt.subplots_adjust(hspace=0.3,wspace=0.3)
plt.subplots_adjust(top=0.9)
plt.tight_layout()
plt.show()
