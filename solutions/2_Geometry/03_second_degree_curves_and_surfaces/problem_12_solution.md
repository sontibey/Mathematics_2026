# Exercise 12. Recognizing a Surface from Cross-Sections

## Question

A certain surface has the following properties:
- the cross-section $z=0$ is a point,
- for $z>0$, the cross-sections $z=\mathrm{const}$ are circles with increasing radius,
- vertical cross-sections through the $Oz$ axis are parabolas.

Propose a simple equation for such a surface and justify your choice.

## Solution

A simple model is $z=x^2+y^2$. At $z=0$, nonnegative squares force $x=y=0$. At $z=c>0$, the section is $x^2+y^2=c$, a circle of increasing radius $\sqrt c$. In any vertical plane through the $z$-axis, write $(x,y)=(r\cos\theta,r\sin\theta)$ with signed $r$; substitution gives $z=r^2$, a parabola. Thus all stated properties hold. The information permits other scales, but this is the simplest choice.
