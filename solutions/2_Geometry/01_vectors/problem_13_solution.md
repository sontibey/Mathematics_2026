# Exercise 13. Do Four Points Lie in One Plane?

## Question

Given

$$
A=(0,0,0),\qquad B=(1,2,0),\qquad C=(0,1,1),\qquad D=(2,5,1).
$$

1. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Find $n=\overrightarrow{AB}\times\overrightarrow{AC}$.
3. Construct $\overrightarrow{AD}$ and check whether $\overrightarrow{AD}\cdot n=0$.
4. Based on this, decide whether $D$ lies in the plane determined by $A,B,C$, and justify the criterion.

## Solution

With $A$ as the common starting point, the first two displacements are

$$
p=\overrightarrow{AB}=(1,2,0),\qquad q=\overrightarrow{AC}=(0,1,1).
$$

Compute their normal:

$$
n=p\times q=(2(1)-0(1),\ 0(0)-1(1),\ 1(1)-2(0))=(2,-1,1).
$$

Since $n\ne0$, the first three points determine a unique plane. For the fourth point,

$$
\overrightarrow{AD}=(2,5,1),\qquad
\overrightarrow{AD}\cdot n=2(2)+5(-1)+1(1)=0.
$$

A zero dot product means this displacement has no component in the normal direction, so $D$ lies in the plane through $A,B,C$. Its equation is $2x-y+z=0$, and $D$ satisfies $4-5+1=0$. There is also a direct reconstruction check: $\overrightarrow{AD}=2p+q$, explicitly expressing the displacement as a combination of the two in-plane directions.
