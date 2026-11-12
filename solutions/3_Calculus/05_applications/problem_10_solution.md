# Exercise 10. A Cable Through Water and Land

Assume straight parallel banks and a straight underwater segment from $A$ to an exit point on the opposite bank, followed by cable along that bank to $B$. Let $x$ be the exit displacement toward $B$ from the point directly opposite $A$, in meters, and let $c>0$ be the land cost per meter. For exits between those two points, $0\le x\le500$,

$$
C(x)=c\left(2\sqrt{100^2+x^2}+500-x\right).
$$

$$
C\prime(x)=c\left(\frac{2x}{\sqrt{10000+x^2}}-1\right)=0\quad\Longleftrightarrow\quad x=\frac{100}{\sqrt3}.
$$

The derivative changes from negative to positive, and $C\prime\prime(x)=20000c/(10000+x^2)^{3/2}>0$, so the optimum is $x\approx57.735$ m. The underwater length is $200/\sqrt3\approx115.470$ m and land length is $500-100/\sqrt3\approx442.265$ m. The minimum cost is $c(500+100\sqrt3)\approx673.205c$.

Allowing arbitrary exit locations gives the full cost $c(2\sqrt{10000+x^2}+|500-x|)$ for $x\in\mathbb R$. For $x<0$ it decreases toward the interval, and for $x>500$ it increases, so no exterior exit improves the solution. This justifies restricting the search to $[0,500]$.
