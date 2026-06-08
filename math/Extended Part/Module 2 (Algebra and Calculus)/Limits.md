---
tags:
  - math
  - module-2
  - extended-part
  - calculus
  - limits
---

# Limits

## Intuitive Concept

The limit of $f(x)$ as $x$ approaches $a$ is the value $L$ that $f(x)$ gets arbitrarily close to:
$$
\lim_{x \to a} f(x) = L
$$

## Limit Theorems

If $\lim_{x \to a} f(x) = L$ and $\lim_{x \to a} g(x) = M$, then:

| Operation | Result |
|-----------|--------|
| Sum | $\lim (f+g) = L + M$ |
| Difference | $\lim (f-g) = L - M$ |
| Product | $\lim (f \cdot g) = L \cdot M$ |
| Quotient | $\lim (f/g) = L/M$ ($M \ne 0$) |
| Scalar multiple | $\lim (k f) = kL$ |
| Composite | $\lim f(g(x)) = f(\lim g(x))$ |

## Important Limits

$$
\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1
$$

$$
\lim_{x \to 0} \frac{e^x - 1}{x} = 1
$$

## Limits at Infinity (Rational Functions)

For $\displaystyle \lim_{x \to \pm\infty} \frac{P(x)}{Q(x)}$ where $P,Q$ are polynomials:

| Degree comparison | Limit |
|-------------------|-------|
| $\deg P < \deg Q$ | $0$ |
| $\deg P = \deg Q$ | ratio of leading coefficients |
| $\deg P > \deg Q$ | $\pm\infty$ |

## Evaluating Limits

Techniques:
- Direct substitution
- Factorisation and cancellation
- Rationalisation
- Using the special limit $\frac{\sin\theta}{\theta} \to 1$
- Using the special limit $\frac{e^x - 1}{x} \to 1$

## Related Topics

- [[Differentiation]]
- [[More about Trigonometric Functions]]
- [[Introduction to e]]
