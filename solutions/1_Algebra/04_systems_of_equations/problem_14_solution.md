# Exercise 14. A Small Change in the Right-Hand Side

## Question

Compare the systems

$$
\begin{cases}
x+y=2, \\
2x-y=1, \\
3x=3
\end{cases}
$$

and

$$
\begin{cases}
x+y=2, \\
2x-y=1, \\
3x=3.1.
\end{cases}
$$

Check the consistency of each system and explain why a small change in one number can change the type of the system.

## Solution

Adding the first two equations gives $3x=3$, so $x=1$ and $y=1$. The third equation of the first system repeats this consequence, giving the unique solution $(1,1)$. In the second system the first two equations still force $3x=3$, but the third requires $3x=3.1$. Subtracting produces $0=0.1$, so it is inconsistent. Even a small nonzero perturbation destroys an exact dependence between the three equations.
