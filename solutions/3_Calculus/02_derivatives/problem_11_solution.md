# Exercise 11. Derivative from the Definition

## Question

Using only

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h,
$$

find the derivative of $f(x)=x^2$. Compare the result with the power rule and indicate where the limit is used in the calculation.

## Solution

Using the definition, for $h\ne0$,

$$
\frac{(x+h)^2-x^2}{h}=\frac{2xh+h^2}{h}=2x+h.
$$

$$
f\prime(x)=\lim_{h\to0}(2x+h)=2x.
$$

The limit is used only after simplifying the difference quotient on the punctured neighborhood $h\ne0$. The result agrees with the power rule for $x^2$.
