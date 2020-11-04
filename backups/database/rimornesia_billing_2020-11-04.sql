# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.31)
# Database: rimornesia_billing
# Generation Time: 2020-11-04 15:12:38 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table payment
# ------------------------------------------------------------

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(100) DEFAULT '',
  `user_id` int(100) DEFAULT NULL,
  `amount` bigint(20) DEFAULT NULL,
  `unique_code` int(20) DEFAULT NULL,
  `booking_id` int(100) DEFAULT NULL,
  `booking_code` varchar(100) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `transaction_id` text,
  `transaction_time` datetime DEFAULT NULL,
  `transaction_status` varchar(50) DEFAULT NULL,
  `payment_token` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table payment_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `payment_log`;

CREATE TABLE `payment_log` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT,
  `action` varchar(50) DEFAULT NULL,
  `value` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table payment_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `payment_session`;

CREATE TABLE `payment_session` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT,
  `token` varchar(100) DEFAULT NULL,
  `expired` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
