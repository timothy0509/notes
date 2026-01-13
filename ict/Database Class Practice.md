# Practice

## 1. Create database and table

Create a fakermon database with a single table of monsters' names.

| Learn                           | Task                                                                                                                                               | SQL / Answers                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Show databases                  | **List** all databases.                                                                                                                            | `SHOW DATABASES`                                       |
| Create database                 | **Create** the pokemon database.                                                                                                                   | `CREATE DATABASE pokemon`                              |
| Drop database                   | Due to copyright issues, avoid the name pokemon.<br>**Rename** the database from pokemon to fakermon.<br><br>*(Cannot directly rename a database)* | `DROP DATABASE pokemon;`<br>`CREATE DATABASE fakermon` |
| Create table                    | **Create** the monster table.<br><br>*Specify the database by:*<br>`USE <db_name>`                                                                 |                                                        |
| Show tables                     | **List** all tables                                                                                                                                |                                                        |
| Show table info                 | **Show** monster table info                                                                                                                        |                                                        |
| Describe table<br>*(Out Syll')* | **Describe** monster table field                                                                                                                   |                                                        |
| Rename table                    | The name monster seems haunting<br>**Rename** monster table to pet<br><br>*(Can rename an existing table)*                                         |                                                        |

## 2. CRUD operations

Manage records in monster table

| Learn                | Task                                                                        | SQL / Answers |
| -------------------- | --------------------------------------------------------------------------- | ------------- |
| Setup                | **Drop** pet table<br>**Re-create** pet table with name field               |               |
| Query all            | **List** all records in monster table<br><br>* Use to verify changes below: |               |
| Insert a row         | **Add** 'Pikachu' to monster table<br><br>*(Field names are optional)*      |               |
| Insert multiple rows | **Add** 'Squirtle' and 'Charmander'<br><br>*(Specify field names)*          |               |
| Update a row         | Pikachu has evolved to Raichu.<br>**Update** 'Pikachu' to 'Raichu'          |               |
| Delete a row         | **Delete** 'Charmander'                                                     |               |
| **Question 1**       | Can we add another 'Raichu'?<br>                                            |               |
| **Question 2**       | Can we add a pet with no name?                                              |               |
| **Question 3**       | Can we update only one Raichu back to Pikachu?                              |               |
## 3. Primary key (PK)

Use of  primary key

| Learn                                   | Task                                                                                                             | SQL / Answers |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------- |
| Setup                                   | Drop pet table<br>                                                                                               |               |
| Set primary key                         | **Add** id as a *primary key*                                                                                    |               |
| Insert a row with PK                    | **Add** 'Pikachu' with id=1                                                                                      |               |
| Insert multiple rows                    | **Add** 'Squirtle' and 'Charmander'                                                                              |               |
| Insert multiple rows with same field    | **Add** two more 'Pikachu'                                                                                       |               |
| Update a row by PK                      | The first Pikachu refused to evolve, evolve the second Pikachu<br><br>**Update** the third 'Pikachu' to 'Raichu' |               |
| Select rows                             | **List** all rows of 'Pikachu'                                                                                   |               |
| Select single rows by PK                | **Select** specific 'Pikachu' with id=1                                                                          |               |
| Delete a row by PK                      | **Delete** the first 'Pikachu'                                                                                   |               |
| Drop primary key                        | **Drop** the primary key (id)                                                                                    |               |
| Fail to add primary key when not unique | Try adding name as **primary key**<br><br>*(Fail: name not unique)*                                              |               |
| Add primary key                         | Add id as **primary key** again<br><br>*(Succeed!)*                                                              |               |
| Add composite PK                        | **Drop PK and add** (id, name) as PK again                                                                       |               |
| Test composite PK                       | **Add** 'Pikachu' with id=9<br><br>*(Fail: violate PK)*                                                          |               |
| Test composite PK 2                     | **Add** 'Squirtle' with id=9                                                                                     |               |
| **Question 1**                          | Can you add another pets with id=2?                                                                              |               |
| **Question 2**                          | What is the purpose of primary key?                                                                              |               |
| **Question 3**                          | Is the primary key meaningful?                                                                                   |               |
| **Question 4**                          | How to set arbitrary primary key easily?                                                                         |               |
| **Question 5**                          | Can the primary key be meaning? Give an example.                                                                 |               |

## 4. AUTO_INCREMENT

Use Auto increment primary key

| Learn                        | Task                                                                                     | SQL / Answers |
| ---------------------------- | ---------------------------------------------------------------------------------------- | ------------- |
| Setup                        | Drop pet table                                                                           |               |
| Auto increment               | **Create** the table pet again using auto increment id, with a name field and a hp field |               |
| Add record                   | **Add** 'Pikachu' with id=2 and hp=10                                                    |               |
| Add row with specific fields | **Add** another 'Pikachu' with hp = 150 and let db decides the id                        |               |
| Add multiple rows            | **Add** 'Squirtle' (hp 20) and 'Charmander' (hp 8)                                       |               |
| Add row with one field only  | **Add** 'Raichu' specifying the name only                                                |               |
| **Question 1**               | How to enforce the field not to be null                                                  |               |
| **Question 2**               | How to set default value when the field is not specified on creation                     |               |

## 5. DEFAULT

Set default field value on row creation

| Learn                            | Task                                                                                                 | SQL / Answers |
| -------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------- |
| Add **DEFAULT**                  | Set default hp=10 if not specific<br><br>*(Verify by 'DESCRIBE pet')*                                |               |
| **Add** row with DEFAULT         | Add 'Squirtle' with default hp<br><br>*(Default value is applied when hp is not specified)*          |               |
| **Add** row and override DEFAULT | Add 'Charmander' with hp=8<br><br>*(Default value is not applied when hp is specified)*              |               |
| Add row with **NULL**            | Add 'Bulbasaur' with hp=NULL<br><br>*(Default value is not applied even if hp is NULL)*              |               |
| **Change** default value         | hp=10 is a bit low,<br>Change default hp to 15<br><br>*(Default value only applies on row creation)* |               |
| **Drop** default value           | We shouldn't assume anything,<br>Drop the default value                                              |               |

## 6. Add/Modify/drop field

Add, modify or drop fields in table

| Learn                                        | Task                                                                                                                                                                                                                                                                   | SQL / Answers |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Add field**/column                         | Add attack field<br><br>*(You can add fields to an existing table without dropping and creating a new one)*                                                                                                                                                            |               |
| Add field with **default** value             | Add defend field with default value of 10<br><br>*(Defend of all rows are set to the default value.)*                                                                                                                                                                  |               |
| **Add** row                                  | Add 'Caterpie' with hp=12, attack=7 and defend=8                                                                                                                                                                                                                       |               |
| **Rename** field by dropping and adding back | Rename defend to def by dropping and adding fields<br><br>*(Not a recommended way, all values of that field will be dropped)*                                                                                                                                          |               |
| **Rename** field by renaming                 | Rename attack to atk without dropping<br><br>*(Note that the original values are kept after renaming)*<br><br>*(Newer MySQL uses the keyword CHANGE instead of RENAME. If your query doesn't work, try the following:<br>ALTER TABLE pet  <br>CHANGE attack atk INT;)* |               |

## 7. NOT NULL

Add NOT NULL constraint to fields

| Learn                                                  | Task                                                                                                                                                                             | SQL / Answers |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Set field to **NOT NULL**                              | Name should not be null. Set it to NOT NULL.                                                                                                                                     |               |
| **Fail** to set NOT NULL if field contains NULL values | hp should not be null.<br>Try set it to NOT NULL.<br><br>*(Failed because some of the existing values are NULL)*                                                                 |               |
| **Questions 1**                                        | Can you set hp to NOT NULL?                                                                                                                                                      |               |
| **Questions 2**                                        | If not, why?                                                                                                                                                                     |               |
| **Questions 3**                                        | How can you fix it?                                                                                                                                                              |               |
| Should not use **=NULL**                               | Try fill NULL value with some value<br><br>*(Failed because we should not use =NULL. We should use IS NULL)*                                                                     |               |
| Should use **IS NULL**                                 | Fill NULL value with some value again                                                                                                                                            |               |
| Set hp to **NOT NULL**                                 | Set hp to NOT NULL.<br><br>*(Succeeded this time!)*                                                                                                                              |               |
| **Violate** NOT NULL constraint                        | Try adding 'Caterpie' with hp NULL<br><br>*(Failed due to NOT NULL constraint)*                                                                                                  |               |
| **Remove** NOT NULL constraint                         | Set hp to nullable again (Remove NOT NULL constraint)                                                                                                                            |               |
| **Verify** removal                                     | Try adding 'Caterpie' with hp NULL<br><br>*(Succeeded this time!)*                                                                                                               |               |
| **Conclusion**                                         | - A constraint can only be applied when the existing data satisfies the constraint itself<br>- After a constraint is set, all (CRUD) operations must not violate the constraint. |               |

## 8. UNIQUE

Add constraint to fields

| Learn                          | Task                                                                                                                                        | SQL / Answers |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **UNIQUE** constraint          | Recreate the table with id as primary key, unique name, default values of hp=10, atk=10 and def=10, and NOT NULL for all fields.            |               |
|                                | Add 'Pikachu' with default states                                                                                                           |               |
| **Verify** UNIQUE field        | Try to add another 'Pikachu' but with different states<br><br>*(Failed because name 'Pikachu' already exists, violating UNIQUE constraint)* |               |
| **Drop** UNIQUE                | Check the name of the unique key and drop it                                                                                                |               |
| **Verify** with UNIQUE removed | Add another 'Pikachu' but with different states again<br><br>*(Succeeded)*                                                                  |               |

## 9. CHECK

Add constraint to fields

| Learn | Task                      | SQL / Answers |
| ----- | ------------------------- | ------------- |
|       | Check length of name      |               |
|       | Check hp > 0              |               |
|       | Check hp between 1 and 30 |               |
|       | Check atk + def < 40      |               |

## 10. INDEX

Add constraint to fields

| Learn | Task | SQL / Answers |
| ----- | ---- | ------------- |
|       |      |               |

## 11. Foreign Key (FK)

Add constraint to fields