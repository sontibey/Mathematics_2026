# Exercise 11. Volume of a Solid of Revolution

## Question

The region under the graph

$$
y=\sqrt{x},\qquad x\in[0,4],
$$

is rotated about the $x$-axis.

1. Construct the integral describing the volume using the disk method.
2. Compute the volume.
3. Explain where the factor $\pi y^2$ in the integral comes from.

## Solution

A slice perpendicular to the $x$-axis is a disk of radius $y=\sqrt x$. Its cross-sectional area is $\pi y^2=\pi x$, since rotating the vertical segment from 0 to $y$ fills a disk. Summing thin disks gives

$$
V=\int_0^4\pi(\sqrt x)^2\,dx=\pi\left[\frac{x^2}{2}\right]_0^4=8\pi.
$$

The volume is $8\pi$ cubic units. The factor $\pi y^2$ comes from disk area, not from an unexplained volume rule.
