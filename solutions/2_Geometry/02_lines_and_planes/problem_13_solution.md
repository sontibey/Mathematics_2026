# Exercise 13. Closest Point on a Plane

For $n=(1,2,2)$, $\|n\|^2=9$ and $n\cdot P-4=-1$. The projection is

$$
Q=P-\frac{-1}{9}n=(28/9,2/9,2/9).
$$

It lies on the plane because $(28+4+4)/9=4$. The displacement $Q-P=n/9$ is normal, and its length is $\|n\|/9=1/3$. Any other point $Y$ on the plane has $Y-Q$ perpendicular to $P-Q$, so $\|P-Y\|^2=\|P-Q\|^2+\|Q-Y\|^2\ge\|P-Q\|^2$. This proves that $Q$ is the closest point.
