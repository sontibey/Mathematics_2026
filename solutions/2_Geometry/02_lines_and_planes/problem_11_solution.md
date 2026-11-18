# Exercise 11. Plane Containing a Line and a Point

## Question

Find the equation of the plane containing

$$
(x,y,z)=(1,0,2)+t(1,1,-1)
$$

and the point $P=(0,2,1)$. Check that both the entire line and the point lie in the plane you obtain.

## Solution

Use the line direction $v=(1,1,-1)$ and the displacement from its base point to $P$, namely $w=(-1,2,-1)$. Their cross product is $n=v\times w=(1,2,3)\ne0$. The plane is

$$
(x-1)+2y+3(z-2)=0,\qquad x+2y+3z=7.
$$

The point $P$ gives $0+4+3=7$. A general line point gives $(1+t)+2t+3(2-t)=7$, so the entire line is contained. The nonzero cross product ensures a unique plane.
