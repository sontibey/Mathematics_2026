# Exercise 5. Angle Between Vectors

## Question

Given $u=(1,1,0)$ and $v=(1,0,1)$:

1. Use the sign of $u\cdot v$ to predict the type of angle.
2. Compute the angle.
3. Compare the result with the prediction.

## Solution

First calculate the dot product without evaluating an inverse trigonometric function:

$$
u\cdot v=1(1)+1(0)+0(1)=1>0.
$$

Both vectors are nonzero, so their norm product is positive. The cosine of their angle must therefore be positive, predicting an acute angle. The lengths are

$$
\|u\|=\sqrt{1^2+1^2+0^2}=\sqrt2,\qquad
\|v\|=\sqrt{1^2+0^2+1^2}=\sqrt2.
$$

Now use the angle formula:

$$
\cos\theta=\frac1{\sqrt2\sqrt2}=\frac12,\qquad
\theta=\frac\pi3=60^\circ.
$$

This lies strictly between zero and $90^\circ$, agreeing with the initial sign prediction. The equal lengths alone would not determine the angle; the dot product measures the directional relationship.
