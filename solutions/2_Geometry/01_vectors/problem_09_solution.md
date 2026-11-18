# Exercise 9. Cross Product as a Perpendicular Direction

## Question

For $u=(1,2,0)$ and $v=(0,1,3)$ compute $u\times v$. Use dot products to check perpendicularity to both vectors, compute $v\times u$, and compare the results.

## Solution

Use the coordinate rule for the oriented cross product:

$$
u\times v=(u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1).
$$

Substituting the coordinates gives

$$
u\times v=(2(3)-0(1),\ 0(0)-1(3),\ 1(1)-2(0))=(6,-3,1).
$$

Perpendicularity is checked independently against each original vector:

$$
(6,-3,1)\cdot(1,2,0)=6-6+0=0,
$$

$$
(6,-3,1)\cdot(0,1,3)=0-3+3=0.
$$

Calculating in the reverse order gives

$$
v\times u=(1(0)-3(2),\ 3(1)-0(0),\ 0(2)-1(1))=(-6,3,-1).
$$

The two results are negatives. They determine the same normal line and have the same length $\sqrt{46}$, but opposite orientations, consistent with the right-hand rule.
