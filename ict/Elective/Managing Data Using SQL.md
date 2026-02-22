---
aliases: ["A headings"]
tags: [Elective, SQL, ICT]
---

Subagent assignments (each top-level heading handled by a subagent):

- Subagent 1: `Managing Data Using SQL` (core SQL and schema)
- Subagent 2: `SQL Operators and Functions` (operators, built-ins, aggregation)
- Subagent 3: `SQL Operations on Multiple Tables` (joins, subqueries, combining results)
- Subagent 4: `Relational Database` (ER concepts, integrity, schema)

---

# Managing Data Using SQL

Clear, exam-focused notes covering practical SQL usage: database creation, table structure, data manipulation, constraints, and schema changes. Use the examples with a sample `students` and `courses` dataset.

## Database and SQL statement

### What is a database?

- A structured collection of data stored and accessed electronically.
- Relational Database Management System (RDBMS) stores data in tables (rows and columns) and uses SQL for querying.
- Examples: MySQL, PostgreSQL, SQLite, SQL Server.

### Database structure

- Database: container for tables, views, indexes, procedures.
- Table: named collection of rows (records) with columns (fields).
- Row: a single record; Column: attribute with a data type and constraints.
- Schema: definition of tables, columns, keys, relationships.

### SQL Statement

- SQL (Structured Query Language) is declarative: you describe what you want, not how to compute it.
- Categories:
  - DDL (Data Definition Language): `CREATE`, `ALTER`, `DROP`.
  - DML (Data Manipulation Language): `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
  - DCL (Data Control Language): `GRANT`, `REVOKE`.
  - Transaction control: `BEGIN`/`START TRANSACTION`, `COMMIT`, `ROLLBACK`.

## Creating Databases and Tables

Basic database and table management commands with examples.

### `SHOW DATABASES`

Lists databases available in the server (MySQL syntax):

```sql
SHOW DATABASES;
```

### `CREATE DATABASE`

Create a new database:

```sql
CREATE DATABASE ict_elective;
```

### `USE`

Select a database to operate in (MySQL):

```sql
USE ict_elective;
```

### `CREATE TABLE`

Create tables with column definitions and constraints. Example `students` table:

```sql
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  dob DATE,
  gender CHAR(1),
  reg_number VARCHAR(10) UNIQUE
);
```

Include sensible constraints: `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `DEFAULT`.

### `SHOW TABLES`

Lists tables in current database:

```sql
SHOW TABLES;
```

## Data Type

- Choose types to match data and storage needs: `INT`, `BIGINT`, `DECIMAL(p,s)`, `CHAR(n)`, `VARCHAR(n)`, `TEXT`, `DATE`, `DATETIME`, `TIMESTAMP`, `BOOLEAN`.
- Use fixed-length `CHAR` for codes; `VARCHAR` for variable-length strings.

#### Numbers with leading zeros

- Numeric types drop leading zeros (e.g., `00123` stored as `123`). To preserve leading zeros:
  - Store as text: `CHAR` or `VARCHAR` (recommended for identifiers like `reg_number`).
  - Use formatting functions when displaying numbers (e.g., `LPAD()` in MySQL):

```sql
SELECT LPAD(student_id, 6, '0') AS padded_id FROM students;
```

## Inserting and Retrieving Data

### `INSERT INTO ... VALUES`

Insert a single row or multiple rows:

```sql
INSERT INTO students (student_id, first_name, last_name, dob, gender, reg_number)
VALUES (1, 'Amina', 'Kassim', '2005-04-12', 'F', 'A001');

INSERT INTO students (student_id, first_name, last_name)
VALUES (2, 'James', 'Doe'), (3, 'Lina', 'Zhang');
```

### `SELECT ... FROM`

Retrieve columns from a table:

```sql
SELECT first_name, last_name FROM students;
SELECT * FROM students; -- all columns
```

### `WHERE`

Filter rows with conditions:

```sql
SELECT * FROM students WHERE gender = 'F' AND dob >= '2004-01-01';
```

### `ORDER BY`

Sort results:

```sql
SELECT * FROM students ORDER BY last_name ASC, first_name DESC;
```

