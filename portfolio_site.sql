-- DROP TABLE IF EXISTS posts;
-- DROP TABLE IF EXISTS projects;
-- DROP TABLE IF EXISTS project_images;
DROP TABLE IF EXISTS mock_data;

-- CREATE TABLE posts (
--     post_id serial PRIMARY KEY,
--     title VARCHAR(100),
--     author VARCHAR(50),
--     date DATE,
--     body TEXT
-- );

-- CREATE TABLE projects (
--     project_id serial PRIMARY KEY,
--     tech_stack VARCHAR(255),
--     title VARCHAR(150),
--     link TEXT,
--     github TEXT
-- );

-- CREATE TABLE project_images (
--     image_id serial PRIMARY KEY,
--     image BYTEA
-- );


CREATE TABLE mock_data (
    id serial PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(35),
    ip_address VARCHAR(20),
    gender VARCHAR(6)
);

COPY mock_data FROM "/home/neka/projects/portfolio-site/data/data.csv" DELIMITER "," CSV HEADER;

-- \COPY mock_data FROM "/home/neka/projects/portfolio-site/data/data.csv" DELIMITER "," CSV HEADER; --in case above command does not work, use backslash and then entire command, i kept receiving permission denied errors when using w/o backslash at beginning of command

-- IF NEEDING TO BRING IN CSV INTO YOUR DATABASE, USE THE FOLLOWING COMMAND
-- COPY name-of-table FROM "absolute path to file" DELIMITER ",", CSV HEADER;
                                                                    -- ^^ this tells postgresql that the very first line is the header in csv and everything else reflects that by commas