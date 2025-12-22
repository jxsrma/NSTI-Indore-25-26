create database NSTIAdvanceQueries;
use NSTIAdvanceQueries;
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    marks INT
);
CREATE TABLE student_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    message VARCHAR(100),
    log_time DATETIME
);

-- Trigger
DELIMITER $$

CREATE TRIGGER after_student_insert
AFTER INSERT ON students
FOR EACH ROW
BEGIN
    INSERT INTO student_log (student_id, message, log_time)
    VALUES (
        NEW.student_id,
        CONCAT('New student added: ', NEW.student_name),
        NOW()
    );
END $$

DELIMITER ;

-- Storage Process
DELIMITER $$

CREATE PROCEDURE GetStudentsAboveMarks(IN min_marks INT)
BEGIN
    SELECT student_id, student_name, marks
    FROM students
    WHERE marks > min_marks;
END $$

DELIMITER ;


INSERT INTO students VALUES
(1, 'Rahul', 85),
(2, 'Neha', 72),
(3, 'Amit', 45),
(4, 'Pooja', 90);

select * from students;
select * from student_log;

-- Using Storage Procedure!!
CALL GetStudentsAboveMarks(70);
CALL GetStudentsAboveMarks(80);
CALL GetStudentsAboveMarks(90);


-- Function
DELIMITER $$

CREATE FUNCTION GetResult(m INT)
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    DECLARE result VARCHAR(10);

    IF m >= 50 THEN
        SET result = 'PASS';
    ELSE
        SET result = 'FAIL';
    END IF;

    RETURN result;
END $$

DELIMITER ;

select Upper(student_name), GetResult(marks) from students;