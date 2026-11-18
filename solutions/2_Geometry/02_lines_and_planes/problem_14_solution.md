# Exercise 14. Contrast: Intersection and Parallelism

## Question

From the point $P=(0,0,1)$, two lines are drawn with direction vectors

$$
v_1=(2,1,-1),\qquad v_2=(2,1,0).
$$

For each line, analyze its position relative to the plane $z=0$.

For the line that intersects the plane, find the intersection point. For the other line, explain how you can recognize parallelism without solving an equation.

## Solution

The plane normal is $n=(0,0,1)$. For $v_1$, $n\cdot v_1=-1\ne0$, so the line intersects once. Its height is $1-t$, giving $t=1$ and intersection $(2,1,0)$. For $v_2$, $n\cdot v_2=0$ and the base point has height 1, so the line is parallel to and disjoint from the plane. Its height remains 1 for all parameters; no equation solving is needed.
