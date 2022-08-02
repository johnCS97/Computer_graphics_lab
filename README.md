Hello, 
This project is about Conway’s game of life (GOL).

The project was part of a university course ("Computer graphics lab, Dr.Poranne Roi") that started in October  2021 and ended in July 2022.

The main goal was to visualize the different generalizations of GOL, where implementation was done with python.

For each variation we define cell rules and transition rules, these rules can vary between two types: discrete and infinitesimal.

What we call the game field is an nxn matrix where its values get calculated with each generation, depending on the rules, some variations include smooth time transition. 

Conway's Game of life:

- discrete grid
- discrete values (0/1)
- discrete-time steps
- 8 neighbors, square
- discrete rules for the neighborhood (2333)
- diagonal and straight gliders (called "glider" and "spaceship")

![GOL](https://user-images.githubusercontent.com/92673473/182391253-07bdebd1-7251-4022-9b3c-ac8bc0759bd0.gif)

Evan's larger-than-life:

- discrete grid
- discrete values (0/1)
- discrete timesteps
- extended neighborhood ((2*r+1)^2-1 neighbors), square
- discrete rules for neighborhood (34,45,34,58)

![LTL](https://user-images.githubusercontent.com/92673473/182391404-92446549-351b-4bed-aae3-8b15570804fd.gif)

Pivato's real life:

- continuous support
- discrete values (0/1)
- discrete-time steps
- finite neighborhood (square or circular), infinitesimal "cell"
- continuous rules for neighborhood
- discrete rules for "cell", i.e. function value
- no gliders, still life in the limit

![PV](https://user-images.githubusercontent.com/92673473/182403167-641a935d-60ea-42db-927f-2f9551e012f4.gif)

Ralph's Smooth Life:

- continuous support
- continuous values between (0->1)
- smooth time steps
- finite neighborhood and finite inner region, both usually circular
- continuous rules for the neighborhood
- continuous rules for the inner region

Smooth Life calculations are a bit heavy, in order to speed things up, we have used kernel convolution with FFT, Reducing time complexity from O(n⁴) to O(n²·log(n)).

Building the kernels:
- Create two arrays with NumPy.meshgrid
- Assign them in the distance equation (d = sqrt{(x_2 - n/2)^2 + (y_2-n/2)^2})
- We use a logistic function to create the circle, giving it the anti-aliasing effect. (X0=radius)
<img width="340" alt="Screen Shot 2022-08-02 at 17 15 16" src="https://user-images.githubusercontent.com/92673473/182396627-c8e9353f-4ab1-4b2c-a784-2b098bff1ba2.png">
- To finish things app we use NumPy.roll since the reference point in the left-top corner
* to create the outer neighborhood we simply subtract the two kernels

![SL](https://user-images.githubusercontent.com/92673473/182391467-a1b51a50-e1f8-4b48-b049-fd3a51e25018.gif)

Conway's Game of Life 3D:

- discrete grid
- discrete values (0/1)
- discrete-time steps
- 26 neighbors, Cube
- discrete rules for the neighborhood (4555)
- discrete rules for cell

![GOL3D](https://user-images.githubusercontent.com/92673473/182402810-810db812-80e1-47e6-bb8a-e69da41df825.gif)

- Initialize with:

  O,X,O
  
  X,X,X
  
  O,X,O

![GOL3D_ACCORDION](https://user-images.githubusercontent.com/92673473/182391620-04ee8f6d-94c2-4e97-bdcf-2118f4481b64.gif)

Ralph's Smooth Life 3D:

- continuous support
- continuous values between (0->1)
- smooth time steps
- finite neighborhood and finite inner region, both typically spherical
- continuous rules for the neighborhood
- continuous rules for the inner region
- Similar implementation to Smooth Life 2D
- Used Marching Cubes algorithm to create the mesh
- Used shade_normals from LihgtSource 

![SL3D](https://user-images.githubusercontent.com/92673473/182391740-eefc90c5-0149-4c39-aecc-c313b7f0b7eb.gif)

Libraries:
- import numpy
- import sys
- import random
- import math
- import scipy.signal
- from matplotlib import animation
- from matplotlib import pyplot
- from matplotlib.colors import LightSource
- from mpl_toolkits.mplot3d.art3d import Poly3DCollection
- from skimage import measure
- from pickle import NONE
- from scipy.fft import fftn, ifftn
- from scipy.ndimage import convolve

