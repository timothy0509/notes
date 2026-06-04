---
tags:
  - ict
  - elective
  - algorithms
  - numerical-errors
aliases:
  - Program Errors
  - Numerical Errors
  - Data Structures
  - Elective C
---

# Program Errors and Data Structures

## Chapter 2: Types of Program Errors

### Overflow Errors

When a number is stored in a variable, if the number exceeds the range of values that can be stored in the data type of the variable, then an **overflow error** occurs.

If the number is lower than the range of values, then an **underflow error** occurs.

> [!tip] Calculation of Overflow Errors
> Two's complement representation, which is mentioned in [[A2|Compulsory A 3.1]].

### Numerical Errors

#### Truncation Errors

**Truncation error** refers to the difference between the true value and the value stored.

$$
\text{Truncation error} = |\text{True value}-\text{Actual value stored}|
$$

#### Rounding Errors

**Rounding error** means the difference between the true value and the rounded value.

$$
\text{Rounding error}=|\text{True value}-\text{Rounded value}|
$$

> [!info] Other Errors
> These errors are mentioned in [[D|Compulsory D 6.2]]:
> - **Syntax errors**
> - **Logical errors**
> - **Run-time errors**
>   - Dividing a number by zero
>   - Calculating the square root of a negative number
>   - Accessing an item outside the range of the array index

---

## Chapter 4: Subprograms

```python
def sum(n1, n2):   # Defining a sub-program
    sum = n1 + n2
    return sum

print(sum(1, 2))   # Calling a sub-program
```

> [!tip] Benefits of Modularisation
> 1. Easy to understand
> 2. Facilitate reuse
> 3. Enhance development efficiency

---

## Chapter 5: Data Structures

### Stacks

==First in, last out== (FILO).

### Queues

==First in, first out== (FIFO).

#### Circular Queue

More efficient to run in limited memory.

### Linear Linked List

A sequence of elements where each element points to the next.

---

## Related

- [[ICT Index]] - Subject overview
- [[A2]] - Data validation (two's complement reference)
- [[D]] - Programming basics and errors
