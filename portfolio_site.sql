DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS project_images;

CREATE TABLE posts (
    post_id serial PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(50),
    date DATE,
    body TEXT
);

CREATE TABLE projects (
    project_id serial PRIMARY KEY,
    tech_stack VARCHAR(255),
    title VARCHAR(150),
    link TEXT,
    github TEXT
);

CREATE TABLE project_images (
    image_id serial PRIMARY KEY,
    image BYTEA
);

-- IF NEEDING TO BRING IN CSV INTO YOUR DATABASE, USE THE FOLLOWING COMMAND
-- COPY name-of-file FROM "absolute path to file" DELIMITER ",", CSV HEADER;