### `DISTINCT`

Remove duplicates from result set:

```sql
SELECT DISTINCT gender FROM students;
```

## Updating and Deleting Data

### `UPDATE ... SET`

Change existing records. Always include a `WHERE` clause to avoid updating all rows unintentionally.

```sql
UPDATE students SET last_name = 'Smith' WHERE student_id = 2;
```

#### Updating multiple fields

```sql
UPDATE students
SET first_name = 'Fatima', dob = '2005-03-20'
WHERE student_id = 1;
```

### `DELETE FROM`

Remove rows. Use `WHERE` to limit deletion.

```sql
DELETE FROM students WHERE student_id = 3;
```

### `DROP TABLE`

Remove table and its data/metadata. Irreversible unless you have backups.

```sql
DROP TABLE students;
```

### `DROP DATABASE`

Delete entire database and all contained objects:

```sql
DROP DATABASE ict_elective;
```

## Setting Constraints

Constraints enforce rules at the database level.

### `PRIMARY KEY`

- Uniquely identifies rows; cannot be NULL. Often an integer `AUTO_INCREMENT` or UUID.

#### Composite Key

- A primary key composed of multiple columns when a single column cannot guarantee uniqueness:

```sql
CREATE TABLE enrollment (
  student_id INT,
  course_id INT,
  term VARCHAR(10),
  PRIMARY KEY (student_id, course_id, term)
);
```

### `FOREIGN KEY`

- Enforces referential integrity between tables:

