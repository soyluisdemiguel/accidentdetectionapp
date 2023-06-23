sql
Copy code
-- user_events.sql

-- Creación de la tabla de relaciones entre usuarios y eventos
CREATE TABLE IF NOT EXISTS user_events (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
event_id INT,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (event_id) REFERENCES events(id)
);

-- Inserción de datos de ejemplo
INSERT INTO user_events (user_id, event_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);