# Exercise 5. Distance from Velocity

## Question

The velocity of a car during the first five seconds is described by the function

$$
v(t)=4t+2\quad [\mathrm{m/s}].
$$

Compute the distance traveled and explain why the integral of velocity gives the change in position.

Then answer what would have to be changed in the reasoning if the velocity also took negative values.

## Solution

Velocity is positive throughout $0\le t\le5$, so distance equals displacement:

$$
D=\int_0^5(4t+2)\,dt=\left[2t^2+2t\right]_0^5=60\,\mathrm m.
$$

Since $v=s\prime$, the fundamental theorem gives $\int v\,dt=s(5)-s(0)$. If velocity took negative values, this integral would still give displacement, while total distance would be $\int_0^5|v(t)|\,dt$, splitting at sign changes.
