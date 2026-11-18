# Exercise 14. Rotation Matrices

## Question

The matrix for a rotation through an angle $\theta$ is

$$
R(\theta)=
\begin{pmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta \\
\end{pmatrix}.
$$

Compute $R(\alpha)R(\beta)$ and, using the angle-sum formulas for sine and cosine, show that

$$
R(\alpha)R(\beta)=R(\alpha+\beta).
$$

Explain the result geometrically.

## Solution

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
