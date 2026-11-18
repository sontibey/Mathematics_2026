# Exercise 11. Decomposition into Parallel and Perpendicular Components

## Question

Decompose $u=(3,4)$ into components parallel and perpendicular to $v=(1,2)$. Check

$$
u=u_{\parallel}+u_{\perp},\qquad u_{\perp}\cdot v=0.
$$

Explain why these are two independent checks of correctness.

## Solution

Write the parallel component as $u_{\parallel}=\lambda v$. The perpendicular component is then forced to be $u_{\perp}=u-\lambda v$. Requiring its dot product with $v$ to vanish gives

$$
(3-\lambda,4-2\lambda)\cdot(1,2)=11-5\lambda=0,
\qquad \lambda=\frac{11}{5}.
$$

Hence

$$
u_{\parallel}=(11/5,22/5),\qquad
u_{\perp}=(3-11/5,4-22/5)=(4/5,-2/5).
$$

The reconstruction check is

$$
u_{\parallel}+u_{\perp}=(15/5,20/5)=(3,4)=u.
$$

The separate directional check is

$$
u_{\perp}\cdot v=4/5+2(-2/5)=0.
$$

Reconstruction alone allows arbitrary incorrect splits, while orthogonality alone does not require the two components to sum to $u$. Together with the explicit parallel form of $u_{\parallel}$, these conditions establish the required decomposition. A further length check gives $\|u\|^2=25=121/5+4/5$, the sum of the squared component lengths.
