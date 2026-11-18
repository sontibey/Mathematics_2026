# Exercise 15. Find the Error in the Monotonicity Analysis

## Question

For the function

$$
f(x)=x^3-3x
$$

the derivative was correctly computed as

$$
f'(x)=3(x-1)(x+1).
$$

However, a student wrote the following conclusion:

> The derivative is positive between its zeros and negative outside them. Therefore, the function is decreasing on $(-\infty,-1)\cup(1,\infty)$, increasing on $(-1,1)$, has a local minimum at $x=-1$, and a local maximum at $x=1$.

1. Without differentiating again, explain why merely identifying the zeros of the derivative does not justify the stated sign chart, and find the error in the student's reasoning.
2. Construct the correct sign chart for $f'(x)$.
3. Give the correct intervals of monotonicity and the character of the extrema.
4. In each of the three intervals, choose one simple test point and show that the sign of the derivative confirms your classification.

## Solution

The zeros of a derivative mark potential sign changes but do not determine the signs between them. The student reversed the sign of the product: outside the roots its two factors have the same sign, not opposite signs.

| Interval | Sign of $x-1$ | Sign of $x+1$ | Sign of $f\prime$ | Behavior |
| --- | --- | --- | --- | --- |
| $(-\infty,-1)$ | $-$ | $-$ | $+$ | Increasing |
| $(-1,1)$ | $-$ | $+$ | $-$ | Decreasing |
| $(1,\infty)$ | $+$ | $+$ | $+$ | Increasing |

The correct local maximum is $(-1,2)$ and local minimum is $(1,-2)$. Test points verify the chart: $f\prime(-2)=9>0$, $f\prime(0)=-3<0$, and $f\prime(2)=9>0$. No second differentiation is needed.
