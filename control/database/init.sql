CREATE USER dockeruser;
CREATE DATABASE dockerDB;
GRANT ALL PRIVILEGES ON DATABASE dockerDB TO dockeruser;

CREATE TABLE IF NO EXISTS only_table (
	first_value INT
);
