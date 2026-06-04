---
tags:
  - ict
  - elective
  - database
  - sql
  - functions
aliases:
  - SQL Functions
  - Database Functions
  - Elective A
---

# Database Functions and Design

## Text Functions

| Function | Description |
| :--- | :--- |
| `LENGTH` | Counts the number of characters |
| `MID(<string>, <start_num>, <num_char>)` | Returns `<num_char>` characters from the `<start_num>`-th character of `<string>` |
| `UPPER` / `LOWER` | Converts to uppercase / lowercase |
| `LEFT(<string>, <n>)` / `RIGHT(<string>, <n>)` | Returns `<n>` characters from the left / right |
| `INSTR(<string>, <sub>)` | Returns the position of the first occurrence of `<sub>` |
| `TRIM` / `LTRIM` / `RTRIM` | Removes leading and trailing spaces |
| `REPLACE(<string>, <old>, <new>)` | Substitutes occurrences of a specified string |
| `CONCAT(<s1>, <s2>, ...)` | Joins strings together |

## Date and Time Functions

| Function | Description |
| :--- | :--- |
| `DATE()` / `NOW()` | Returns current date / date and time |
| `YEAR(<date>)`, `MONTH(<date>)`, `DAY(<date>)` | Extracts the component from a date |
| `DATEDIFF(<interval>, <d1>, <d2>)` | Calculates the difference between two dates |
| `DATEADD(<interval>, <num>, <date>)` | Adds a time interval to a date |

## Aggregation Functions

`COUNT`, `MAX`, `MIN`, `SUM`, `AVG`

> [!error] Do NOT use `COUNT()`!
> `COUNT()` is not valid. Use `COUNT(*)`.

> [!warning] Do NOT mix up `WHERE` and `HAVING`!
> `WHERE` is used to filter the records **before** categorisation, while `HAVING` is used to filter the categories **after** categorisation.

> [!caution] Aggregation Without GROUP BY
> ```sql
> MariaDB [ict]> SELECT NAME, MAX(SCORE2) FROM STUDENT;
> +------+-------------+
> | NAME | MAX(SCORE2) |
> +------+-------------+
> | Hans |          89 |
> +------+-------------+
> ```
> However, Hans does not have the highest score. Use `GROUP BY` for correct results.

---

# Joining Tables

## INNER JOIN

Returns records that have matching values in both tables.

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

## LEFT (OUTER) JOIN

Returns all records from the left table, and the matched records from the right table. The result is NULL from the right side if there is no match.

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

## RIGHT (OUTER) JOIN

Returns all records from the right table, and the matched records from the left table. The result is NULL from the left side when there is no match.

```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

---

# Database Design

## Entity-Relationship Diagram (ERD)

- **Entities**: Represented by rectangles (e.g., STUDENT).
- **Attributes**: Represented by ovals. **Primary Keys** are underlined.
- **Relationships**: Represented by diamonds.
- **Cardinality**:
  - 1:1 (One-to-One)
  - 1:N (One-to-Many)
  - M:N (Many-to-Many)
- **Participation**:
  - **Mandatory (Total)**: Every entity instance must participate in the relationship (double line).
  - **Optional (Partial)**: Not all entity instances participate.

## Normalisation

Process of reducing data redundancy and preventing update anomalies.

1. **1NF (First Normal Form)**: No repeating groups; all attributes are atomic.
2. **2NF (Second Normal Form)**: Must be in 1NF and have **no partial functional dependencies** (all non-key attributes must depend on the *entire* primary key).
3. **3NF (Third Normal Form)**: Must be in 2NF and have **no transitive dependencies** (non-key attributes should not depend on other non-key attributes).

---

# Database Management

## Data Integrity

- **Entity Integrity**: Every table must have a unique Primary Key that is NOT NULL.
- **Referential Integrity**: Foreign Keys must match an existing Primary Key in the related table (prevents orphaned records).
- **Domain Integrity**: Data must follow defined formats, types, or ranges.

## Data Security & Privacy

- **Authentication**: Verifying identity (e.g., password).
- **Authorization**: Granting permissions (SELECT, UPDATE, DELETE).
- **Views**: Virtual tables that restrict access to sensitive columns/rows.
- **Record Locking**: Prevents inconsistencies when multiple users update the same data simultaneously.

## DBA (Database Administrator) Roles

- Performance monitoring and query optimization.
- Backup and recovery management (Full vs. Incremental).
- Defining the **Data Dictionary** (Metadata about tables, types, and constraints).

---

# Relational Database Concepts

## Chapter 4: Relational Database

> [!tip] Lots of Buzzwords
> This chapter contains many important terms. Pay close attention to the definitions.

### Concept of a Relational Database

**Relational databases** organise data in **tabular form** (tables). A table consists of columns and rows. Each row is a **record**.

The elements of a relational database are usually stored as or represented by different elements in a **Database Management System** (DBMS).

> [!info] Elements of a Relational Database and Their DBMS Counterparts
> | Relational Database | DBMS |
> | :--- | :--- |
> | Entity type | Table |
> | Entity | Record |
> | Attribute | Field |
> | Relationship | Foreign key |
> | Domain | Datatype and constraint |

---

## Related

- [[ICT Index]] - Subject overview
- [[Elective/A headings]] - SQL syntax reference
- [[Database Class Practice]] - SQL practice exercises
- [[Elective/Elective A Chapters 4-5]] - Database design theory
