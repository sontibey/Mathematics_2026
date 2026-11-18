# Exercise 7. Choosing a Method Deliberately

## Question

Do not solve all of the following systems completely. For each situation, choose the method that best uses its structure and justify your choice:

1. one system with a triangular coefficient matrix

$$
\begin{cases}
2x-y=3, \\
4y=8;
\end{cases}
$$

2. three systems $Ax=b_i$ with the same invertible matrix $A$, when $A^{-1}$ is already known;
3. one $3\times3$ system for which the inverse matrix is not given and the goal is only to find one solution vector.

For case 1, carry out the chosen method completely. For cases 2 and 3, describe the plan and indicate which part of the computation would be reusable or unnecessary. Do not judge a method by its name alone — refer to the number of right-hand sides and the structure of the matrix.

## Solution

**Case 1.** The coefficient matrix is triangular, so back substitution is sufficient: $4y=8$ gives $y=2$, then $2x-2=3$ gives $x=5/2$. These satisfy both original equations.

**Case 2.** Since $A^{-1}$ is already known, compute $x_i=A^{-1}b_i$ for each of the three right-hand sides. Reuse the same inverse; no additional inversion is needed. The identity $Ax_i=AA^{-1}b_i=b_i$ verifies each solution.

**Case 3.** Apply Gaussian elimination to $[A\mid b]$, then back substitute (or identify inconsistency or free variables if pivots are missing). Computing the full inverse would solve for all columns of an identity matrix unnecessarily when only one right-hand side is requested. If more right-hand sides appeared later, the coefficient elimination factors could be reused.
