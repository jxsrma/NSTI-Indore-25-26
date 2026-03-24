-- Create the database
CREATE DATABASE movies_db;
USE movies_db;

-- Create the genres table
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL UNIQUE
);

-- Create the directors table
CREATE TABLE directors (
    director_id INT AUTO_INCREMENT PRIMARY KEY,
    director_name VARCHAR(255) NOT NULL UNIQUE
);

-- Create the movies table
CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year YEAR NOT NULL,
    genre_id INT,
    director_id INT,
    duration INT,  -- Duration in minutes
    rating DECIMAL(3,1),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

-- Create the actors table
CREATE TABLE actors (
    actor_id INT AUTO_INCREMENT PRIMARY KEY,
    actor_name VARCHAR(255) NOT NULL UNIQUE
);

-- Create the movie_cast table
CREATE TABLE movie_cast (
    movie_id INT,
    actor_id INT,
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
);

-- Create the ratings table
CREATE TABLE ratings (
    movie_id INT,
    user_id INT,
    rating DECIMAL(3,1) CHECK (rating >= 0 AND rating <= 10),
    review_date DATE,
    PRIMARY KEY (movie_id, user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

-- Insert sample data into genres
INSERT INTO genres (genre_name) VALUES ('Action'), ('Comedy'), ('Drama'), ('Sci-Fi'), ('Horror'), ('Thriller'), ('Romance'), ('Fantasy'), ('Mystery'), ('Adventure');

-- Insert sample data into directors
INSERT INTO directors (director_name) VALUES ('Christopher Nolan'), ('Quentin Tarantino'), ('Steven Spielberg'), ('Martin Scorsese'), ('James Cameron'), ('Ridley Scott'), ('Peter Jackson'), ('Stanley Kubrick'), ('Francis Ford Coppola'), ('David Fincher');

-- Insert sample data into movies
INSERT INTO movies (title, release_year, genre_id, director_id, duration, rating) VALUES
('Inception', 2010, 4, 1, 148, 8.8),
('Pulp Fiction', 1994, 1, 2, 154, 8.9),
('Jurassic Park', 1993, 4, 3, 127, 8.1),
('Titanic', 1997, 7, 5, 195, 7.8),
('The Dark Knight', 2008, 6, 1, 152, 9.0),
('The Godfather', 1972, 3, 9, 175, 9.2),
('Fight Club', 1999, 6, 10, 139, 8.8),
('Forrest Gump', 1994, 7, 4, 142, 8.8),
('The Matrix', 1999, 4, 6, 136, 8.7),
('Avatar', 2009, 8, 5, 162, 7.9);

-- Insert sample data into actors
INSERT INTO actors (actor_name) VALUES ('Leonardo DiCaprio'), ('Samuel L. Jackson'), ('Tom Hanks'), ('Robert De Niro'), ('Morgan Freeman'), ('Brad Pitt'), ('Johnny Depp'), ('Matt Damon'), ('Scarlett Johansson'), ('Meryl Streep');

-- Insert sample data into movie_cast
INSERT INTO movie_cast (movie_id, actor_id) VALUES
(1, 1), (2, 2), (3, 3), (4, 1), (5, 1), (6, 4), (7, 6), (8, 3), (9, 5), (10, 7);

-- Insert sample data into ratings
INSERT INTO ratings (movie_id, user_id, rating, review_date) VALUES
(1, 101, 9.0, '2024-02-01'),
(2, 102, 8.5, '2024-02-02'),
(3, 103, 7.8, '2024-02-03'),
(4, 104, 7.9, '2024-02-04'),
(5, 105, 9.1, '2024-02-05'),
(6, 106, 9.3, '2024-02-06'),
(7, 107, 8.6, '2024-02-07'),
(8, 108, 8.7, '2024-02-08'),
(9, 109, 8.4, '2024-02-09'),
(10, 110, 7.9, '2024-02-10');