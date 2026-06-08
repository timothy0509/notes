---
tags:
  - math
  - module-2
  - extended-part
  - algebra
  - determinants
---

# Determinants

## Determinant of Order 2

For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
$$
|A| = \det A = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
$$

## Determinant of Order 3

For $A = \begin{pmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{pmatrix}$:

**First row expansion:**
$$
|A| = a_1 \begin{vmatrix} b_2 & c_2 \\ b_3 & c_3 \end{vmatrix} - b_1 \begin{vmatrix} a_2 & c_2 \\ a_3 & c_3 \end{vmatrix} + c_1 \begin{vmatrix} a_2 & b_2 \\ a_3 & b_3 \end{vmatrix}
$$

Equivalently (Sarrus's rule):
$$
\det A = a_1 b_2 c_3 + b_1 c_2 a_3 + c_1 a_2 b_3 - c_1 b_2 a_3 - a_1 c_2 b_3 - b_1 a_2 c_3
$$

## Notations

- $|A|$ — determinant of matrix $A$
- $\det A$ — alternative notation

## Related Topics

- [[Matrices]]
- [[Systems of Linear Equations]]
