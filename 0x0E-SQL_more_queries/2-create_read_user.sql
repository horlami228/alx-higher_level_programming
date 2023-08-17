-- create a new database
-- create a new user
-- grant them SELECT privilege to the database

CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_2`;

CREATE USER
    IF NOT EXISTS `user_0d_2`@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON `user_0d_2.*`
    TO `user_0d_2`@'localhost';

FLUSH PRIVILEGES;
