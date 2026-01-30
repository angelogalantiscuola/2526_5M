DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS bookmark;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE bookmark (
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, post_id),
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (post_id) REFERENCES post (id)
);

INSERT INTO user (username, password) VALUES ('admin', 'adminpass');
INSERT INTO user (username, password) VALUES ('student', 'studentpass');

INSERT INTO post (author_id, title, body, created) VALUES (1, 'Welcome to the Blog', 'This is the first post on the blog!', '2024-01-15 10:30:00');
INSERT INTO post (author_id, title, body, created) VALUES (2, 'Hello World', 'This is a post by a student.', '2024-03-20 14:15:00');
INSERT INTO post (author_id, title, body, created) VALUES (1, 'Second Post', 'Another post by the admin user.', '2024-11-10 09:45:00');
INSERT INTO post (author_id, title, body, created) VALUES (2, 'Learning SQL', 'This post discusses basic SQL commands.', '2025-05-05 16:20:00');
INSERT INTO post (author_id, title, body, created) VALUES (1, 'Database Design', 'An introduction to designing databases.', '2026-01-27 11:00:00');
