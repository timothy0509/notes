---
tags:
  - math
  - module-1
  - extended-part
  - calculus
  - derivative
  - limits
---

# Derivative of a Function

## Intuitive Concept of Limits

$\lim_{x\to a} f(x) = L$ means $f(x)$ approaches $L$ as $x$ approaches $a$.

## Limit Theorems

| Theorem | Expression |
|---|---|
| Sum | $\lim(f+g) = \lim f + \lim g$ |
| Difference | $\lim(f-g) = \lim f - \lim g$ |
| Product | $\lim(f \cdot g) = \lim f \cdot \lim g$ |
| Quotient | $\lim(f/g) = \lim f / \lim g$, $\lim g \neq 0$ |
| Scalar multiple | $\lim(kf) = k \lim f$ |
| Composite | $\lim f(g(x)) = f(\lim g(x))$ |

## Limits of Common Functions

- $\lim_{x\to a} x^n = a^n$
- $\lim_{x\to a} e^x = e^a$
- $\lim_{x\to a} \ln x = \ln a$, $a > 0$

## Definition of Derivative

The derivative of $f$ at $x$ is the slope of the tangent to $y = f(x)$ at that point:

$$f'(x) = \lim_{h\to 0} \frac{f(x+h) - f(x)}{h}$$

(First principles not required for this module.)

## Notations

$$y', \quad f'(x), \quad \frac{dy}{dx}, \quad \left.\frac{dy}{dx}\right|_{x=x_0}$$

## Slope of Tangent

The slope of the tangent to $y = f(x)$ at $x = x_0$ is $f'(x_0)$ (or $\frac{dy}{dx}\big|_{x=x_0}$).

## Related

- [[Differentiation of a Function]]
- [[Exponential and Logarithmic Functions]]
- [[Second Derivative]]
