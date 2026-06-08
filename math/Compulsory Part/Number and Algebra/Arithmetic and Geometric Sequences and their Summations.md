---
tags:
  - math
  - compulsory-part
  - number-algebra
  - sequences
---

# Arithmetic and Geometric Sequences and their Summations

## Arithmetic Sequences
Common difference $d$: $T_{n+1} - T_n = d$.

General term:
$$T_n = a + (n-1)d$$

Properties:
- $T_n = \frac{1}{2}(T_{n-1} + T_{n+1})$
- If $T_1,T_2,T_3,\ldots$ is arithmetic, then $kT_1+a,kT_2+a,kT_3+a,\ldots$ is also arithmetic.

### Sum to $n$ Terms
$$S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}(a + \ell)$$
where $\ell = T_n$.

## Geometric Sequences
Common ratio $r$: $\dfrac{T_{n+1}}{T_n} = r$.

General term:
$$T_n = ar^{n-1}$$

Properties:
- $T_n^2 = T_{n-1} \times T_{n+1}$
- If $T_1,T_2,T_3,\ldots$ is geometric, then $kT_1,kT_2,kT_3,\ldots$ is also geometric.

### Sum to $n$ Terms
$$S_n = \frac{a(1-r^n)}{1-r} = \frac{a(r^n-1)}{r-1} \quad (r \neq 1)$$

### Sum to Infinity
For $|r| < 1$:
$$S_\infty = \frac{a}{1-r}$$

## Real-life Problems
- Interest (compound interest)
- Growth (population, bacteria)
- Depreciation (asset value over time)
