---
tags:
  - math
  - compulsory-part
  - data-handling
  - probability
---

# More about Probability

## Set Language

| Notation               | Meaning                                   |
| ---------------------- | ----------------------------------------- |
| $A \cup B$             | Union — at least one of $A$ or $B$ occurs |
| $A \cap B$             | Intersection — both $A$ and $B$ occur     |
| $A'$ or $\overline{A}$ | Complement — $A$ does not occur           |

## Venn Diagrams

Used to visualise relationships between events and their probabilities.

## Addition Law

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

### Mutually Exclusive Events

If $A$ and $B$ cannot occur together: $P(A \cap B) = 0$

$$
P(A \cup B) = P(A) + P(B)
$$

### Complementary Events

$$
P(A') = 1 - P(A)
$$

## Multiplication Law

For **independent** events:
$$
P(A \cap B) = P(A) \times P(B)
$$

Events $A$ and $B$ are independent if the occurrence of one does not affect the probability of the other.

## Conditional Probability

$$
P(A \cap B) = P(A) \times P(B \mid A)
$$

where $P(B \mid A)$ is the probability of $B$ given $A$ has occurred.

Bayes' Theorem is not required.

## Using Permutations and Combinations

Probability problems can be solved by counting outcomes using [[Permutations and Combinations]]:

$$
P(\text{event}) = \frac{\text{number of favourable outcomes}}{\text{total number of possible outcomes}}
$$

Count the numerator and denominator using $nPr$ or $nCr$ as appropriate.
