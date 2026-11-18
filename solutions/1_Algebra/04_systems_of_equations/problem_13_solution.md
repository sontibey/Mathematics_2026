# Exercise 13. Does Every Equation Add New Information?

## Question

Consider the system

$$
x_1+x_2=10,\qquad x_2+x_3=8,\qquad x_1-x_3=2.
$$

Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

## Solution

Subtract the second equation from the first to obtain $x_1-x_3=10-8=2$. Thus the third equation adds no information. Let $x_2=s$; then

$$
(x_1,x_2,x_3)=(10-s,s,8-s),\qquad s\in\mathbb R.
$$

The first two equations are independent; neither follows from the other. The third is redundant, and substitution verifies all three for every $s$.
