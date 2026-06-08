---
tags:
  - math
  - module-1
  - extended-part
  - calculus
  - integration
  - definite-integral
  - area
---

# Definite Integration and its Applications

## Concept

The definite integral is defined as the limit of a sum of areas of rectangles under a curve.

$$\int_a^b f(x)\,dx$$

Dummy variable: $\int_a^b f(x)\,dx = \int_a^b f(t)\,dt$.

## Fundamental Theorem of Calculus

$$\int_a^b f(x)\,dx = F(b) - F(a), \quad \text{where } \frac{d}{dx}F(x) = f(x)$$

## Properties

| Property | Formula |
|---|---|
| Zero length | $\int_a^a f(x)\,dx = 0$ |
| Reversal | $\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$ |
| Additivity | $\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$ |
| Scalar multiple | $\int_a^b k f(x)\,dx = k \int_a^b f(x)\,dx$ |
| Sum/Difference | $\int_a^b [f(x) \pm g(x)]\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx$ |

## Integration by Substitution (Definite)

$$\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$$

Change the limits when substituting.

## Area of Plane Figures

Area bounded by $y = f(x)$, the $x$-axis, $x = a$, $x = b$:

$$A = \int_a^b |f(x)|\,dx$$

When $f(x) \ge 0$ on $[a,b]$: $A = \int_a^b f(x)\,dx$.

**Not required:** area between curve and $y$-axis, area between two curves.

## Related

- [[Indefinite Integration and its Applications]]
- [[Approximation of Definite Integrals using the Trapezoidal Rule]]
