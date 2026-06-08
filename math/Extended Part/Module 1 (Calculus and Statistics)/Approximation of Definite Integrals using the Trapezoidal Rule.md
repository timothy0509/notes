---
tags:
  - math
  - module-1
  - extended-part
  - calculus
  - integration
  - trapezoidal-rule
  - approximation
---

# Approximation of Definite Integrals using the Trapezoidal Rule

## Trapezoidal Rule

Divide $[a,b]$ into $n$ equal subintervals of width $h = \frac{b-a}{n}$:

$$\int_a^b f(x)\,dx \approx \frac{h}{2}\big[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\big]$$

where $x_i = a + ih$ for $i = 0, 1, 2, \ldots, n$.

## Over-estimate / Under-estimate

Use the [[Second Derivative]] and concavity:

| Concavity of $f$ on $[a,b]$ | Approximation |
|---|---|
| Concave up ($f''(x) > 0$) | **Over-estimate** |
| Concave down ($f''(x) < 0$) | **Under-estimate** |

## Notes

- Error estimation is **not required**
- More subintervals $\implies$ better approximation

## Related

- [[Definite Integration and its Applications]]
