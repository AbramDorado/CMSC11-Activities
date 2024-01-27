-- Lab Exercise 9
--Write a SQL query to answer each of the following questions.

--1. In what year was Jerry Seinfeld born?

SELECT birth FROM "people" WHERE name="Jerry Seinfeld";

--2. How many shows have started in 1970?

SELECT COUNT(title) FROM "shows" WHERE year="1970";

--3. How many shows have 10-star rating?

SELECT COUNT(rating) FROM "ratings" WHERE rating="10";

--4. In what year "Arrested Development" was released?

SELECT year FROM "shows" WHERE title="Arrested Development";

--5. How many shows end with "development"

SELECT COUNT(title) FROM "shows" WHERE title like "%development";