```sql
CREATE TABLE courses (
  course_id INT PRIMARY KEY,
  title VARCHAR(100)
);

CREATE TABLE enrollment (
  student_id INT,
  course_id INT,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

### Other Constraints

- `UNIQUE`, `NOT NULL`, `CHECK` (validate values), `DEFAULT` (set default values).

## Altering Table Structure

Use `ALTER TABLE` to change schema without dropping table.

### Renaming Tables

```sql
ALTER TABLE old_name RENAME TO new_name; -- PostgreSQL / standard
-- MySQL: RENAME TABLE old_name TO new_name;
```

### Adding fields

```sql
ALTER TABLE students ADD COLUMN email VARCHAR(100);
```

### Modifying fields

Change definition of a column (name, type, nullability).

#### Renaming fields

```sql
ALTER TABLE students RENAME COLUMN reg_number TO registration_no; -- PostgreSQL
-- MySQL: ALTER TABLE students CHANGE reg_number registration_no VARCHAR(10);
```

#### Changing data types

```sql
ALTER TABLE students ALTER COLUMN dob TYPE TIMESTAMP; -- PostgreSQL
-- MySQL: ALTER TABLE students MODIFY dob DATETIME;
```

### Dropping fields

```sql
ALTER TABLE students DROP COLUMN email;
```

### Adding and dropping constraints

#### Primary Key

Add:

```sql
ALTER TABLE enrollment ADD PRIMARY KEY (student_id, course_id);
```

Drop (syntax varies):

```sql
ALTER TABLE enrollment DROP CONSTRAINT enrollment_pkey; -- PostgreSQL
-- MySQL: ALTER TABLE enrollment DROP PRIMARY KEY;
```

#### Foreign Key

Add:

```sql
ALTER TABLE enrollment
ADD CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(student_id);
```

Drop:

```sql
ALTER TABLE enrollment DROP CONSTRAINT fk_student; -- PostgreSQL
-- MySQL: ALTER TABLE enrollment DROP FOREIGN KEY fk_student;
```

#### Other constraints

- `UNIQUE`, `CHECK` and `NOT NULL` can be added or removed with `ALTER TABLE` (syntax database-specific).

# SQL Operators and Functions

Operators and built-in functions let you evaluate expressions, transform data, and aggregate results.

## SQL Operator

### Arithmetic operator

- `+ - * / %` for addition, subtraction, multiplication, division and modulus.

Example:

```sql
SELECT price, quantity, price * quantity AS total FROM sales;
```

### Comparison operator

- `=`, `<>` or `!=`, `<`, `>`, `<=`, `>=`.

### Logical Operator

- `AND`, `OR`, `NOT` combine boolean expressions.

#### `IN`

Check membership in a list:

```sql
SELECT * FROM students WHERE student_id IN (1,2,5);
```

### `BETWEEN ... AND`

Range test inclusive:

```sql
SELECT * FROM students WHERE dob BETWEEN '2004-01-01' AND '2006-12-31';
```

### `LIKE`

Pattern matching with wildcards `%` (any string) and `_` (single char):

```sql
SELECT * FROM students WHERE last_name LIKE 'S%'; -- starts with S
SELECT * FROM students WHERE reg_number LIKE '%001'; -- ends with 001
```

### `IS NULL` and `IS NOT NULL`

NULL represents unknown/missing data; comparisons with `=` fail—use `IS NULL`.

```sql
SELECT * FROM students WHERE email IS NULL;
```

## Function

Functions operate on data: text, date/time, numeric and aggregation functions.

### Text function

- `CONCAT()`, `UPPER()`, `LOWER()`, `TRIM()`, `SUBSTR()` / `SUBSTRING()`.

Example:

```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM students;
```

### Time function

- `NOW()`, `CURRENT_DATE`, `DATE_ADD`, `DATEDIFF`, `EXTRACT()`.

Example: age calculation (MySQL):

```sql
SELECT TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age FROM students;
```

### Aggregation function

- Operate across rows: `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`.

#### `GROUP BY` clause

Group rows to produce aggregated results per group:

```sql
SELECT gender, COUNT(*) AS cnt FROM students GROUP BY gender;
```

#### `HAVING` clause

Filter groups (use after `GROUP BY`):

```sql
SELECT course_id, COUNT(*) AS enrolments
FROM enrollment
GROUP BY course_id
HAVING COUNT(*) > 10;
```

#### `COUNT(<expression>)`

- `COUNT(*)` counts rows; `COUNT(column)` counts non-NULL values.

#### `MAX(<expression>)` and `MIN(<expression>)`

- Return largest/smallest value in a group.

### `SUM(<expression>)`

- Total of numeric expression.

### `AVG(<expression>)`

- Average of numeric expression (NULLs ignored).

# SQL Operations on Multiple Tables

Key techniques: joins, subqueries, set operations, views and indexes.

## Joining Tables

Combining columns from related tables using keys.

### `INNER JOIN`

Return rows with matching keys in both tables:

```sql
SELECT s.first_name, s.last_name, c.title
FROM students s
INNER JOIN enrollment e ON s.student_id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id;
```

### `LEFT JOIN`

Return all rows from left table and matched rows from right table (NULL where no match):

```sql
SELECT s.first_name, e.course_id
FROM students s
LEFT JOIN enrollment e ON s.student_id = e.student_id;
```

### `RIGHT JOIN`

All rows from right table + matches from left (less common; mirror of LEFT JOIN).

### `FULL JOIN`

Return rows with matches in either table; rows missing match show NULLs (supported in PostgreSQL).

### Other joining methods

#### Equi-join

- Join using equality condition (most common): `ON a.id = b.a_id`.

#### `NATURAL JOIN`

- Automatically joins on columns with the same name; use cautiously (implicit behavior).

#### Self join

- Join table to itself to compare rows:

```sql
SELECT a.student_id, b.student_id
FROM students a
JOIN students b ON a.registration_no = b.registration_no
WHERE a.student_id <> b.student_id;
```

#### Joining more than two tables

- Chain joins using multiple `JOIN` clauses.

#### `CROSS JOIN`

- Cartesian product (every row of A paired with every row of B). Rarely used without `WHERE`.

## Subquery

Query nested within another query; can appear in `SELECT`, `FROM`, `WHERE`.

### `IN`

Use a subquery to test membership:

```sql
SELECT * FROM students WHERE student_id IN (SELECT student_id FROM enrollment WHERE course_id = 10);
```

### `EXISTS`

Tests whether subquery returns any rows; efficient for correlated subqueries:

```sql
SELECT * FROM students s WHERE EXISTS (
  SELECT 1 FROM enrollment e WHERE e.student_id = s.student_id AND e.course_id = 10
);
```

### `ANY`

Compare a value to any value in subquery result (e.g., `> ANY(...)`).

### `ALL`

Compare a value to all values in subquery result (e.g., `>= ALL(...)`).

## Combining Results

Set operations combine result sets with compatible columns.

### `UNION`

Combine results of two queries, removing duplicates. Columns must match in number and compatible types:

```sql
SELECT first_name FROM students
UNION
SELECT name FROM teachers;
```

#### Joining tables vs combining results

- Joins create wider rows (combine columns from tables) while `UNION` stacks rows (combine similar results vertically).

### `UNION ALL`

Same as `UNION` but keeps duplicates (faster).

### `EXCEPT`

Return rows from first query not present in second (PostgreSQL). MySQL uses `NOT IN` or `LEFT JOIN`/`IS NULL` pattern instead.

## Creating Views and Indices

Abstractions and performance tools.

### View

- A virtual table defined by a query; simplifies complex queries and can provide a security layer by exposing limited columns.

#### View in database

##### `CREATE VIEW`

```sql
CREATE VIEW student_names AS
SELECT student_id, first_name || ' ' || last_name AS full_name FROM students; -- PostgreSQL concat
```

##### `CREATE OR REPLACE VIEW`

Updates view definition without dropping it:

```sql
CREATE OR REPLACE VIEW student_names AS
SELECT student_id, CONCAT(first_name, ' ', last_name) AS full_name FROM students; -- MySQL
```

##### `DROP VIEW`

```sql
DROP VIEW student_names;
```

### Index

- Indexes speed up lookups on columns but add overhead on writes (INSERT/UPDATE/DELETE). Choose indexes for frequently searched or joined columns.

#### `CREATE INDEX`

```sql
CREATE INDEX idx_students_lastname ON students(last_name);
```

#### `DROP INDEX`

```sql
DROP INDEX idx_students_lastname; -- MySQL
-- PostgreSQL: DROP INDEX idx_students_lastname;
```

# Relational Database

Conceptual foundations for designing databases correctly.

## Concept of a Relational Database

### Entity

- A real-world object or concept represented as a table (e.g., Student, Course).

### Attribute

- A property of an entity (e.g., `first_name`, `dob`). Mapped to table columns.

### Relationship

- How entities relate: one-to-one, one-to-many, many-to-many (implemented with join tables).

### Domain

- Allowed set of values for an attribute (data type, range, enumerations).

## Schema

Design of tables, keys, constraints and relationships.

### Key fields

#### Candidate Key

- A column or set of columns that uniquely identify a row (multiple candidates possible).

##### Composite Key

- Candidate key composed of multiple attributes.

#### Primary Key

- Chosen candidate key used as the main identifier.

#### Foreign key

- Attribute that references a primary key in another table to represent relationships.

### Index

- Improves lookup speed; usually built on key fields or frequently searched columns.

## Integrity

Rules that keep data correct and meaningful.

### Entity integrity

- Primary keys must be unique and not NULL.

### Referential integrity

- Foreign keys must either match a primary key in the referenced table or be NULL (unless `NOT NULL`). Use `ON DELETE` / `ON UPDATE` actions (`CASCADE`, `SET NULL`, `RESTRICT`).

### Domain integrity

- Values must be within the defined domain (type, `CHECK` constraints, enumerations).

## Rollback

- Transactions group multiple statements into an atomic unit. Use `BEGIN` / `START TRANSACTION`, then `COMMIT` to persist, or `ROLLBACK` to undo all changes since transaction started.

Example:

```sql
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- If error or validation fails:
ROLLBACK;
-- Otherwise:
COMMIT;
```

---

Exam tips

- Learn core DDL and DML statements with syntax and common options.
- Practice by building small schemas (`students`, `courses`, `enrollment`) and writing queries (joins, aggregates, subqueries).
- For exams: always state assumptions, show sample output for SELECT queries, and remember to use `WHERE` with `UPDATE`/`DELETE`.

Further study

- Transactions and isolation levels, query optimization, normalization forms, stored procedures and triggers.
