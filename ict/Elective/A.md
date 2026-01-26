# Chapter 2
## Function

### Text function
`LENGTH` counts the number of characters.
`MID(<string>, <start_num>, <num_char>)` returns `<num_char>` characters from the `<start_num>`-th character of `<string>`.
`UPPER` converts to uppercase, `LOWER` converts to lowercase.

## Aggregation functions
`COUNT`, `MAX`, `MIN`, `SUM`, `AVG`

> [!warning] Do not use `COUNT()`!!!!
> `COUNT()` is not valid. Use `COUNT(*)`

> [!warning] DO NOT MIX UP `WHERE` AND `HAVING`!!!
> `WHERE` is used to filter the records **before** categorisation, while `HAVING` is used to filter the categories **after** categorisation.

> [!warning] use aggregation function
> ```sql
> MariaDB [ict]> SELECT NAME, MAX(SCORE2) FROM STUDENT;
> +------+-------------+
> | NAME | MAX(SCORE2) |
> +------+-------------+
> | Hans |          89 |
> +------+-------------+
> ```
> However, Hans does not have the highest score.

