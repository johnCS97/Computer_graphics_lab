Hello, 
This project is about conway’s game of life (GOL).
The project was part of a university course that started in October  2021, and ended in July 2022.
The main goal was to visualize the different generalizations of GOL, were implementaion was done with python and some libriries from there.
For each variation we define cell rules and transition rules ,these rules can vary between two types: discrete and infistimal.
What we call the game field is an nxn by matrix were it's values gets calculated with each generation, depending on the rules, some variations include smooth time transtion. 

Conway's Game of life:

- discrete grid
- discrete values (0/1)
- discrete time steps
- 8 neighbors, square
- discrete rules for neighborhood (2333)
- discrete rules for cell
- diagonal and straight gliders (called "glider" and "spaceship")

Evan's larger than life:

- discrete grid
- discrete values (0/1)
- discrete timesteps
- extended neighborhood (2*r+1)^2-1 neighbors), square
- discrete rules for neighborhood (34,45,34,58)
- discrete rules for cell

Pivato's real life:

- continuous support (more in the spirit of excitable media and reaction diffusion)
- discrete values (0/1)
- discrete time steps
- finite neighborhood (square or circular), infinitesimal "cell"
- continuous rules for neighborhood (filling between 0 (empty) and 1 (full))
- discrete rules for "cell", i.e. function value
- no gliders, still life in the limit

Ralph's Smooth Life:

- continuous support
- continuous values between (0->1)
- smooth time steps
- finite neighborhood and finite inner region, both typically circular
- continuous rules for neighborhood
- continuous rules for inner region

Conway's Game of life 3D:

- discrete grid
- discrete values (0/1)
- discrete time steps
- 26 neighbors, Cube
- discrete rules for neighborhood (4555)
- discrete rules for cell

Ralph's Smooth Life 3D:

- continuous support
- continuous values between (0->1)
- smooth time steps
- finite neighborhood and finite inner region, both typically sphrical
- continuous rules for neighborhood
- continuous rules for inner region
