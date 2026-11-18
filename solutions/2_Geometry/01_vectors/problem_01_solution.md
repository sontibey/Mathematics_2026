# Exercise 1. Vector Operations and Their Meaning

## Question

For $u=(2,-1,3)$ and $v=(-1,4,2)$ compute

$$
u+v,\qquad u-v,\qquad 3u-2v.
$$

Then verify that $(u+v)-v=u$, and explain geometrically what adding two vectors means.

## Solution

A vector sum records the combined displacement along each coordinate axis. Subtraction reverses the second displacement, while scalar multiplication scales every coordinate. Applying these definitions gives

$$
u+v=(2+(-1),-1+4,3+2)=(1,3,5),
$$

$$
u-v=(2-(-1),-1-4,3-2)=(3,-5,1).
$$

For the weighted combination, first scale the vectors and then subtract:

$$
3u=(6,-3,9),\qquad 2v=(-2,8,4),
$$

$$
3u-2v=(6-(-2),-3-8,9-4)=(8,-11,5).
$$

The required recovery check is

$$
(u+v)-v=(1-(-1),3-4,5-2)=(2,-1,3)=u.
$$

Geometrically, start with displacement $u$ and then make displacement $v$ from its endpoint. The vector from the initial point to the final point is $u+v$. Translating a vector to join these steps does not change it. Placing both tails at the same point instead gives the parallelogram construction.
