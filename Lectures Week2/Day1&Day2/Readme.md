# Database Fundamentals

## 1. What is a Database?

### **Definition**  
A **database** is an organized collection of data stored electronically, managed by a **Database Management System (DBMS)**. It allows users to create, read, update, and delete data efficiently.

### **Why Use a Database?**
- To store and manage large amounts of structured data.
- Ensure data integrity and security.
- Perform operations like adding, updating, deleting, and querying data efficiently.

### **Types of Databases Include:**
- **Relational:** Uses tables (e.g., *MySQL*, *SQLite*).
- **NoSQL:** For unstructured data (e.g., *MongoDB*, *Firebase Firestore*).
- **In-memory:** Fast access (e.g., *Redis*) for gaming, machine learning, IoT applications.

Databases are used in various applications, from simple storage to complex systems.

---

## 2. What is MySQL Database?

### **MySQL Database**
**MySQL** is an open-source relational database management system (RDBMS) that uses **Structured Query Language (SQL)** to manage data. It is widely used for web applications and various business systems.

### **MySQL Database Features**
MySQL is a popular RDBMS with several key features:
- **Open Source:** Free to use and modify.
- **Cross-Platform:** Runs on various operating systems, including Windows, Linux, and macOS.
- **High Performance:** Optimized for speed, handling large volumes of data with quick response times.
- **Scalability:** Supports large databases and multiple simultaneous users.
- **Support for SQL:** Uses SQL for querying and managing data.

### **MySQL Database Structure**
A MySQL database consists of several key components:
- **Database:** A collection of related tables.
- **Tables:** Core components that store data in rows and columns, each representing a specific entity (e.g., users, products).
- **Rows:** Represent single records in the table.
- **Columns:** Represent specific attributes of data (e.g., name, age, email).
- **Schema:** Defines the structure of the database, including tables, columns, data types, and relationships.
- **Data Types:** Specify the kind of data that can be stored in each column (e.g., INT, VARCHAR, DATE).
- **Indexes:** Improve the speed of data retrieval operations.
- **Relationships:** Connections between tables, defined through primary keys and foreign keys.
    - **Primary Key:** Unique identifier for each record in a table.
    - **Foreign Key:** Links to the primary key of another table, establishing a relationship.

### **Creating a MySQL Database Using SQL Commands**
```sql
mysql -u root -p
CREATE DATABASE my_new_database;
SHOW DATABASES;
USE my_new_database;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SHOW TABLES;
SHOW COLUMNS FROM users;
EXIT;
```
### c. What is an ERD (Entity-Relationship Diagram)?
#### Definition:
An Entity-Relationship Diagram (ERD) is a visual representation of how different entities (or tables) in a database are related to each other. It helps in designing the structure of a database before implementation.

#### Why Use ERDs?
- **Visualization:** ERDs allow you to visually map out entities, attributes, and relationships before creating actual database tables.
- **Planning:** It’s an essential step in database design, ensuring that you correctly organize and structure data.
- **Communication:** ERDs are useful for explaining and discussing database designs with other developers and stakeholders.

### d. How ERDs and Databases Work Together
When designing a database, the first step is to understand the data you need to store and the relationships between different pieces of data. An ERD provides a blueprint that helps you structure the data logically before you start creating the tables and relationships in the database.

## 2. Introduction to ERDs
### a. Components of an ERD
- **Entities:** Represents a table in a database. These are the objects or things we want to store information about.  
  - *Example:* Students, Courses.
- **Attributes:** Represents fields/columns in a table. These are the pieces of information we collect about an entity.  
  - *Example:* For the Student entity, attributes might be `student_id`, `student_name`, `email`.
- **Relationships:** Shows how entities are related to each other, describing how data in one table relates to data in another table.  
  - *Example:* A Student enrolls in many Courses, and a Course can have many Students (many-to-many relationship).

### b. Data Types
#### Why data types matter:
Data types define the kind of information a field can hold, ensuring consistency and data integrity.

#### Common MySQL Data Types:
- `INT`: For whole numbers.
- `VARCHAR(n)`: For variable-length text.
- `CHAR(n)`: For fixed-length text.
- `DATE`: Stores dates only (e.g., YYYY-MM-DD).
- `DATETIME`: For dates with time (e.g., YYYY-MM-DD HH:MM:SS).
- `FLOAT` / `DECIMAL`: For decimal numbers.
- `TINYINT`: Small integers (from 0 to 9), often for boolean values (0 or 1).

#### Example:
For the `student_name` column in a Students table, the data type would be `VARCHAR(255)`, while `age` might be `INT`.

### c. Primary Keys
- **What is a Primary Key?**  
  A primary key (PK) is a unique identifier for a record in a table. It ensures that no two records have the same value for this field.

- **Why use a Primary Key?**  
  It is essential for ensuring data integrity and efficient data retrieval.
  - *Example:* `student_id` in the Students table would be a primary key because each student has a unique ID.

### d. Types of Relationships
- **One-to-One (1:1):**  
  One record in Table A is related to exactly one record in Table B.  
  *Example:* A Person can have one Passport.

