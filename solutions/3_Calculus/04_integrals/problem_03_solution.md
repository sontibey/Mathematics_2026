# Exercise 3. Recognizing Basic Antiderivatives

## Question

Compute

$$
\int\left(2e^x+3\cos x-4\sin x\right)\,dx.
$$

Match each term with a known derivative and verify the entire result with one differentiation.

## Solution

The integrand is a sum, so it is enough to find a function for each summand whose derivative returns that summand. The exponential is unchanged by differentiation, and the sine–cosine derivative pair determines the signs:

| Required derivative | Candidate term | Reason |
| --- | --- | --- |
| $2e^x$ | $2e^x$ | $(e^x)'=e^x$ |
| $3\cos x$ | $3\sin x$ | $(\sin x)'=\cos x$ |
| $-4\sin x$ | $4\cos x$ | $(\cos x)'=-\sin x$ |

Thus the family of antiderivatives on $\mathbb R$ is

$$
2e^x+3\sin x+4\cos x+C,\qquad C\in\mathbb R.
$$

One differentiation verifies the whole expression:

$$
\frac{d}{dx}\left(2e^x+3\sin x+4\cos x+C\right)
=2e^x+3\cos x-4\sin x.
$$

The cosine term in the answer has a positive coefficient; its derivative supplies the negative sign required by the original integrand. Only one arbitrary constant is necessary because any constants from separately integrated terms combine into a single constant.
