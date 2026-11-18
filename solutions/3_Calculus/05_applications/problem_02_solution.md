# Exercise 2. Maximum Area of a Rectangle

## Question

A rectangle has perimeter $40$.

1. Write its area as a function of the length of one side.
2. Determine the domain of this function resulting from the geometry of the problem.
3. Find the dimensions that give the maximum area.
4. Justify that the point found actually gives a maximum.

## Solution

Let the side lengths be $x$ and $y$ in consistent length units. The perimeter constraint $2x+2y=40$ gives $y=20-x$, so

$$
A(x)=x(20-x),\qquad 0<x<20.
$$

Then $A\prime(x)=20-2x=0$ gives $x=10$, and $A\prime\prime(x)=-2<0$ proves the unique global maximum. The dimensions are $10\times10$, with area 100 square units. Equivalently, $A(x)=100-(x-10)^2\le100$, and the limiting degenerate endpoints give zero area.
