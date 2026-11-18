# Exercise 4. Dot Product and Perpendicularity

## Question

For $u=(1,2,-1)$ and $v=(2,-1,3)$ compute $u\cdot v$ and determine whether the vectors are perpendicular. Then find $a$ so that $w=(2,-1,a)$ is perpendicular to $u$, and check the result.

## Solution

For nonzero vectors, the dot product is $u\cdot v=\|u\|\|v\|\cos\theta$, so perpendicularity is equivalent to a zero dot product. Here

$$
u\cdot v=1(2)+2(-1)+(-1)(3)=2-2-3=-3.
$$

The result is not zero, so the two given vectors are not perpendicular; its negative sign also indicates an obtuse angle. For the unknown third coordinate in $w$, impose the perpendicularity condition before solving:

$$
u\cdot w=1(2)+2(-1)+(-1)a=-a=0.
$$

It follows that $a=0$. The resulting vector $w=(2,-1,0)$ is nonzero, and direct substitution checks the condition:

$$
(1,2,-1)\cdot(2,-1,0)=2-2+0=0.
$$
