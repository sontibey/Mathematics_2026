# Exercise 9. Minimizing the Material Used for a Can

For fixed volume $V>0$, let $r>0$ be the radius and $h>0$ the height. The constraint is $\pi r^2h=V$, so $h=V/(\pi r^2)$. A closed cylinder has two circular ends, giving

$$
S(r)=2\pi r^2+2\pi rh=2\pi r^2+\frac{2V}{r},\qquad r>0.
$$

$$
S\prime(r)=4\pi r-\frac{2V}{r^2}=0\quad\Longleftrightarrow\quad r^3=\frac{V}{2\pi}.
$$

Since $S\prime\prime(r)=4\pi+4V/r^3>0$ and $S\to\infty$ as $r\to0^+$ or $r\to\infty$, this is the unique global minimum. The volume constraint then gives $h=2r$: the optimal height equals the diameter.
