

-- Create the Student Database with fields
CREATE TABLE Student (
    student_name VARCHAR(100),
    roll_number INT PRIMARY KEY,
    class VARCHAR(50),
    phone_number VARCHAR(15),
    total_marks INT
);


-- ALTER table to add new attributes/ modify data type/ drop attribute
    --- Add new attributes
    ALTER TABLE Student
    ADD email VARCHAR(100),
    address VARCHAR(255);

    --- Modify Data Types
    ALTER TABLE Student
    MODIFY phone_number VARCHAR(20);

    --- Drop an attribute
    ALTER TABLE Student
    DROP COLUMN address;


-- UPDATE table to modify data
    --- Update a specific student's data
    UPDATE Student
    SET total_marks = 85
    WHERE roll_number = 101;

    --- Update multiple columns for a specific student
    UPDATE Student
    SET phone_number = '1234567890', class = '12B'
    WHERE roll_number = 102;

    --- Update data for all students
    UPDATE Student
    SET total_marks = total_marks + 5;


-- ORDER By to display data in ascending / desecending order
    --- Display data in ascending order
    SELECT * FROM Student
    ORDER BY roll_number ASC;

    --- Display data in descending order
    SELECT * FROM Student
    ORDER BY roll_number DESC;


-- Delete to remove tuple(s)
    --- Delete a specific row
    DELETE FROM Student
    WHERE roll_number = 101;

    --- Delete multiple rows on a condition
    DELETE FROM Student
    WHERE class = '10A';

    --- Delete all rows from the table
    DELETE FROM Student;

-- Group BY and find the min, max, sum, count and avarage
SELECT class,
       MIN(total_marks) AS MinMarks,
       MAX(total_marks) AS MaxMarks,
       SUM(total_marks) AS TotalMarks,
       COUNT(*) AS StudentCount,
       AVG(total_marks) AS AverageMarks
FROM Student
GROUP BY class;
