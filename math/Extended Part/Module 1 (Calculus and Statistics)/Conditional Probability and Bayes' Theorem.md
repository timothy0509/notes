---
tags:
  - math
  - module-1
  - extended-part
  - statistics
  - probability
  - conditional-probability
  - bayes
---

# Conditional Probability and Bayes' Theorem

## Conditional Probability

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

$P(A|B)$ is the probability of $A$ occurring given $B$ has occurred.

## Multiplication Rule

$$P(A \cap B) = P(A) \cdot P(B|A) = P(B) \cdot P(A|B)$$

## Bayes' Theorem

For a partition $B_1, B_2, \ldots, B_n$ of the sample space:

$$P(B_i|A) = \frac{P(A|B_i)\,P(B_i)}{\sum_{j=1}^n P(A|B_j)\,P(B_j)}$$

### Simple Form (two events)

$$P(B|A) = \frac{P(A|B)\,P(B)}{P(A)}$$

## Related

- [[Discrete Random Variables]]
- [[Probability Distribution, Expectation and Variance]]
- [[More about Probability (CP)]]
