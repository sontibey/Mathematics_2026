# Exercise 6. A System with a Parameter — Which Cases Actually Occur?

## Question

Analyze, depending on the parameter $a$, the system

$$
\begin{cases}
x+y=2, \\
ax+ay=4.
\end{cases}
$$

Among the three possibilities — exactly one solution, infinitely many solutions, no solution — determine which actually occur and for which values of $a$. If one type cannot occur, explain why.

## Solution

Eliminating with $R_2\leftarrow R_2-aR_1$ gives $0=4-2a$. If $a=2$, the second equation repeats the first and all solutions are $(x,y)=(2-s,s)$, with $s\in\mathbb R$. If $a\ne2$, the remaining equation is a contradiction, so there are no solutions. Exactly one solution never occurs: the coefficient rows are always dependent, leaving at most one independent equation for two unknowns.
