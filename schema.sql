-- Author: Kevin Lu
-- Date: 10/2/2019
-- File: schema.sql
-- Purpose: Create the table for us.
-- Modification: N/A

DROP TABLE IF EXISTS users;
    CREATE TABLE users (
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);