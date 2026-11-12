# Exercise 13. A Multi-Layer Composition

$$
x\longrightarrow x^2\longrightarrow\sin(x^2)\longrightarrow e^{\sin(x^2)}.
$$

Differentiate the outermost function first, evaluating its derivative at its input, and multiply by the derivative of that input. Repeating this procedure works back through the layers:

$$
f\prime(x)=e^{\sin(x^2)}\cos(x^2)\,2x.
$$

The three factors are respectively the derivatives of the exponential, sine, and square layers. At zero the result is zero, as expected from the even symmetry of the original function.
