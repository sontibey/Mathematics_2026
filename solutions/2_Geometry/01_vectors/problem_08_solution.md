# Exercise 8. Linear Combination and Checking the Result

## Question

Check whether $w=(5,1)$ can be written as

$$
w=au+bv,
$$

where $u=(1,1)$ and $v=(2,-1)$. If so, find $a,b$, reconstruct $w$ from them, and explain the geometric meaning of the existence of such coefficients.

## Solution

The proposed equality must hold in both coordinates. Substituting the given vectors yields

$$
a+2b=5,\qquad a-b=1.
$$

The second equation gives $a=1+b$. Substitution into the first gives $1+3b=5$, hence $b=4/3$ and $a=7/3$. Check the reconstructed vector explicitly:

$$
\frac73(1,1)+\frac43(2,-1)
=(7/3,7/3)+(8/3,-4/3)=(5,1)=w.
$$

Thus the representation exists. It is unique because $u$ and $v$ are nonparallel: their coordinate determinant is $1(-1)-2(1)=-3\ne0$. Geometrically, the two coefficients specify the scaled displacements along two independent directions whose combined endpoint is $w$.
