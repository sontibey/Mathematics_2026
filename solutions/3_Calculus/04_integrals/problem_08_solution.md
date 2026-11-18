# Exercise 8. Choosing the Factors in Integration by Parts

## Question

Compute

$$
\int x\cos x\,dx.
$$

Before calculating, justify why it is convenient to differentiate $x$ and integrate $\cos x$, rather than the other way around.

## Solution

Choose $u=x$ and $dv=\cos x\,dx$, so $du=dx$ and $v=\sin x$. Differentiating $x$ reduces its degree, while integrating cosine stays elementary. Reversing the choice would introduce $x^2$ and fail to simplify the remaining integral.

$$
\int x\cos x\,dx=x\sin x-\int\sin x\,dx=x\sin x+\cos x+C.
$$

Differentiating gives $\sin x+x\cos x-\sin x=x\cos x$.
