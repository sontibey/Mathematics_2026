# Exercise 15. Comparing Directions Using the Cosine of the Angle

## Question

Given

$$
a=(1,2,1),\qquad b=(2,4,2),\qquad c=(2,0,3).
$$

For each pair, compute

$$
\frac{u\cdot v}{\|u\|\,\|v\|}.
$$

Order the pairs by increasing angle between the vectors. Explain why for $a$ and $b$ the value is $1$ even though the vectors have different lengths.

## Solution

The cosine formula removes the lengths of the two vectors and measures only their relative direction. Compute the norms and dot products first:

$$
\|a\|=\sqrt6,\qquad \|b\|=\sqrt{24}=2\sqrt6,\qquad \|c\|=\sqrt{13},
$$

$$
a\cdot b=2+8+2=12,\qquad a\cdot c=2+0+3=5,\qquad b\cdot c=4+0+6=10.
$$

The three normalized values are therefore

$$
\cos\theta_{ab}=\frac{12}{\sqrt6\,2\sqrt6}=1,
$$

$$
\cos\theta_{ac}=\frac5{\sqrt{78}},\qquad
\cos\theta_{bc}=\frac{10}{2\sqrt{78}}=\frac5{\sqrt{78}}.
$$

Because $0<5/\sqrt{78}<1$ and cosine is strictly decreasing for angles in $[0,\pi]$, the increasing-angle order is

$$
\theta_{ab}=0<\theta_{ac}=\theta_{bc}=\arccos\left(\frac5{\sqrt{78}}\right).
$$

The equality $b=2a$ explains both results: scaling by a positive factor changes length but preserves direction, so the angle between $a$ and $b$ is zero and each has the same angle with $c$. The scale factor cancels between the numerator and denominator of the cosine formula.
