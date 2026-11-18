# Exercise 14. Closest Point on a Line

## Question

Given a point $P=(4,1)$ and a line through the origin with direction $v=(1,2)$. Using projection, find the closest point on the line, the distance from $P$ to the line, and verify that the appropriate vector is perpendicular to the direction of the line.

## Solution

Every point on the line is $Q=tv=(t,2t)$. For the closest point, the connecting displacement $P-Q$ must be perpendicular to the line direction. Solve this condition:

$$
(P-tv)\cdot v=(4-t,1-2t)\cdot(1,2)=6-5t=0,
\qquad t=\frac65.
$$

Thus the projection point and displacement are

$$
Q=(6/5,12/5),\qquad P-Q=(14/5,-7/5).
$$

The perpendicularity check and distance are

$$
(P-Q)\cdot v=14/5-14/5=0,
$$

$$
d=\|P-Q\|=\sqrt{196/25+49/25}=\sqrt{49/5}=\frac7{\sqrt5}.
$$

To justify that this is a minimum rather than just a stationary construction, any other line point is $Q+sv$. Orthogonality gives

$$
\|P-(Q+sv)\|^2=\|P-Q\|^2+s^2\|v\|^2=\frac{49}{5}+5s^2.
$$

This is minimized uniquely at $s=0$, proving that $Q$ is the closest point.
