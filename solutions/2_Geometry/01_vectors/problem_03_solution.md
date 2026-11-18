# Exercise 3. Vector Normalization

## Question

For $v=(3,4)$ find a unit vector $e$ with the same direction and orientation. Check that $\|e\|=1$, reconstruct $v$ in the form $v=\|v\|e$, and explain what changes during normalization and what remains unchanged.

## Solution

To retain direction and orientation, look for $e=\lambda v$ with a positive scalar $\lambda$. Since $\|v\|=\sqrt{3^2+4^2}=5$, the requirement $\|e\|=\lambda\|v\|=1$ determines $\lambda=1/5$. Thus

$$
e=(3/5,4/5).
$$

Check the unit-length condition and recovery of the original vector separately:

$$
e\cdot e=\frac9{25}+\frac{16}{25}=1,\qquad \|e\|=1,
$$

$$
\|v\|e=5(3/5,4/5)=(3,4)=v.
$$

Normalization changes the magnitude from 5 to 1. It preserves the line of action and orientation because the scale factor is positive. A negative factor would reverse the orientation and would not meet the question's requirement.
