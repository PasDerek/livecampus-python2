-- MariaDB dump 10.19  Distrib 10.11.4-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: projet
-- ------------------------------------------------------
-- Server version	10.11.4-MariaDB-1~deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add etudiants',7,'add_etudiants'),
(26,'Can change etudiants',7,'change_etudiants'),
(27,'Can delete etudiants',7,'delete_etudiants'),
(28,'Can view etudiants',7,'view_etudiants'),
(29,'Can add formulaires',8,'add_formulaires'),
(30,'Can change formulaires',8,'change_formulaires'),
(31,'Can delete formulaires',8,'delete_formulaires'),
(32,'Can view formulaires',8,'view_formulaires'),
(33,'Can add reponses formulaire',9,'add_reponsesformulaire'),
(34,'Can change reponses formulaire',9,'change_reponsesformulaire'),
(35,'Can delete reponses formulaire',9,'delete_reponsesformulaire'),
(36,'Can view reponses formulaire',9,'view_reponsesformulaire'),
(37,'Can add etudiant',10,'add_etudiant'),
(38,'Can change etudiant',10,'change_etudiant'),
(39,'Can delete etudiant',10,'delete_etudiant'),
(40,'Can view etudiant',10,'view_etudiant'),
(41,'Can add formulaire',11,'add_formulaire'),
(42,'Can change formulaire',11,'change_formulaire'),
(43,'Can delete formulaire',11,'delete_formulaire'),
(44,'Can view formulaire',11,'view_formulaire');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES
(1,'pbkdf2_sha256$720000$5xZnH9rM5SqEBbIJijIec7$t/AXKt2DEke3bwOjzrRiCIO+KJNZsGgefIg7YHJJ+Kg=','2024-02-11 12:38:48.000000',1,'admin','','','',1,1,'2024-02-06 20:40:21.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES
(1,'2024-02-06 21:27:39.000000','1','Formulaire object (1)',1,'[{\"added\": {}}]',11,1),
(2,'2024-02-06 22:15:15.000000','1','Formulaire object (1)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(3,'2024-02-06 22:15:21.000000','1','Formulaire object (1)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(4,'2024-02-06 22:16:15.000000','1','Formulaire object (1)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(5,'2024-02-06 22:16:21.000000','1','Formulaire object (1)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(6,'2024-02-07 19:20:22.000000','1','Etudiant object (1)',1,'[{\"added\": {}}]',10,1),
(7,'2024-02-07 20:55:40.000000','2','Etudiant object (2)',1,'[{\"added\": {}}]',10,1),
(8,'2024-02-07 22:36:45.000000','1','Formulaire object (1)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(9,'2024-02-10 12:31:42.000000','3','Etudiant object (3)',1,'[{\"added\": {}}]',10,1),
(10,'2024-02-10 12:32:07.000000','1','Etudiant object (1)',2,'[]',10,1),
(11,'2024-02-10 12:32:15.000000','2','Etudiant object (2)',2,'[{\"changed\": {\"fields\": [\"Password\"]}}]',10,1),
(12,'2024-02-10 12:32:28.000000','2','Etudiant object (2)',2,'[{\"changed\": {\"fields\": [\"Password\"]}}]',10,1),
(13,'2024-02-10 12:44:43.000000','1','Formulaire object (1)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(14,'2024-02-10 12:44:50.000000','1','Formulaire object (1)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(15,'2024-02-10 14:21:25.000000','3','Etudiant object (3)',3,'',10,1),
(16,'2024-02-10 14:24:39.000000','1','Etudiant object (1)',2,'[{\"changed\": {\"fields\": [\"Password\"]}}]',10,1),
(17,'2024-02-10 14:24:52.000000','2','Etudiant object (2)',2,'[{\"changed\": {\"fields\": [\"Password\"]}}]',10,1),
(18,'2024-02-10 18:09:53.000000','1','Formulaire object (1)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(19,'2024-02-11 10:53:03.000000','2','Formulaire object (2)',1,'[{\"added\": {}}]',11,1),
(20,'2024-02-11 10:54:04.000000','2','Formulaire object (2)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1),
(21,'2024-02-11 12:38:56.000000','2','Formulaire object (2)',2,'[{\"changed\": {\"fields\": [\"Ouvert\"]}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(10,'mon_projet','etudiant'),
(7,'mon_projet','etudiants'),
(11,'mon_projet','formulaire'),
(8,'mon_projet','formulaires'),
(9,'mon_projet','reponsesformulaire'),
(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2024-02-06 20:40:02.000000'),
(2,'auth','0001_initial','2024-02-06 20:40:02.000000'),
(3,'admin','0001_initial','2024-02-06 20:40:02.000000'),
(4,'admin','0002_logentry_remove_auto_add','2024-02-06 20:40:02.000000'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-02-06 20:40:02.000000'),
(6,'contenttypes','0002_remove_content_type_name','2024-02-06 20:40:02.000000'),
(7,'auth','0002_alter_permission_name_max_length','2024-02-06 20:40:02.000000'),
(8,'auth','0003_alter_user_email_max_length','2024-02-06 20:40:02.000000'),
(9,'auth','0004_alter_user_username_opts','2024-02-06 20:40:02.000000'),
(10,'auth','0005_alter_user_last_login_null','2024-02-06 20:40:02.000000'),
(11,'auth','0006_require_contenttypes_0002','2024-02-06 20:40:02.000000'),
(12,'auth','0007_alter_validators_add_error_messages','2024-02-06 20:40:02.000000'),
(13,'auth','0008_alter_user_username_max_length','2024-02-06 20:40:02.000000'),
(14,'auth','0009_alter_user_last_name_max_length','2024-02-06 20:40:02.000000'),
(15,'auth','0010_alter_group_name_max_length','2024-02-06 20:40:02.000000'),
(16,'auth','0011_update_proxy_permissions','2024-02-06 20:40:02.000000'),
(17,'auth','0012_alter_user_first_name_max_length','2024-02-06 20:40:02.000000'),
(18,'sessions','0001_initial','2024-02-06 20:40:02.000000'),
(19,'mon_projet','0001_initial','2024-02-06 20:43:22.000000'),
(20,'mon_projet','0002_etudiant_email','2024-02-06 20:51:49.000000'),
(21,'mon_projet','0003_alter_etudiant_email','2024-02-06 20:53:11.000000'),
(22,'mon_projet','0004_rename_statut_formulaire_ouvert_and_more','2024-02-06 21:00:51.000000'),
(23,'mon_projet','0005_reponsesformulaire_maitrise','2024-02-06 21:00:51.000000'),
(24,'mon_projet','0006_alter_formulaire_date_ouverture_and_more','2024-02-06 21:07:42.000000'),
(25,'mon_projet','0007_alter_formulaire_options','2024-02-06 21:25:09.000000'),
(26,'mon_projet','0008_alter_formulaire_date_fermeture','2024-02-06 21:27:27.000000'),
(27,'mon_projet','0009_formulaire_nom_formulaire','2024-02-10 12:41:44.000000'),
(28,'mon_projet','0010_alter_formulaire_date_fermeture','2024-02-10 12:44:09.000000'),
(29,'mon_projet','0011_alter_etudiant_password','2024-02-10 14:19:06.000000'),
(30,'mon_projet','0012_alter_etudiant_password','2024-02-10 14:22:15.000000'),
(31,'mon_projet','0013_alter_etudiant_password','2024-02-10 14:24:07.000000'),
(32,'mon_projet','0014_alter_reponsesformulaire_difficulte_and_more','2024-02-11 12:45:27.000000'),
(33,'mon_projet','0015_reponsesformulaire_date_acces','2024-02-11 13:12:15.000000'),
(34,'mon_projet','0016_remove_reponsesformulaire_date_acces','2024-02-11 13:30:39.000000'),
(35,'mon_projet','0017_reponsesformulaire_date_access','2024-02-11 14:01:15.000000'),
(36,'mon_projet','0018_alter_reponsesformulaire_progression','2024-02-11 14:28:59.000000'),
(37,'mon_projet','0019_alter_reponsesformulaire_progression','2024-02-11 14:29:57.000000');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('r20750361yhs06yqsthn8rs43zxt0u4k','.eJxVjDsOwjAQRO_iGlkb_IlNSc8ZrN31GgeQI-VTIe5OIqWAcua9mbdKuC41rbNMacjqojp1-u0I-SltB_mB7T5qHtsyDaR3RR901rcxy-t6uH8HFee6rW3XB7KGnImRnQ0YHDjPZ8-AZAWhMOUOSjQRC8hGDWwRQvDCWXr1-QLKnjea:1rZ96e:njf9ncpNqFcy6LEfoHvY75kaMvF9rGP8s2kTnW3tunM','2024-02-25 12:38:48.000000');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mon_projet_etudiant`
--

DROP TABLE IF EXISTS `mon_projet_etudiant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mon_projet_etudiant` (
  `numero_etudiant` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`numero_etudiant`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mon_projet_etudiant_email_4f9e2abe_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mon_projet_etudiant`
--

LOCK TABLES `mon_projet_etudiant` WRITE;
/*!40000 ALTER TABLE `mon_projet_etudiant` DISABLE KEYS */;
INSERT INTO `mon_projet_etudiant` VALUES
(1,'etudiant1','Etudiant','1','b\'$2b$12$4TyDCUyI.QwPaJSwW/95r.FPya07w6J1hrXlfhP5YXMGfRT9uoOze\'','etudiant1@projet.xyz'),
(2,'etudiant2','Etudiant','2','b\'$2b$12$4TyDCUyI.QwPaJSwW/95r.FPya07w6J1hrXlfhP5YXMGfRT9uoOze\'','etudiant2@projet.xyz');
/*!40000 ALTER TABLE `mon_projet_etudiant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mon_projet_formulaire`
--

DROP TABLE IF EXISTS `mon_projet_formulaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mon_projet_formulaire` (
  `id_formulaire` int(11) NOT NULL AUTO_INCREMENT,
  `ouvert` tinyint(1) NOT NULL,
  `date_ouverture` datetime(6) NOT NULL,
  `date_fermeture` datetime(6) DEFAULT NULL,
  `nom_formulaire` varchar(50) NOT NULL,
  PRIMARY KEY (`id_formulaire`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mon_projet_formulaire`
--

LOCK TABLES `mon_projet_formulaire` WRITE;
/*!40000 ALTER TABLE `mon_projet_formulaire` DISABLE KEYS */;
INSERT INTO `mon_projet_formulaire` VALUES
(1,1,'2024-02-10 18:09:53.000000',NULL,'Premier formulaire'),
(2,1,'2024-02-11 12:38:56.000000',NULL,'Formulaire journée 2');
/*!40000 ALTER TABLE `mon_projet_formulaire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mon_projet_reponsesformulaire`
--

DROP TABLE IF EXISTS `mon_projet_reponsesformulaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mon_projet_reponsesformulaire` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `progression` int(11) NOT NULL,
  `difficulte` varchar(50) NOT NULL,
  `id_formulaire_id` int(11) NOT NULL,
  `numero_etudiant_id` int(11) NOT NULL,
  `maitrise` varchar(50) NOT NULL,
  `date_access` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mon_projet_reponsesf_id_formulaire_id_d1a3e494_fk_mon_proje` (`id_formulaire_id`),
  KEY `mon_projet_reponsesf_numero_etudiant_id_839daa5d_fk_mon_proje` (`numero_etudiant_id`),
  CONSTRAINT `mon_projet_reponsesf_id_formulaire_id_d1a3e494_fk_mon_proje` FOREIGN KEY (`id_formulaire_id`) REFERENCES `mon_projet_formulaire` (`id_formulaire`),
  CONSTRAINT `mon_projet_reponsesf_numero_etudiant_id_839daa5d_fk_mon_proje` FOREIGN KEY (`numero_etudiant_id`) REFERENCES `mon_projet_etudiant` (`numero_etudiant`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mon_projet_reponsesformulaire`
--

LOCK TABLES `mon_projet_reponsesformulaire` WRITE;
/*!40000 ALTER TABLE `mon_projet_reponsesformulaire` DISABLE KEYS */;
INSERT INTO `mon_projet_reponsesformulaire` VALUES
(1,100,'Un peu compliqué',1,1,'J\'ai compris',NULL),
(2,50,'OK',1,2,'J\'ai compris',NULL),
(6,0,'Vide',2,1,'Vide','2024-02-11 14:29:22.000000'),
(7,10,'Très compliqué',2,2,'C\'est flou','2024-02-11 16:27:39.000000');
/*!40000 ALTER TABLE `mon_projet_reponsesformulaire` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-11 17:51:13
