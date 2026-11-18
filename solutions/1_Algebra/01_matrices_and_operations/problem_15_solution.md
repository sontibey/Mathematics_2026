# Exercise 15. Associativity and Calculation Paths

## Question

Given

$$
A=
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix},\quad B=
\begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix},\quad C=
\begin{pmatrix}
2 & 1 \\
0 & -1 \\
\end{pmatrix}.
$$

Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

## Solution

For the first calculation path,

$$
AB=\begin{pmatrix}
5 & 2 \\
1 & 4 \\
\end{pmatrix},\qquad (AB)C=\begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}.
$$

For the second path,

$$
BC=\begin{pmatrix}
2 & 1 \\
4 & 1 \\
-2 & -4 \\
\end{pmatrix},\qquad A(BC)=\begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}.
$$

Thus $(AB)C=A(BC)$. Associativity permits regrouping a product without changing the order of its factors.

For ordinary dense multiplication, counting every scalar multiplication and addition (including operations with zeros):

| Path | First product | Second product | Total |
| --- | --- | --- | --- |
| $(AB)C$ | 12 multiplications, 8 additions | 8 multiplications, 4 additions | 20 multiplications, 12 additions |
| $A(BC)$ | 12 multiplications, 6 additions | 12 multiplications, 8 additions | 24 multiplications, 14 additions |

The first grouping uses 6 fewer scalar operations under this convention. This follows from the rule that an $m\times n$ by $n\times p$ product uses $mnp$ multiplications and $mp(n-1)$ additions. Exploiting zeros or ones can reduce the actual work, so the counting convention matters.
