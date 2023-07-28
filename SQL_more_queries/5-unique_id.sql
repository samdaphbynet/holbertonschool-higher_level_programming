-- Create the table unique id in Mysql server.
CREATE TABLE 
    IF NOT EXISTS unique_id(
        id INT NOT NULL DEFAULT 1, 
        name VARCHAR(256),
        UNIQUE INDEX(id));