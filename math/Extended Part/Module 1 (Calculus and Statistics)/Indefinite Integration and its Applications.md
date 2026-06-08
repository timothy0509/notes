---
tags:
  - math
  - module-1
  - extended-part
  - calculus
  - integration
  - indefinite-integral
---

# Indefinite Integration and its Applications

## Concept

Indefinite integration is the reverse process of differentiation.

$$\int f(x)\,dx = F(x) + C \quad \Longleftrightarrow \quad \frac{d}{dx}F(x) = f(x)$$

$C$ is the **constant of integration**.

## Properties

| Property | Formula |
|---|---|
| Scalar multiple | $\int k f(x)\,dx = k \int f(x)\,dx$ |
| Sum/Difference | $\int [f(x) \pm g(x)]\,dx = \int f(x)\,dx \pm \int g(x)\,dx$ |

## Basic Integration Formulae

| Derivative | Integral |
|---|---|
| $k$ | $\int k\,dx = kx + C$ |
| $x^n \;(n \neq -1)$ | $\int x^n\,dx = \dfrac{x^{n+1}}{n+1} + C$ |
| $\dfrac{1}{x}$ | $\int \dfrac{1}{x}\,dx = \ln|x| + C$ |
| $e^x$ | $\int e^x\,dx = e^x + C$ |

## Integration by Substitution

Let $u = g(x)$, then $du = g'(x)\,dx$:

$$\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$$

Integration by parts is **not required**.

## Related

- [[Differentiation of a Function]]
- [[Definite Integration and its Applications]]
