# Exercise 5. The Classical Limit Leading to the Number $e$

The limit is $e\approx2.718281828$. To justify it, for $u>0$ integrate $1/(1+t)$ on $[0,u]$ to obtain $u/(1+u)\le\ln(1+u)\le u$. Setting $u=1/n$ gives

$$
\frac{n}{n+1}\le n\ln(1+1/n)\le1.
$$

Both bounds tend to 1, so continuity of the exponential gives $(1+1/n)^n\to e$.

| $n$ | $(1+1/n)^n$ (approximately) |
| --- | --- |
| 1 | 2.000000 |
| 10 | 2.593742 |
| 100 | 2.704814 |
| 1000 | 2.716924 |

The values support the result but only sample finitely many terms. The inequalities control every sufficiently large index and provide the proof.
