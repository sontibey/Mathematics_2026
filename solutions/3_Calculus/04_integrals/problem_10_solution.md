# Exercise 10. Definite Integral and Checking the Result

## Question

Before carrying out the exact calculation, estimate the possible range of values of the integral

$$
\int_0^2(x^2+1)\,dx,
$$

using

$$
1\le x^2+1\le5
$$

on $[0,2]$. Only then compute the integral exactly, compare the result with the earlier estimate, and explain what type of computational error such a check can detect.

## Solution

The integrand lies between 1 and 5 on an interval of length 2, so before integrating,

$$
2\le\int_0^2(x^2+1)\,dx\le10.
$$

The exact value is

$$
\left[\frac{x^3}{3}+x\right]_0^2=\frac83+2=\frac{14}3.
$$

This lies in $[2,10]$. The bound can detect an impossible negative result or a magnitude outside this interval, but cannot detect every error within it.
