-- Active: 1689760779587@@127.0.0.1@3306@Gift
-- Active: 1689760779587@@127.0.0.1@3306
"""Q1. A database is a structured collection of data that is organized and stored in a way that allows for efficient retrieval, management, and manipulation of that data. Databases are commonly used in various applications and systems to store and retrieve information.

SQL databases are based on the relational model, where data is organized into tables with rows and columns.
They enforce a predefined schema that determines the structure of the data.
SQL databases use SQL as the standard language for defining, querying, and manipulating data.
They provide ACID (Atomicity, Consistency, Isolation, Durability) properties, which ensure data integrity and transactional consistency.
Popular SQL databases include MySQL, PostgreSQL, Oracle, Microsoft SQL Server, and SQLite.
NoSQL Databases:

NoSQL databases use various data models for organizing and storing data, such as key-value pairs, document-oriented, columnar, or graph-based structures.
They offer flexibility in data representation, allowing for schema-less or schema-flexible designs.
NoSQL databases are designed to scale horizontally, making them suitable for handling large amounts of data and high traffic loads.
They typically lack ACID properties in favor of performance and scalability.
Examples of NoSQL databases include MongoDB, Cassandra, Redis, Couchbase, and Neo4j."""


"""Q2. DDL stands for Data Definition Language, and it is a subset of SQL used to define and manage the structure of a database and its objects. DDL statements are responsible for creating, modifying, and deleting database objects such as tables, indexes, views, and constraints.

a. CREATE - The create statement is used to create new database objects, such as tables, views, indexes, or schemas.
"""

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    emp_age INT,
    emp_department VARCHAR(100)
);

CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);


"""b. DROP:
The DROP command is used to remove an existing database object, such as a table or index.
"""

DROP TABLE Student;

"""c. ALTER:
The ALTER command is used to modify the structure of an existing database object, such as adding or dropping columns from a table."""

ALTER TABLE Employees
ADD emp_salary DECIMAL(10, 2);


"""d. TRUNCATE:
The TRUNCATE command is used to remove all the data from a table, but it retains the structure of the table. It is a faster alternative to the DELETE command when you want to delete all records from a table."""


TRUNCATE TABLE Employees;


""" Q3. DML stands for Data Manipulation Language,  DML commands are responsible for performing operations such as inserting, updating, and deleting data 
in the database tables."""


# A. INSERT: The INSERT command is used to insert data into a table.

INSERT INTO Employees (emp_id, emp_name, emp_age, emp_department, emp_salary)
VALUES (101, 'John Doe', 30, 'IT', 55000), (102, 'John Jacob', 20, 'CSE', 50000);

# B. UPDATE: The UPDATE command is used to modify existing records in a table.
UPDATE Employees
SET emp_salary = emp_salary + 5000
WHERE emp_id = 101;

# C. DELETE: The DELETE command is used to remove records from a table.

DELETE FROM Employees
WHERE emp_id = 101;


# Q4. DQL stands for Data Query Language, and it is a subset of SQL (Structured Query Language) used to retrieve and manipulate data from a database. The primary DQL command is SELECT, which allows you to retrieve specific information from one or more tables in the database.

SELECT emp_name, emp_salary
FROM Employees
WHERE emp_salary > 40000;

# Q5. Explain Primary Key and Foreign Key.

"""A. Primary Key:
A Primary Key is a column or a set of columns in a database table that uniquely identifies each row (record) in that table. 
It must have a unique value for each row and cannot contain NULL values.

B. Foreign Key:
A Foreign Key is a column or a set of columns in a table that refers to the Primary Key of another table. 
It establishes a relationship between two tables, allowing data in one table to be linked to data in another table. 
"""

""" Q6.
A. cursor() method:
When you connect to a MySQL database in Python, the cursor() method is used to create a cursor object. The cursor object allows 
you to interact with the database and execute SQL queries. It acts as a pointer that enables you to traverse and manipulate the 
data in the database.

B. execute() method:
The execute() method is used to execute SQL queries through the cursor object. It takes an SQL query as a parameter and sends it 
to the database for execution. The execute() method is often used to perform SELECT, INSERT, UPDATE, DELETE, and other types of 
SQL operations.
"""

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)


""" Q7.
In an SQL query, the clauses are executed in the following order:
SELECT
FROM
WHERE
GROUP BY
HAVING ORDER BY
"""