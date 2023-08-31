-- Sets up a MySQL server for the project
CREATE DATABASE IF NOT EXISTS podshare_v1;
CREATE USER IF NOT EXISTS 'podshare_dev'@'localhost' IDENTIFIED BY 'podshare_dev_pwd';
ALTER USER 'podshare_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'podshare_dev_pwd';
GRANT ALL PRIVILEGES ON podshare_v1.* TO 'podshare_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'podshare_dev'@'localhost';
FLUSH PRIVILEGES;
