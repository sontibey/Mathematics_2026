# Exercise 11. An n-th Root

$$
\sqrt[n]{5^n+2^n}=5\left(1+(2/5)^n\right)^{1/n}.
$$

Since $1\le1+(2/5)^n\le2$, the last factor lies between 1 and $2^{1/n}$, both tending to 1. Thus the limit is 5. The dominant term is exponential, so factor $5^n$ inside the root; the root turns it into 5. Dividing by a power of $n$ would not capture this growth.
