---
tags:
  - math
  - module-2
  - extended-part
  - algebra
  - vectors
---

# Introduction to Vectors

## Scalars vs Vectors

- **Scalar**: a quantity with magnitude only (e.g. mass, temperature)
- **Vector**: a quantity with both magnitude and direction (e.g. displacement, velocity)

## Notation

| Form | Example |
|------|---------|
| Bold lowercase | $\mathbf{a}$ |
| Arrow | $\vec{a}$ or $\overrightarrow{AB}$ |
| Components | $\begin{pmatrix} x \\ y \end{pmatrix}$ or $\begin{pmatrix} x \\ y \\ z \end{pmatrix}$ |

## Magnitude

In $\mathbb{R}^2$: $|\mathbf{a}| = \sqrt{x^2 + y^2}$

In $\mathbb{R}^3$: $|\mathbf{a}| = \sqrt{x^2 + y^2 + z^2}$

## Special Vectors

- **Zero vector**: $\mathbf{0}$ (magnitude $0$, no direction)
- **Unit vector**: $|\hat{\mathbf{a}}| = 1$; $\hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|}$

## Vector Operations

### Addition

$\mathbf{a} + \mathbf{b}$ (parallelogram law / tip-to-tail)

### Subtraction

$\mathbf{a} - \mathbf{b} = \mathbf{a} + (-\mathbf{b})$

### Scalar Multiplication

$\lambda \mathbf{a}$ scales the magnitude by $|\lambda|$; reverses direction if $\lambda < 0$.

## Properties

| Property | Formula |
|----------|---------|
| Commutative | $\mathbf{a} + \mathbf{b} = \mathbf{b} + \mathbf{a}$ |
| Associative | $\mathbf{a} + (\mathbf{b} + \mathbf{c}) = (\mathbf{a} + \mathbf{b}) + \mathbf{c}$ |
| Identity | $\mathbf{a} + \mathbf{0} = \mathbf{a}$ |
| Zero scalar | $0\mathbf{a} = \mathbf{0}$ |
| Scalar associativity | $\lambda(\mu\mathbf{a}) = (\lambda\mu)\mathbf{a}$ |
| Scalar distributivity | $(\lambda + \mu)\mathbf{a} = \lambda\mathbf{a} + \mu\mathbf{a}$, $\lambda(\mathbf{a} + \mathbf{b}) = \lambda\mathbf{a} + \lambda\mathbf{b}$ |
| Linear independence | If $\alpha\mathbf{a} + \beta\mathbf{b} = \alpha'\mathbf{a} + \beta'\mathbf{b}$ with $\mathbf{a},\mathbf{b}$ non-zero and non-parallel, then $\alpha = \alpha'$, $\beta = \beta'$ |

## Rectangular Coordinate System

In $\mathbb{R}^2$: $\mathbf{a} = \begin{pmatrix} x \\ y \end{pmatrix} = x\mathbf{i} + y\mathbf{j}$

In $\mathbb{R}^3$: $\mathbf{a} = \begin{pmatrix} x \\ y \\ z \end{pmatrix} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$

Direction of $\mathbf{a}$ in $\mathbb{R}^2$: $\cos\theta = \frac{x}{\sqrt{x^2 + y^2}}$, $\sin\theta = \frac{y}{\sqrt{x^2 + y^2}}$

## Related Topics

- [[Scalar Product and Vector Product]]
- [[Applications of Vectors]]
