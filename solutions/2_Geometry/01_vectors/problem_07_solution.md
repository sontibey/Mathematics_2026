# Exercise 7. Linear Dependence Without Heavy Computation

## Question

Given

$$
u=(1,2,3),\qquad v=(2,4,6),\qquad w=(0,1,1).
$$

Identify a specific relation between $u$ and $v$, decide whether the three vectors can be linearly independent, and explain why no long calculation is needed.

## Solution

Compare the coordinates before attempting elimination: $2(1,2,3)=(2,4,6)$, hence $v=2u$. This supplies the relation

$$
2u-v+0w=(0,0,0).
$$

The coefficients $(2,-1,0)$ are not all zero, which is exactly a witness of linear dependence. A zero coefficient for $w$ is allowed in the definition, so adding $w$ cannot make this three-vector set independent. No determinant is needed because two vectors already repeat the same direction.