- **One-to-Many (1:N):**  
  One record in Table A can be related to multiple records in Table B.  
  *Example:* A Teacher can teach many Courses.

- **Many-to-Many (N:N):**  
  Many records in Table A can be related to many records in Table B, usually requiring a junction table.  
  *Example:* Students enroll in many courses, and courses have many students (requires an Enrollment table).

### e. Naming Conventions
- **Consistency is Key:** Table names are usually plural (e.g., students, orders), while columns are singular (student_name, order_date).
- **CamelCase or Snake_Case:** Choose a naming convention for column names and stick with it throughout the database.
  - *Example:* Use `student_name` or `StudentName` but be consistent.
- **Avoid Abbreviations:** Use meaningful names to avoid confusion (course_id instead of crs_id).

## 3. Using MySQL Workbench to Create ERDs
### a. Introduction to MySQL Workbench
#### What is MySQL Workbench?
MySQL Workbench is a unified tool for database modeling, SQL development, and administration. It allows you to visually design and create database schemas using ERDs.

### b. Step-by-Step Guide to Create ERDs
1. **Open MySQL Workbench:**  
   Launch the MySQL Workbench application and navigate to the Database Modeling section.
2. **Creating a New EER Diagram:**  
   - Click on `File > New Model`.
   - From the Model Overview panel, click on `Add Diagram` to create a new ERD.

### c. Adding Entities (Tables)
1. **Adding Tables:**  
   - Click on the Table icon from the toolbar or right-click inside the diagram and choose `Create Table`.
   - A dialog will appear where you can name the table (e.g., `Students`) and add columns (e.g., `student_id`, `student_name`, `email`, `status`, `created_at`, `updated_at`).

2. **Defining Data Types:**  
   - For each column, define the data type (e.g., `student_id` as `INT`, `student_name` as `VARCHAR(255)`, `email` as `VARCHAR(255)`, `status` as `VARCHAR(255)`, `created_at` as `DATETIME`, `updated_at` as `DATETIME`).

3. **Setting Primary Keys:**  
   - Mark the `student_id` as the Primary Key (PK) by checking the PK box in the table editor.

### d. Creating Relationships
1. **Adding Foreign Keys (Relationships):**  
   - Click on the Foreign Key tool to create relationships between tables.
   - *Example:* If you have Courses and Enrollments tables, create a relationship by linking the `course_id` in Courses with the `course_id` in Enrollments.

2. **Example Relationship:**  
   - A one-to-many relationship between Students and Enrollments:
     - Each student can enroll in multiple courses (1:N).
     - You would link the `student_id` from the Students table to the `student_id` in the Enrollments table as a foreign key.

### e. Generating SQL from the ERD
1. **Forward Engineering:**  
   - Once the ERD is complete, demonstrate how to Forward Engineer the diagram to generate SQL scripts.
   - Go to `Database > Forward Engineer` and follow the steps to convert the ERD into actual database tables in MySQL.

## SQL QUERIES LECTURE
### 4. Basic SQL CRUD Queries
- **INSERT:** Inserts data into the students table.
  ```sql
  INSERT INTO students (student_name, email, status) VALUES ('Alice Johnson', 'alice.johnson@example.com', 'active');```

- **SELECT**: Retrieves all records from the `students` table.
  - Example:
    ```sql
    SELECT * FROM students;
    ```
- **SELECT with Filters**:
  - Example:
    ```sql
    SELECT * FROM students WHERE student_name = 'Alice Johnson';
    ```
- **UPDATE**: Updates the email of the student named 'Alice Johnson'.
  - Example:
    ```sql
    UPDATE students SET email = 'alicejohnson@example.com' WHERE student_name = 'Alice Johnson';
    ```
- **DELETE**: Removes the student named 'Alice Johnson' from the table.
  - Example:
    ```sql
    DELETE FROM students WHERE student_name = 'Alice Johnson';
    ```

## JOINs
- **Inner JOIN**: Combines data from `students`, `enrollments`, and `courses`.
  - Example:
    ```sql
    SELECT students.student_name, courses.title 
    FROM students 
    JOIN enrollments ON students.id = enrollments.student_id 
    JOIN courses ON enrollments.course_id = courses.id;
    ```
- **LEFT JOIN**: Returns all students, even those not enrolled in courses.
  - Example:
    ```sql
    SELECT students.student_name, courses.title 
    FROM students 
    LEFT JOIN enrollments ON students.id = enrollments.student_id 
    LEFT JOIN courses ON enrollments.course_id = courses.id;
    ```

## Other SQL Operators
- **WHERE Clause**: Filters records where the email contains 'example.com'.
  - Example:
    ```sql
    SELECT * FROM students WHERE email LIKE '%example.com';
    ```
- **ORDER BY Clause**: Sorts students by `student_name` in ascending order.
  - Example:
    ```sql
    SELECT * FROM students ORDER BY student_name ASC;
    ```
- **LIMIT/OFFSET Clause**: Retrieves 10 students starting from the 6th student.
  - Example:
    ```sql
    SELECT * FROM students ORDER BY student_name ASC LIMIT 10 OFFSET 5;
    ```


