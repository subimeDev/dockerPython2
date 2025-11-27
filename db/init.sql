-- Docker Compose ya creó la base de datos 'testdb' (ver environment),
-- así que solo necesitamos USARLA.
USE testdb;

-- Crea una tabla de ejemplo
CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserta algunos datos de ejemplo
INSERT INTO usuarios (nombre) VALUES ('Ana de Docker');
INSERT INTO usuarios (nombre) VALUES ('Juan Compositor');
