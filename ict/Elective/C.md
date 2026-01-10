## Chapter 2
### Types of program errors
#### Overflow errors
When a number is stored in a variable, if the number exceeds the range of values that can be stored in the data type of the variable, then an **overflow error** occurs.
If the number is lower than the range of values, then an **underflow error** occurs.

> [!hint] Calculation of overflow errors
> Two's complement representation, which is mentioned in Compulsory A 3.1.

#### Numerical Errors
##### Truncation errors
**Truncation error** refers to the difference between the true value and the value stored.
$$
\text{Truncation error} = |\text{True value}-\text{Actual value stored}|
$$
##### Rounding errors
**Rounding error** means the difference between the true value and the rounded value.
$$
\text{Rounding error}=|\text{True value}-\text{Rounded value}|
$$
> [!info] Other errors
> These errors are mentioned in Compulsory D 6.2.
> - **Syntax errors**
> - **Logical errors**
> - **Run-time errors**
> 	- Dividing a number by zero
> 	- Calculating the square root of a negative number
> 	- Accessing an item outside the range of the array index

## Chapter 4
### Subprograms
```python
def sum(n1, n2):   # Defining a sub-program
    sum = n1 + n2
    return sum

print(sum(1, 2))   # Calling a sub-program
```
> [!tip] Benefits of modularisation
> 1. Easy to understand
> 2. Facilitate reuse
> 3. Enhance development efficiency

## Chapter 5
### Stacks
First in, last out
### Queues
First in, first out
#### Circular queue
more efficient to run in
### Linear linked list
