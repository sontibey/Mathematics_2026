# Exercise 15. Complete Classification of a Line Relative to a Plane

Assume $v\ne0$ and $n\ne0$. Substitution into the plane gives $n\cdot p+t(n\cdot v)=d$.

- If $n\cdot v\ne0$, there is exactly one intersection, at $t=(d-n\cdot p)/(n\cdot v)$.
- If $n\cdot v=0$ and $n\cdot p\ne d$, there is no intersection: the line is parallel and disjoint.
- If $n\cdot v=0$ and $n\cdot p=d$, every parameter works: the line is contained in the plane.

For examples take $z=0$. The line $(0,0,1)+t(0,0,-1)$ meets it once at the origin; $(0,0,1)+t(1,0,0)$ is disjoint; $(0,0,0)+t(1,0,0)$ is contained. Substituting their heights verifies all three cases.
