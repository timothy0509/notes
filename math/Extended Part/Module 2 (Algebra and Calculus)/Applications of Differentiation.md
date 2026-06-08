---
tags:
  - math
  - module-2
  - extended-part
  - calculus
  - differentiation
  - applications
---

# Applications of Differentiation

## Equation of Tangents

The slope of the tangent to $y = f(x)$ at $x = a$ is $f'(a)$. The equation of the tangent line is:
$$
y - f(a) = f'(a)(x - a)
$$

## Maxima and Minima

| Type | Condition |
|------|-----------|
| **Local maximum** | $f'(c) = 0$ and $f'(x)$ changes $+$ to $-$ at $c$ |
| **Local minimum** | $f'(c) = 0$ and $f'(x)$ changes $-$ to $+$ at $c$ |
| **Global maximum/minimum** | Largest/smallest value over the entire domain (check endpoints) |

**Second Derivative Test:**
- $f'(c) = 0$, $f''(c) < 0$ → local max
- $f'(c) = 0$, $f''(c) > 0$ → local min

## Curve Sketching

Consider the following for polynomial and rational functions:

| Feature | How to Find |
|---------|-------------|
| Symmetry | Check $f(-x) = f(x)$ (even) or $f(-x) = -f(x)$ (odd) |
| $x$-intercepts | Solve $f(x) = 0$ |
| $y$-intercept | $f(0)$ |
| Max/min points | $f'(x) = 0$ |
| Points of inflection | $f''(x) = 0$ |
| Vertical asymptote | Denominator $= 0$ |
| Horizontal asymptote | $\lim_{x \to \pm\infty} f(x)$ |
| Oblique asymptote | Occurs when $\deg P = \deg Q + 1$ for rational functions; divide to find linear asymptote |

## Rate of Change

If $y = f(x)$ and both $x$ and $y$ change with time $t$:
$$
\frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt}
$$

Solve related rates problems by:
1. Identify the given rate and the desired rate
2. Write an equation relating the variables
3. Differentiate implicitly with respect to $t$
4. Substitute known values

## Related Topics

- [[Differentiation]]
- [[Indefinite Integration and its Applications]]
