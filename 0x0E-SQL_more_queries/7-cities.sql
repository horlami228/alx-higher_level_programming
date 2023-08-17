-- create database hbtn_0d_usa
-- create a table states in hbtn_0d_usa


CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

USE `hbtn_0d_usa`;

CREATE TABLE
    IF NOT EXISTS `cities`
    (id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states.id
    );
