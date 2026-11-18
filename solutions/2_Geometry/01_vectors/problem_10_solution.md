# Exercise 10. Triangle Area from Vectors

## Question

The points $A=(0,0,0)$, $B=(2,1,0)$, and $C=(1,3,2)$ form a triangle. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$, compute the area of the parallelogram using the cross product, and then find the area of the triangle. Explain the factor $\frac12$.

## Solution

Use two sides with the same starting vertex:

$$
p=\overrightarrow{AB}=(2,1,0),\qquad q=\overrightarrow{AC}=(1,3,2).
$$

The cross product records a perpendicular direction and has magnitude equal to the parallelogram area:

$$
p\times q=(1(2)-0(3),\ 0(1)-2(2),\ 2(3)-1(1))=(2,-4,5).
$$

Its length is

$$
A_{\mathrm{parallelogram}}=\sqrt{2^2+(-4)^2+5^2}=\sqrt{45}=3\sqrt5.
$$

For an independent arithmetic check, $p\cdot p=5$, $q\cdot q=14$, and $p\cdot q=5$, so

$$
\|p\times q\|^2=(p\cdot p)(q\cdot q)-(p\cdot q)^2=5(14)-25=45.
$$

The two sides span a parallelogram divided by a diagonal into two congruent triangles. Consequently the requested triangle has area

$$
A_{\mathrm{triangle}}=\frac12(3\sqrt5)=\frac{3\sqrt5}{2}.
$$
