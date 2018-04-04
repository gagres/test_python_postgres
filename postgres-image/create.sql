-- Just a script to create database table structure
CREATE TABLE Persons (
    PersonId INT PRIMARY KEY, 
    PersonName VARCHAR(255)
);

INSERT INTO Persons VALUES (1, 'Gabriel');
INSERT INTO Persons VALUES (2, 'Marcelo');