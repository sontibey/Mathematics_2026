# Exercise 3. A Box Made from Cardboard

## Question

From a $30\,\mathrm{cm}\times40\,\mathrm{cm}$ sheet, squares of side length $x$ are cut from the corners and the edges are folded up to form an open box.

Write the volume as a function of $x$, determine the physically meaningful domain, and find the value of $x$ for which the volume is greatest.

## Solution

If $x$ is measured in centimeters, the box has height $x$ and base $(30-2x)\times(40-2x)$, hence

$$
V(x)=x(30-2x)(40-2x)=1200x-140x^2+4x^3,\qquad 0<x<15.
$$

$$
V\prime(x)=1200-280x+12x^2=0\quad\Longleftrightarrow\quad x=\frac{35\pm5\sqrt{13}}3.
$$

Only $x_*=(35-5\sqrt{13})/3\approx5.6574\,\mathrm{cm}$ is in the physical domain. The derivative is positive before $x_*$ and negative after it until 15, so this is the global maximum. The other root is approximately 17.68 and is inadmissible. The limiting volumes at 0 and 15 are zero. The maximum volume is approximately $3032.30\,\mathrm{cm}^3$.
