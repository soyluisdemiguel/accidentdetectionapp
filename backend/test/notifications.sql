sql
Copy code
-- notifications.sql

-- Creación de la tabla notificaciones
CREATE TABLE IF NOT EXISTS notifications (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
event_id INT,
timestamp DATETIME,
status ENUM('read', 'unread'),
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (event_id) REFERENCES events(id)
);

-- Inserción de datos de ejemplo
INSERT INTO notifications (user_id, event_id, timestamp, status) VALUES
(1, 1, '2023-03-21 09:10:00', 'unread'),
(2, 2, '2023-03-21 10:40:00', 'unread'),
(3, 3, '2023-03-21 12:10:00', 'unread'),
(4, 4, '2023-03-21 14:10:00', 'unread'),
(5, 5, '2023-03-21 15:40:00', 'unread'),
(6, 6, '2023-03-21 16:10:00', 'unread'),
(7, 7, '2023-03-21 17:40:00', 'unread'),
(8, 8, '2023-03-21 18:10:00', 'unread'),
(9, 9, '2023-03-21 19:40:00', 'unread'),
(10, 10, '2023-03-21 20:10:00', 'unread');