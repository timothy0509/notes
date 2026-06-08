---
tags:
  - math
  - module-2
  - extended-part
  - algebra
  - vectors
---

# Scalar Product and Vector Product

## Scalar (Dot) Product

### Definition

$$
\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos\theta
$$

In components ($\mathbb{R}^2$ or $\mathbb{R}^3$):
$$
\mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3
$$

### Properties

| Property | Formula |
|----------|---------|
| Commutative | $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$ |
| Scalar associativity | $(\lambda\mathbf{a}) \cdot \mathbf{b} = \lambda(\mathbf{a} \cdot \mathbf{b})$ |
| Distributive | $\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}$ |
| Norm | $|\mathbf{a}|^2 = \mathbf{a} \cdot \mathbf{a} \ge 0$ |
| Zero | $\mathbf{a} \cdot \mathbf{a} = 0 \iff \mathbf{a} = \mathbf{0}$ |
| Cauchy-Schwarz | $|\mathbf{a} \cdot \mathbf{b}| \le |\mathbf{a}| |\mathbf{b}|$ |
| Law of cosines | $|\mathbf{a} - \mathbf{b}|^2 = |\mathbf{a}|^2 + |\mathbf{b}|^2 - 2(\mathbf{a} \cdot \mathbf{b})$ |

## Vector (Cross) Product

### Definition ($\mathbb{R}^3$ only)

$$
\mathbf{a} \times \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \sin\theta \; \mathbf{n}
$$

where $\mathbf{n}$ is a unit vector perpendicular to both $\mathbf{a}$ and $\mathbf{b}$, following the right-hand rule.

In components:
$$
\mathbf{a} \times \mathbf{b} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
$$

### Properties

| Property | Formula |
|----------|---------|
| Self-cross | $\mathbf{a} \times \mathbf{a} = \mathbf{0}$ |
| Anti-commutative | $\mathbf{b} \times \mathbf{a} = -(\mathbf{a} \times \mathbf{b})$ |
| Distributive | $(\mathbf{a} + \mathbf{b}) \times \mathbf{c} = \mathbf{a} \times \mathbf{c} + \mathbf{b} \times \mathbf{c}$, $\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}$ |
| Scalar | $(\lambda\mathbf{a}) \times \mathbf{b} = \lambda(\mathbf{a} \times \mathbf{b}) = \mathbf{a} \times (\lambda\mathbf{b})$ |
| Lagrange identity | $|\mathbf{a} \times \mathbf{b}|^2 = |\mathbf{a}|^2 |\mathbf{b}|^2 - (\mathbf{a} \cdot \mathbf{b})^2$ |

## Related Topics

- [[Introduction to Vectors]]
- [[Applications of Vectors]]
