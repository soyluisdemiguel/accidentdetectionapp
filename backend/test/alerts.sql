sql
Copy code
-- alerts.sql

-- Creación de la tabla alertas
CREATE TABLE IF NOT EXISTS alerts (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
event_type ENUM('accident', 'theft', 'public_disturbance', 'medical_emergency'),
geofence_radius INT,
latitude DECIMAL(9,6),
longitude DECIMAL(9,6),
FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Inserción de datos de ejemplo
INSERT INTO alerts (user_id, event_type, geofence_radius, latitude, longitude) VALUES
(1, 'accident', 1000, 40.416775, -3.703790),
(2, 'medical_emergency', 500, 40.419200, -3.700345),
(3, 'theft', 800, 40.417000, -3.701120),
(4, 'public_disturbance', 700, 40.415600, -3.698500),
(5, 'accident', 900, 40.418300, -3.704560),
(6, 'medical_emergency', 1000, 40.420100, -3.702230),
(7, 'theft', 600, 40.413900, -3.705890),
(8, 'public_disturbance', 800, 40.416300, -3.707560),
(9, 'accident', 700, 40.417700, -3.709230),
(10, 'medical_emergency', 1200, 40.419100, -3.710900);