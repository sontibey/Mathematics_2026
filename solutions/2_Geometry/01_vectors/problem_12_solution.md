# Exercise 12. A Normal Vector to a Plane

## Question

Given $A=(1,0,2)$, $B=(2,1,0)$, and $C=(0,3,1)$. Construct two vectors lying in the plane, find a vector perpendicular to both, and check the perpendicularity using dot products.

## Solution

Subtract the same base point from the other two points to obtain in-plane directions:

$$
p=B-A=(1,1,-2),\qquad q=C-A=(-1,3,-1).
$$

A vector perpendicular to both can be constructed by the cross product:

$$
n=p\times q=(1(-1)-(-2)(3),\ (-2)(-1)-1(-1),\ 1(3)-1(-1))=(5,3,4).
$$

This vector is nonzero, so the two directions are not parallel and the three points determine a plane. Check the two perpendicularity requirements:

$$
n\cdot p=5+3-8=0,\qquad n\cdot q=-5+9-4=0.
$$

Any vector between points of this plane is a combination of $p$ and $q$, and its dot product with $n$ is therefore zero. This explains why $n$ is normal to the whole plane. As an additional check, its equation is $5x+3y+4z=13$, satisfied by all three given points.
