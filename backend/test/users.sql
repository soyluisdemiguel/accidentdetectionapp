-- users.sql

-- Creación de la tabla usuarios
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(255),
  phone VARCHAR(20),
  role ENUM('citizen', 'police', 'emergency_services'),
  latitude DECIMAL(9,6),
  longitude DECIMAL(9,6)
);

-- Inserción de datos de ejemplo
INSERT INTO users (first_name, last_name, email, password, phone, role, latitude, longitude) VALUES
('Juan', 'Pérez', 'juan.perez@example.com', 'encrypted_password', '+34 123 456 789', 'citizen', 40.416775, -3.703790),
('Maria', 'García', 'maria.garcia@example.com', 'encrypted_password', '+34 123 456 788', 'citizen', 40.419200, -3.700345),
('Pedro', 'González', 'pedro.gonzalez@example.com', 'encrypted_password', '+34 123 456 787', 'police', 40.417000, -3.701120),
('Laura', 'Rodríguez', 'laura.rodriguez@example.com', 'encrypted_password', '+34 123 456 786', 'emergency_services', 40.415600, -3.698500),
('Miguel', 'Martín', 'miguel.martin@example.com', 'encrypted_password', '+34 123 456 785', 'citizen', 40.418300, -3.704560),
('Ana', 'Sánchez', 'ana.sanchez@example.com', 'encrypted_password', '+34 123 456 784', 'citizen', 40.420100, -3.702230),
('David', 'López', 'david.lopez@example.com', 'encrypted_password', '+34 123 456 783', 'citizen', 40.413900, -3.705890),
('Sara', 'Hernández', 'sara.hernandez@example.com', 'encrypted_password', '+34 123 456 782', 'police', 40.416300, -3.707560),
('Fernando', 'Morales', 'fernando.morales@example.com', 'encrypted_password', '+34 123 456 781', 'emergency_services', 40.417700, -3.709230),
('Isabel', 'Ortiz', 'isabel.ortiz@example.com', 'encrypted_password', '+34 123 456 780', 'citizen', 40.419100, -3.710900);
