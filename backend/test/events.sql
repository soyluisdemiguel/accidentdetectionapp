-- events.sql

-- Creación de la tabla eventos
CREATE TABLE IF NOT EXISTS events (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  event_type ENUM('accident', 'theft', 'public_disturbance', 'medical_emergency'),
  description TEXT,
  latitude DECIMAL(9,6),
  longitude DECIMAL(9,6),
  timestamp DATETIME,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Inserción de datos de ejemplo
INSERT INTO events (user_id, event_type, description, latitude, longitude, timestamp) VALUES
(1, 'accident', 'Accidente de tráfico en la calle Gran Vía', 40.420200, -3.703450, '2023-03-21 09:00:00'),
(2, 'theft', 'Robo de cartera en la calle Fuencarral', 40.422100, -3.701980, '2023-03-21 10:30:00'),
(3, 'public_disturbance', 'Altercado en la plaza Sol', 40.416775, -3.703790, '2023-03-21 12:00:00'),
(4, 'medical_emergency', 'Persona desmayada en la calle Preciados', 40.419000, -3.705230, '2023-03-21 14:00:00'),
(5, 'accident', 'Accidente de moto en la calle Princesa', 40.422900, -3.706670, '2023-03-21 15:30:00'),
(6, 'theft', 'Robo de bicicleta en la calle Atocha', 40.420800, -3.704120, '2023-03-21 16:00:00'),
(7, 'public_disturbance', 'Manifestación en la calle Alcalá', 40.418700, -3.701570, '2023-03-21 17:30:00'),
(8, 'medical_emergency', 'Persona con dificultades para respirar en la calle Hortaleza', 40.416600, -3.699020, '2023-03-21 18:00:00'),
(9, 'accident', 'Accidente laboral en la calle Serrano', 40.414500, -3.696470, '2023-03-21 19:30:00'),
(10, 'theft', 'Robo de móvil en la calle Montera', 40.412400, -3.693920, '2023-03-21 20:00:00');
