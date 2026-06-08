---
tags:
  - math
  - module-2
  - extended-part
  - algebra
  - matrices
---

# Matrices

## Matrix Operations

### Addition

Matrices of the same dimensions: $(A + B)_{ij} = A_{ij} + B_{ij}$

### Scalar Multiplication

$(\lambda A)_{ij} = \lambda A_{ij}$

### Multiplication

$A$ ($m \times n$) and $B$ ($n \times p$):
$$
(AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
$$

## Properties

| Property | Formula |
|----------|---------|
| Commutative (addition) | $A + B = B + A$ |
| Associative (addition) | $A + (B + C) = (A + B) + C$ |
| Associative (multiplication) | $A(BC) = (AB)C$ |
| Distributive | $A(B + C) = AB + AC$, $(A + B)C = AC + BC$ |
| Scalar associativity | $(\lambda\mu)A = \lambda(\mu A)$ |
| Scalar distribution | $(\lambda + \mu)A = \lambda A + \mu A$, $\lambda(A + B) = \lambda A + \lambda B$ |
| Determinant of product | $|AB| = |A|\,|B|$ |

**Note:** Matrix multiplication is **not** commutative in general ($AB \ne BA$).

## Inverses of Square Matrices

A square matrix $A$ is invertible if there exists $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$.

### Order 2

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad
A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$

### Order 3

$A^{-1} = \frac{1}{\det A} \, \text{adj}(A)$, where $\text{adj}(A)$ is the adjugate (transpose of the cofactor matrix).

### Properties of Inverses

| Property | Formula |
|----------|---------|
| Uniqueness | The inverse of $A$ is unique |
| Inverse of inverse | $(A^{-1})^{-1} = A$ |
| Scalar | $(\lambda A)^{-1} = \lambda^{-1} A^{-1}$ |
| Power | $(A^n)^{-1} = (A^{-1})^n$ |
| Transpose | $(A^T)^{-1} = (A^{-1})^T$ |
| Determinant | $|A^{-1}| = |A|^{-1}$ |
| Product | $(AB)^{-1} = B^{-1} A^{-1}$ |

## Related Topics

- [[Determinants]]
- [[Systems of Linear Equations]]
