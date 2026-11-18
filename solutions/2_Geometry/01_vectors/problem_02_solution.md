# Exercise 2. Distance as the Length of a Vector

## Question

The points are $A=(1,2,3)$ and $B=(4,-2,6)$.

1. Construct $\overrightarrow{AB}$.
2. Compute its length.
3. Compute the distance between the points using the coordinate formula.
4. Explain why both calculations give the same result.

## Solution

The displacement must point from $A$ toward $B$, so subtract the starting coordinates from the ending coordinates:

$$
\overrightarrow{AB}=(4-1,-2-2,6-3)=(3,-4,3).
$$

A check on the direction is $A+\overrightarrow{AB}=(4,-2,6)=B$. Its length follows from the three-dimensional Pythagorean theorem:

$$
\|\overrightarrow{AB}\|^2=3^2+(-4)^2+3^2=34,\qquad
\|\overrightarrow{AB}\|=\sqrt{34}.
$$

Calculating directly from the point-distance formula gives

$$
d(A,B)=\sqrt{(4-1)^2+(-2-2)^2+(6-3)^2}=\sqrt{9+16+9}=\sqrt{34}.
$$

These are two forms of the same geometry: the coordinate differences are the orthogonal components of the joining segment. Distance ignores its orientation; reversing the segment would negate the displacement but leave its length unchanged.
