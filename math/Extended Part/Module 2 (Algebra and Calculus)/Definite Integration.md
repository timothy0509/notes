---
tags:
  - math
  - module-2
  - extended-part
  - calculus
  - integration
---

# Definite Integration

## Concept

The definite integral is defined as the limit of a sum of areas of rectangles under a curve:
$$
\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x
$$

## Dummy Variables

The variable of integration does not matter:
$$
\int_a^b f(x)\,dx = \int_a^b f(t)\,dt
$$

## Properties

| Property | Formula |
|----------|---------|
| Zero length | $\displaystyle\int_a^a f(x)\,dx = 0$ |
| Reversal | $\displaystyle\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$ |
| Additivity | $\displaystyle\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$ |
| Scalar multiple | $\displaystyle\int_a^b k f(x)\,dx = k\int_a^b f(x)\,dx$ |
| Sum/difference | $\displaystyle\int_a^b [f(x) \pm g(x)]\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx$ |
| Odd function | $\displaystyle\int_{-a}^{a} f(x)\,dx = 0$ if $f$ is odd |
| Even function | $\displaystyle\int_{-a}^{a} f(x)\,dx = 2\int_0^{a} f(x)\,dx$ if $f$ is even |

## Fundamental Theorem of Calculus

If $F'(x) = f(x)$, then:
$$
\int_a^b f(x)\,dx = F(b) - F(a)
$$

## Definite Integration by Substitution

Change the limits of integration along with the substitution:
$$
\int_{x=a}^{x=b} f(g(x))\,g'(x)\,dx = \int_{u=g(a)}^{u=g(b)} f(u)\,du
$$

## Definite Integration by Parts

$$
\int_a^b u\,dv = [uv]_a^b - \int_a^b v\,du
$$

Limited to at most **two** applications.

## Related Topics

- [[Indefinite Integration and its Applications]]
- [[Applications of Definite Integration]]
- [[Odd and Even Functions]]
