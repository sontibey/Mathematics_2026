# Exercise 3. The Product Rule — Why Is It Needed?

## Question

For

$$
f(x)=(x^2+1)e^x
$$

compute the derivative. Then compare the correct result with the incorrect idea

$$
f'(x)\stackrel{?}{=}(2x)e^x
$$

and explain which term is missing.

## Solution

The product rule differentiates each varying factor in turn:

$$
f\prime(x)=2xe^x+(x^2+1)e^x=e^x(x^2+2x+1).
$$

The proposed $2xe^x$ omits $(x^2+1)e^x$, the term arising from differentiating $e^x$. At $x=0$, for example, the correct slope is 1, whereas the proposed expression gives zero.
