-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.22-0ubuntu0.20.10.2 - (Ubuntu)
-- SO del servidor:              Linux
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para ServidorWeb
CREATE DATABASE IF NOT EXISTS `ServidorWeb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ServidorWeb`;

-- Volcando estructura para tabla ServidorWeb.libros
CREATE TABLE IF NOT EXISTS `libros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `isbn` varchar(50) DEFAULT NULL,
  `user` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `titulo` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `autores` text,
  `publisher` varchar(50) DEFAULT NULL,
  `anhopub` varchar(16) DEFAULT NULL,
  `idioma` varchar(50) DEFAULT NULL,
  `paginas` varchar(16) DEFAULT NULL,
  `comentarios` text,
  PRIMARY KEY (`id`),
  KEY `isbn` (`isbn`),
  KEY `FK_libros_usuarios` (`user`),
  CONSTRAINT `FK_libros_usuarios` FOREIGN KEY (`user`) REFERENCES `usuarios` (`nombre`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=477 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla ServidorWeb.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `password` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
CREATE USER IF NOT EXISTS 'tellico-synchronized'@'localhost' IDENTIFIED WITH mysql_native_password BY 'proyecto-nicolas';
GRANT ALL ON `ServidorWeb`.* TO 'tellico-synchronized'@'localhost';