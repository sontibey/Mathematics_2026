# Exercise 2. Maximum Area of a Rectangle

Let the side lengths be $x$ and $y$ in consistent length units. The perimeter constraint $2x+2y=40$ gives $y=20-x$, so

$$
A(x)=x(20-x),\qquad 0<x<20.
$$

Then $A\prime(x)=20-2x=0$ gives $x=10$, and $A\prime\prime(x)=-2<0$ proves the unique global maximum. The dimensions are $10\times10$, with area 100 square units. Equivalently, $A(x)=100-(x-10)^2\le100$, and the limiting degenerate endpoints give zero area.
