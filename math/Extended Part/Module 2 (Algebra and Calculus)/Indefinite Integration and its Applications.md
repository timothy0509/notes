---
tags:
  - math
  - module-2
  - extended-part
  - calculus
  - integration
---

# Indefinite Integration and its Applications

## Concept

Integration is the reverse process of differentiation:
$$
\frac{d}{dx}[F(x)] = f(x) \quad \Longrightarrow \quad \int f(x)\,dx = F(x) + C
$$

$C$ is the constant of integration.

## Basic Formulae

$$
\int k\,dx = kx + C
$$

$$
\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \quad (n \ne -1)
$$

$$
\int \frac{1}{x}\,dx = \ln|x| + C
$$

$$
\int e^x\,dx = e^x + C
$$

$$
\int \sin x\,dx = -\cos x + C
$$

$$
\int \cos x\,dx = \sin x + C
$$

$$
\int \sec^2 x\,dx = \tan x + C
$$

## Properties

$$
\int k f(x)\,dx = k \int f(x)\,dx
$$

$$
\int [f(x) \pm g(x)]\,dx = \int f(x)\,dx \pm \int g(x)\,dx
$$

## Integration by Substitution

Let $u = g(x)$, then $du = g'(x)\,dx$:
$$
\int f(g(x))\,g'(x)\,dx = \int f(u)\,du
$$

## Trigonometric Substitutions

| Expression | Substitution | Result |
|-----------|-------------|--------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $a\cos\theta$ |
| $\frac{1}{\sqrt{a^2 - x^2}}$ | $x = a\sin\theta$ | $\frac{1}{a}\sec\theta$ |
| $\frac{1}{x^2 + a^2}$ | $x = a\tan\theta$ | $\frac{1}{a}\sec^2\theta$ |

Results in terms of inverse trigonometric functions:
$$
\int \frac{1}{\sqrt{a^2 - x^2}}\,dx = \sin^{-1}\frac{x}{a} + C
$$

$$
\int \frac{1}{x^2 + a^2}\,dx = \frac{1}{a}\tan^{-1}\frac{x}{a} + C
$$

## Integration by Parts

$$
\int u\,dv = uv - \int v\,du
$$

Limited to at most **two** applications per integral.

Example: $\int \ln x\,dx = x\ln x - x + C$

## Notations

$\sin^{-1}x$, $\cos^{-1}x$, $\tan^{-1}x$ denote inverse trigonometric functions (principal values).

## Related Topics

- [[Differentiation]]
- [[Definite Integration]]
- [[Applications of Definite Integration]]
