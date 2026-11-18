# Exercise 12. Intersection Line of Two Planes

## Question

Find a parametric equation of the line that is the intersection of

$$
x+y+z=3,\qquad x-y+z=1.
$$

Find its direction vector in two ways: from the system of equations and from the cross product of the normal vectors. Compare the results.

## Solution

Subtracting the second plane equation from the first gives $2y=2$, so $y=1$ and $x+z=2$. Set $z=t$:

$$
(x,y,z)=(2,1,0)+t(-1,0,1).
$$

The direction read from the equations is $v=(-1,0,1)$. The normals give

$$
(1,1,1)\times(1,-1,1)=(2,0,-2)=-2v.
$$

These are parallel directions, so they describe the same line. Substituting the parametric coordinates gives constants 3 and 1 in the two plane equations for every $t$.
