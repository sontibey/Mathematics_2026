# Exercise 3. When Can Matrices Be Multiplied?

## Question

The matrix sizes are

$$
A_{2\times3},\qquad B_{3\times4},\qquad C_{4\times2},\qquad D_{2\times2}.
$$

For the products

$$
AB,\ BA,\ BC,\ CB,\ AC,\ CA,\ AD,\ DA
$$

determine whether they are defined. If so, state the size of the result. Justify each decision using the dimension compatibility condition.

## Solution

The product of an $m\times n$ matrix and a $p\times q$ matrix is defined exactly when $n=p$; its size is then $m\times q$.

| Product | Inner dimensions | Defined? | Result size |
| --- | --- | --- | --- |
| $AB$ | $3=3$ | Yes | $2\times4$ |
| $BA$ | $4\ne2$ | No | — |
| $BC$ | $4=4$ | Yes | $3\times2$ |
| $CB$ | $2\ne3$ | No | — |
| $AC$ | $3\ne4$ | No | — |
| $CA$ | $2=2$ | Yes | $4\times3$ |
| $AD$ | $3\ne2$ | No | — |
| $DA$ | $2=2$ | Yes | $2\times3$ |
