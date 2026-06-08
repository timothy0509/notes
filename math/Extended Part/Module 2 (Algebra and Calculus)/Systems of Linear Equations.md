---
tags:
  - math
  - module-2
  - extended-part
  - algebra
  - linear-equations
---

# Systems of Linear Equations

## Cramer's Rule

For a system $A\mathbf{x} = \mathbf{b}$ with $\det A \ne 0$:

**2 variables:**
$$
x = \frac{\begin{vmatrix} b_1 & a_{12} \\ b_2 & a_{22} \end{vmatrix}}{\det A}, \qquad
y = \frac{\begin{vmatrix} a_{11} & b_1 \\ a_{21} & b_2 \end{vmatrix}}{\det A}
$$

**3 variables:**
$$
x = \frac{\det A_x}{\det A}, \quad
y = \frac{\det A_y}{\det A}, \quad
z = \frac{\det A_z}{\det A}
$$

where $A_x$ replaces the first column of $A$ with $\mathbf{b}$, etc.

## Inverse Matrix Method

$$
\mathbf{x} = A^{-1}\mathbf{b}
$$

(Requires $A$ to be invertible, i.e. $\det A \ne 0$.)

## Gaussian Elimination

1. Write the augmented matrix $[A \mid \mathbf{b}]$
2. Perform row operations to reach row-echelon form
3. Use back-substitution to solve

Row operations:
- Swap two rows
- Multiply a row by a non-zero constant
- Add a multiple of one row to another

## Homogeneous Systems

$A\mathbf{x} = \mathbf{0}$ always has the trivial solution $\mathbf{x} = \mathbf{0}$.

**Theorem:** A system of homogeneous linear equations has **nontrivial solutions** if and only if the coefficient matrix $A$ is **singular** ($\det A = 0$).

## Related Topics

- [[Determinants]]
- [[Matrices]]
