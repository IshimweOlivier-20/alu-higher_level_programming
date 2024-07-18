-- A script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
CREATE USER 'user_0d_1'@'localhost'
CREATE USER 'user_0d_2'@'localhost'
SHOW GRANT FOR 'user_0d_1'@'localhost';
SHOW GRANT FOR 'user_0d_2'@'localhost';
