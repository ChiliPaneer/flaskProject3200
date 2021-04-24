-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: python_test
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `logs`
--

DROP TABLE IF EXISTS `logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sic_time` decimal(10,1) DEFAULT NULL,
  `total_time` decimal(10,1) DEFAULT NULL,
  `pic_time` decimal(10,1) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `night_time` decimal(10,1) DEFAULT NULL,
  `day_time` decimal(10,1) DEFAULT NULL,
  `xc_time` decimal(10,1) DEFAULT NULL,
  `dual_received` decimal(10,1) DEFAULT NULL,
  `dual_given` decimal(10,1) DEFAULT NULL,
  `actual_instrument` decimal(10,1) DEFAULT NULL,
  `simulated_instrument` decimal(10,1) DEFAULT NULL,
  `departure` varchar(4) DEFAULT NULL,
  `destination` varchar(4) DEFAULT NULL,
  `via` varchar(4) DEFAULT NULL,
  `day_landings` int DEFAULT NULL,
  `night_landings` int DEFAULT NULL,
  `num_instrument_approaches` int DEFAULT NULL,
  `remarks` varchar(300) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `aircraft_id` int DEFAULT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id_idx` (`user_id`),
  KEY `aircraft_id_idx` (`aircraft_id`),
  CONSTRAINT `logs_to_aircrafts` FOREIGN KEY (`aircraft_id`) REFERENCES `aircrafts` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `logs_to_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logs`
--

LOCK TABLES `logs` WRITE;
/*!40000 ALTER TABLE `logs` DISABLE KEYS */;
INSERT INTO `logs` VALUES (8,NULL,1.2,NULL,'2021-04-24 00:00:00',NULL,1.2,NULL,1.2,NULL,NULL,NULL,'KLWM','KBOS','2B2',2,NULL,NULL,'Landed at Logan Airport',3,1,'2021-04-24 10:52:11','2021-04-24 10:52:11'),(10,NULL,1.3,NULL,'2021-04-24 00:00:00',NULL,1.3,NULL,1.3,NULL,NULL,NULL,'KBOS','KLWM','KBVY',NULL,NULL,NULL,'Back to Lawrence',3,6,'2021-04-24 10:53:59','2021-04-24 10:53:59'),(11,NULL,0.8,NULL,'2021-04-25 00:00:00',NULL,NULL,NULL,0.8,NULL,NULL,NULL,'KLWM','KLWM',NULL,5,NULL,NULL,'Practice Traffic Patterns',3,1,'2021-04-24 10:54:32','2021-04-24 10:54:32'),(12,NULL,1.0,1.0,'2021-04-22 00:00:00',NULL,1.0,NULL,1.0,NULL,NULL,NULL,'KLWM','KLWM',NULL,5,NULL,NULL,'Practice engine failures',5,1,'2021-04-24 11:01:23','2021-04-24 11:01:23'),(13,NULL,1.1,1.1,'2021-04-23 00:00:00',NULL,1.1,NULL,NULL,NULL,NULL,NULL,'KLWM','KLWM','KPSM',2,NULL,NULL,'Passenges landed at Portsmouth',5,1,'2021-04-24 11:02:53','2021-04-24 11:02:53'),(14,NULL,0.8,NULL,'2021-04-24 00:00:00',NULL,0.8,NULL,0.8,NULL,NULL,NULL,'KOWD','KBED',NULL,1,NULL,NULL,'quick flight from Norwood to Bedford',6,6,'2021-04-24 11:03:57','2021-04-24 11:03:57'),(15,NULL,0.9,NULL,'2021-04-24 00:00:00',NULL,0.9,NULL,0.9,NULL,NULL,NULL,'KBED','KLWM',NULL,1,NULL,NULL,'Back to lawrence',6,6,'2021-04-24 11:05:14','2021-04-24 11:05:14');
/*!40000 ALTER TABLE `logs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-24 11:11:29
