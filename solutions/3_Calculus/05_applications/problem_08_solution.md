# Exercise 8. Number of Requests Handled by a Server

## Question

The rate at which requests arrive at a server during the first 5 minutes is described by the function

$$
r(t)=100+20t\quad [\mathrm{requests/min}],\qquad 0\le t\le5.
$$

1. Compute the total number of requests that arrived during this time.
2. Compute the average rate of incoming requests over this interval.
3. Compare the average rate with the values $r(0)$ and $r(5)$.

## Solution

$$
R=\int_0^5(100+20t)\,dt=\left[100t+10t^2\right]_0^5=750.
$$

The total is 750 requests in this continuous rate model. The average rate is $750/5=150\,\mathrm{requests/min}$. The endpoint rates are $r(0)=100$ and $r(5)=200$; for this linear rate, their arithmetic mean is also 150. The trapezoid area $(100+200)5/2=750$ checks the integral.
