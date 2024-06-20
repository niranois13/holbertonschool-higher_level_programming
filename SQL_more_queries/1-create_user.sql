-- creates and grants all privileges to user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH authentication_plugin BY 'user_0d_1_pwd';
GRANTS ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost';