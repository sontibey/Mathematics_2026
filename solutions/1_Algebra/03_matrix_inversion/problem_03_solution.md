# Exercise 3. When Does the Inverse Not Exist?

## Question

For

$$
A=
\begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
$$

explain in two ways why $A^{-1}$ does not exist: using the determinant and using dependence between the rows.

## Solution

The determinant is $2(2)-4(1)=0$, so the inverse does not exist. Independently, $R_1=2R_2$, so the rows are dependent; the map cannot recover two independent input coordinates. For example, $A(-2,1)^T=0$, although $(-2,1)^T\ne0$. An inverse would imply $(-2,1)^T=A^{-1}0=0$, a contradiction.
