Here are your comprehensive notes based on the provided chapter material, formatted in Obsidian-flavored markdown.

# Database Systems & Design

## Chapter 1: Relational Database Basics

### Elements of a Relational Database

| Relational Database | DBMS |
| :--- | :--- |
| **Entity type** | Table |
| **Entity** | Record |
| **Attribute** | Field |
| **Relationship** | Foreign key |
| **Domain** | Data type and constraint |

### Schema Structure
The `STUDENT` schema is defined as:
`STUDENT (SID, SNAME, SEX, DOB, HKID, CLASS, CNO, SCORE, EMAIL, REG)`

| Field | Data Type | Description | Remark |
| :--- | :--- | :--- | :--- |
| SID | Character | Student identity code | Primary key |
| SNAME | Character | Student name | |
| SEX | Character | Sex of the student | |
| DOB | Date | Date of birth of the student | |
| HKID | Character | HKID of the student | Candidate key |
| CLASS | Character | Class of the student | Foreign key |
| CNO | Integer | Class number of the student | |
| SCORE | Float | Score of the student | |
| EMAIL | Character | Personal email address of the student | Candidate key |
| REG | Boolean | Whether the student is registered | |

### Keys
#### Candidate Key
*   Stores unique data.
*   Cannot store null value.
*   May consist of more than one field.
*   Must be minimal.
*   Is the candidate for the primary key.
*   *Note:* A candidate key consisting of more than one field is called a **composite key**.

#### Primary Key
*   Stores unique data.
*   Cannot store null value.
*   May consist of more than one field.
*   Must be minimal.
*   *Rule:* A table may have more than one candidate key, but it can only have one primary key.

### Foreign Key & Indexing
*   **Foreign Key**: Used to show the relationship between records in two tables; it is the primary key of the parent table. A table can have more than one foreign key.
*   **Index**:
    *   Allows the DBMS to perform a binary search on the indexed field to speed up data retrieval.
    *   Updated if changes are made to the data or a new record is added.
    *   Takes time to update and consumes storage space.
    *   *Tip:* Only frequently searched fields should be indexed.

### Integrity Constraints
| Integrity | Concern |
| :--- | :--- |
| **Entity integrity** | The existence and validity of the primary key |
| **Referential integrity** | The validity of the foreign key |
| **Domain integrity** | The data types and constraints of the attributes |

---

## Chapter 2: Database Design and ER Diagrams

### ER Diagram Components
ER diagrams are used to model the logical view of a database.

| Shape | Element | Remark |
| :--- | :--- | :--- |
| Rectangle | Entity type | |
| Diamond | Relationship | Relationships may have attributes. |
| Ellipse | Attribute | Underlined attributes represent the primary key. |

#### Relationships and Cardinality
*   **Mandatory side**: A student *must* join a sports event.
*   **Optional side**: A student *may or may not* join a sports event.
*   **One**: A student may join *one* sports event at most.
*   **Many**: A student may join *many* sports events.

### Managing Anomalies
*   **Update anomaly**: Failure to maintain data consistency after an update is made.
*   **Insertion anomaly**: Inability to insert data of one entity type without having the data of another entity type.
*   **Deletion anomaly**: Loss of data of one entity type when deleting the data of another entity type.

### Normalisation vs. Denormalisation

| Normalisation | Denormalisation |
| :--- | :--- |
| Less storage space required | Faster data retrieval |
| Higher flexibility of data management | Simpler SQL statements for queries |
| No risk of data inconsistency (Update anomaly) | |
| Ability to insert/delete without data loss | |

### Functional Dependencies
*   **Partial functional dependency**: Some non-primary key attributes are dependent on *part* of the primary key.
*   **Transitive functional dependency**: Some non-primary key attributes are dependent on *other non-primary key* attributes.

### Levels of Normalisation (Normal Forms)

| Rule | 1NF | 2NF | 3NF |
| :--- | :---: | :---: | :---: |
| No multiple values for an attribute | ✅ | ✅ | ✅ |
| No repeating attributes | ✅ | ✅ | ✅ |
| No partial functional dependency | | ✅ | ✅ |
| No transitive functional dependency | | | ✅ |