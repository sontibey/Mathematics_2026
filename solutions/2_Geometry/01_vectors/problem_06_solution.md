# Exercise 6. Projection and Perpendicular Component

## Question

Find the projection of $u=(4,2)$ onto the direction $v=(1,1)$. Then compute

$$
r=u-\mathrm{proj}_v\,u
$$

and verify that $r\cdot v=0$. Explain this result geometrically.

## Solution

A projection onto the direction of $v$ has the form $p=\lambda v$. Its defining condition is that the residual $u-p$ be perpendicular to $v$, so

$$
(u-\lambda v)\cdot v=0,\qquad
\lambda=\frac{u\cdot v}{v\cdot v}=\frac{4+2}{1+1}=3.
$$

Therefore the parallel and residual parts are

$$
p=\mathrm{proj}_v\,u=3(1,1)=(3,3),\qquad
r=u-p=(4,2)-(3,3)=(1,-1).
$$

Two checks confirm the construction:

$$
r\cdot v=1-1=0,\qquad p+r=(3,3)+(1,-1)=(4,2)=u.
$$

The projection lies on the diagonal line $y=x$. The residual is the orthogonal displacement from that line to the endpoint of $u$. Thus the construction separates the original displacement into motion along the chosen direction and motion across it.
