# Exercise 10. Projection of a Point onto a Plane

## Question

Find the orthogonal projection of $P=(2,1,3)$ onto the plane $x+y+z=3$, and then find the reflection of $P$ across this plane. Check that the midpoint of the segment joining the point and its reflection lies on the plane.

## Solution

For $n=(1,1,1)$ and $d=3$, the signed correction factor is $(n\cdot P-d)/\|n\|^2=(6-3)/3=1$. Hence

$$
Q=P-n=(1,0,2),\qquad P^*=P-2n=(0,-1,1).
$$

The projection $Q$ lies on the plane since $1+0+2=3$, and $P-Q=n$ is normal. The midpoint $(P+P^*)/2=(1,0,2)=Q$ lies on the plane. Thus $P^*$ is the reflection.
