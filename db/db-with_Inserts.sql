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
CREATE DATABASE IF NOT EXISTS `ServidorWeb`;
USE `ServidorWeb`;

-- Volcando estructura para tabla ServidorWeb.libros
CREATE TABLE IF NOT EXISTS `libros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `isbn` varchar(50) DEFAULT NULL,
  `user` varchar(50) CHARACTER SET utf8mb4  DEFAULT NULL,
  `titulo` text CHARACTER SET utf8mb4,
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
) ENGINE=InnoDB AUTO_INCREMENT=477 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ServidorWeb.libros: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
INSERT INTO `libros` (`id`, `isbn`, `user`, `titulo`, `autores`, `publisher`, `anhopub`, `idioma`, `paginas`, `comentarios`) VALUES
	(477, '1-78110-131-0', 'admin', 'Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Pottermore Publishing', '2015', 'es', '264', '<p>Harry vive con sus horribles tíos y el insoportable primo Dudley, hasta que su ingreso en el Colegio Hogwarts de Magia y Hechicería cambia su vida para siempre. Allí aprenderá trucos y encantamientos fabulosos, y hará un puñado de buenos amigos... aunque también algunos temibles enemigos. Y, sobre todo, conocerá los secretos que lo ayudarán a cumplir con su destino.</p>'),
	(478, '2-8062-7419-2', 'admin', 'Harry Potter y la piedra filosofal de J. K. Rowling (Guía de lectura)', 'ResumenExpress.com,', 'ResumenExpress.com', '2017', 'es', '62', 'ResumenExpress.com presenta y analiza en esta guía de lectura <i>Harry Potter y la piedra filosofal</i>, el primer tomo de una saga de siete volúmenes que escribe J. K. Rowling. Este éxito mundial narra la historia de Harry Potter, un chico que descubre el mundo de los magos y, junto a sus amigos, tendrá que resolver el misterio de la piedra filosofal y derrotar al malvado Voldemort, que parece aterrar a todo el mundo...<br><br><b>¡Ya no tienes que leer y resumir todo el libro, nosotros lo hemos hecho por ti!</b><br><br>Esta guía incluye:<br><br>• Un resumen completo del libro<br>• Un estudio de los personajes<br>• Las claves de lectura<br>• Pistas para la reflexión<br><br><i>¿Por qué elegir ResumenExpress.com?</i> <br>Para aprender de forma rápida. Porque nuestras publicaciones están escritas con un estilo claro y conciso que te ayudará a ganar tiempo y a entender las obras sin esfuerzo. Disponibles en formato impreso y digital, te acompañarán en tu aventura literaria.<br><br><i><b>Toma una dosis de literatura acelerada con ResumenExpress.com</b></i><br>'),
	(479, '1-78110-135-3', 'admin', 'Harry Potter y la Orden del Fénix', 'J.K. Rowling', 'Pottermore Publishing', '2015', 'es', '928', '<p>«Compartes los pensamientos y las emociones con el Señor Tenebroso. El director cree que no es conveniente que eso continúe ocurriendo. Quiere que te enseñe a cerrar tu mente al Señor Tenebroso.»<br><br>La oscuridad se ciñe sobre Hogwarts. Tras el ataque de los dementores a su primo Dudley, Harry Potter sabe que Voldemort no se detendrá ante nada hasta dar con él. Hay muchos que niegan la vuelta del Señor Tenebroso, pero Harry no está solo: una orden secreta se reúne en Grimmauld Place para luchar contra las fuerzas oscuras. Harry debe permitir que el profesor Snape le enseñe a protegerse contra los brutales ataques de Voldemort a su mente. Pero cada día son más fuertes y Harry se está quedando sin tiempo...<br><br><i>Tema musical compuesto por James Hannigan.</i></p>'),
	(480, '956-142116-X', 'admin', 'El Quijote. Versión abreviada y adaptada al español de América', 'Miguel de Cervantes', 'Ediciones UC', '2017', 'en', '576', 'Esta nueva versión del clásico cervantino adapta el lenguaje de la obra al español actual de América. De esta manera, permite a los lectores disfrutar del conjunto de su trama y de su humor, sin las dificultades que genera la distancia temporal con el español del tiempo en que fue escrito y con la realidad histórico-cultural de la España de 1.605. La edición mantiene la trama central de El ingenioso hidalgo Don Quijote de la Mancha, y prescinde de las historias intercaladas que se alejan de la historia central.'),
	(481, '', 'admin', 'Primera y segunda parte de el Leon de Espana', 'Pedro de la Vecilla Castellanos', 'Juan Fernandez', '1586', 'es', '812', '');
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla ServidorWeb.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8mb4  DEFAULT NULL,
  `password` text CHARACTER SET utf8mb4 ,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ServidorWeb.usuarios: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id`, `nombre`, `password`) VALUES
	(92, 'admin', '713bfda78870bf9d1b261f565286f85e97ee614efe5f0faf7c34e7ca4f65baca'),
	(93, 'normal', '7bf24d6ca2242430343ab7e3efb89559a47784eea1123be989c1b2fb2ef66e83');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
CREATE USER IF NOT EXISTS 'tellico-synchronized'@'localhost' IDENTIFIED WITH mysql_native_password BY 'proyecto-nicolas';
GRANT ALL ON `ServidorWeb`.* TO 'tellico-synchronized'@'localhost';
