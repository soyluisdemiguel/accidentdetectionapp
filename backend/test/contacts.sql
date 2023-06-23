sql
Copy code
-- contacts.sql

-- Creación de la tabla de contactos de emergencia
CREATE TABLE IF NOT EXISTS contacts (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100),
phone VARCHAR(20),
FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Inserción de datos de ejemplo
INSERT INTO contacts (user_id, first_name, last_name, email, phone) VALUES
(1, 'Fernando', 'Martínez', 'fernando.martinez@example.com', '+34 123 456 789'),
(1, 'María', 'García', 'maria.garcia@example.com', '+34 123 456 788'),
(2, 'Pedro', 'González', 'pedro.gonzalez@example.com', '+34 123 456 787'),
(3, 'Laura', 'Rodríguez', 'laura.rodriguez@example.com', '+34 123 456 786'),
(4, 'Miguel', 'Martín', 'miguel.martin@example.com', '+34 123 456 785'),
(4, 'Sara', 'Hernández', 'sara.hernandez@example.com', '+34 123 456 784'),
(5, 'David', 'López', 'david.lopez@example.com', '+34 123 456 783'),
(6, 'Ana', 'Sánchez', 'ana.sanchez@example.com', '+34 123 456 782'),
(6, 'Fernando', 'Morales', 'fernando.morales@example.com', '+34 123 456 781'),
(7, 'Isabel', 'Ortiz', 'isabel.ortiz@example.com', '+34 123 456 780');
