# Exercise 7. Choosing a Method Deliberately

**Case 1.** The coefficient matrix is triangular, so back substitution is sufficient: $4y=8$ gives $y=2$, then $2x-2=3$ gives $x=5/2$. These satisfy both original equations.

**Case 2.** Since $A^{-1}$ is already known, compute $x_i=A^{-1}b_i$ for each of the three right-hand sides. Reuse the same inverse; no additional inversion is needed. The identity $Ax_i=AA^{-1}b_i=b_i$ verifies each solution.

**Case 3.** Apply Gaussian elimination to $[A\mid b]$, then back substitute (or identify inconsistency or free variables if pivots are missing). Computing the full inverse would solve for all columns of an identity matrix unnecessarily when only one right-hand side is requested. If more right-hand sides appeared later, the coefficient elimination factors could be reused.
