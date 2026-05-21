CREATE DATABASE attendance_db;

USE attendance_db;

CREATE TABLE attendance_new (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    time VARCHAR(20),
    date DATE,
    UNIQUE (name, date)
);

SELECT * FROM attendance_new;