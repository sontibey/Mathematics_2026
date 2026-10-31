# Exercise 14. Rotation Matrices

Row–column multiplication gives

$$
R(\alpha)R(\beta)=\begin{pmatrix}
\cos\alpha\cos\beta-\sin\alpha\sin\beta & -\cos\alpha\sin\beta-\sin\alpha\cos\beta \\
\sin\alpha\cos\beta+\cos\alpha\sin\beta & -\sin\alpha\sin\beta+\cos\alpha\cos\beta \\
\end{pmatrix}.
$$

Using the angle-sum identities, this becomes

$$
\begin{pmatrix}
\cos(\alpha+\beta) & -\sin(\alpha+\beta) \\
\sin(\alpha+\beta) & \cos(\alpha+\beta) \\
\end{pmatrix}=R(\alpha+\beta).
$$

Geometrically, rotating a vector by $\beta$ and then by $\alpha$, about the same origin, adds the angles and preserves length. As a check, setting $\beta=-\alpha$ gives $R(0)=I$.
