---
tags:
  - math
  - module-2
  - extended-part
  - binomial-theorem
  - foundation-knowledge
---

# The Binomial Theorem

## Binomial Expansion

For positive integer $n$:
$$
(a+b)^n = \sum_{r=0}^{n} \binom{n}{r} a^{\,n-r} b^{\,r}
$$

where the binomial coefficients are:
$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

## Summation Notation

$$
(a+b)^n = \sum_{r=0}^{n} \binom{n}{r} a^{\,n-r} b^{\,r}
$$

## Proof (by Induction)

**Base case $n=1$:** $(a+b)^1 = a + b = \binom{1}{0}a + \binom{1}{1}b$

**Assume true for $n=k$.** For $n=k+1$:
$$
\begin{aligned}
(a+b)^{k+1} &= (a+b)(a+b)^k \\
&= (a+b)\sum_{r=0}^{k} \binom{k}{r} a^{\,k-r} b^{\,r} \\
&= \sum_{r=0}^{k} \binom{k}{r} a^{\,k+1-r} b^{\,r} + \sum_{r=0}^{k} \binom{k}{r} a^{\,k-r} b^{\,r+1} \\
&= \binom{k}{0}a^{k+1} + \sum_{r=1}^{k} \left[\binom{k}{r} + \binom{k}{r-1}\right] a^{\,k+1-r} b^{\,r} + \binom{k}{k}b^{k+1}
\end{aligned}
$$

Using Pascal's identity $\binom{k}{r} + \binom{k}{r-1} = \binom{k+1}{r}$:
$$
(a+b)^{k+1} = \sum_{r=0}^{k+1} \binom{k+1}{r} a^{\,k+1-r} b^{\,r}
$$

## Pascal's Triangle

```
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
  1 5 10 10 5 1
```

Each entry is the sum of the two above it.

## Not Required

- Expansion of trinomials
- Greatest coefficient / greatest term
- Numerical approximation

## Related Topics

- [[Mathematical Induction]]
- [[More about Trigonometric Functions]]
