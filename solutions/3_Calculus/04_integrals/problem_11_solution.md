# Exercise 11. Choose the Method First

**1. Substitution:** the sine argument is linear. Put $u=3x$, $du=3\,dx$:

$$
\int\sin(3x)\,dx=-\frac13\cos(3x)+C.
$$

Its derivative is $\sin(3x)$.

**2. Integration by parts:** differentiating $\ln x$ produces $1/x$, which simplifies against a polynomial. For $x>0$, choose $u=\ln x$, $dv=x\,dx$:

$$
\int x\ln x\,dx=\frac{x^2}{2}\ln x-\int\frac x2\,dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}+C.
$$

The derivative is $x\ln x+x/2-x/2=x\ln x$.

**3. Substitution:** $u=x^2+1$, $du=2x\,dx$:

$$
\int\frac{x}{\sqrt{x^2+1}}\,dx=\frac12\int u^{-1/2}\,du=\sqrt{x^2+1}+C.
$$

Differentiation gives $x/\sqrt{x^2+1}$. The first and third integrands have domain $\mathbb R$.
