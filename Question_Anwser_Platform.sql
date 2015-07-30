-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Question_Anwser_Platform
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_account`
--

DROP TABLE IF EXISTS `tb_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_account` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT ' 账户用户名',
  `password` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '账户密码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='登录账户表（存储账户信息: 用户名和密码）';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_account`
--

LOCK TABLES `tb_account` WRITE;
/*!40000 ALTER TABLE `tb_account` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_answer`
--

DROP TABLE IF EXISTS `tb_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_answer` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `answer_username` varchar(50) DEFAULT NULL COMMENT '回答者的用户名',
  `answer_time` date DEFAULT NULL COMMENT '回答时间',
  `question_id` int(11) unsigned NOT NULL COMMENT '对应问题的ID',
  `is_accepted` tinyint(1) unsigned NOT NULL COMMENT '回答是否被采纳',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_answer`
--

LOCK TABLES `tb_answer` WRITE;
/*!40000 ALTER TABLE `tb_answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_ask`
--

DROP TABLE IF EXISTS `tb_ask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_ask` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `question_id` int(11) unsigned NOT NULL COMMENT '问题ID',
  `ask_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '追问内容 (文字, 语音或图片的一种)',
  `content_type` tinyint(1) unsigned NOT NULL COMMENT '追问内容类型 (0: 文字 1: 语音 2: 图片)',
  `ask_time` date DEFAULT NULL COMMENT '追问时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_ask`
--

LOCK TABLES `tb_ask` WRITE;
/*!40000 ALTER TABLE `tb_ask` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_ask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_level`
--

DROP TABLE IF EXISTS `tb_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_level` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '注册的用户名',
  `level_id` int(11) unsigned NOT NULL COMMENT '等级ID',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_level`
--

LOCK TABLES `tb_level` WRITE;
/*!40000 ALTER TABLE `tb_level` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_level_rule`
--

DROP TABLE IF EXISTS `tb_level_rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_level_rule` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `level` int(11) unsigned NOT NULL COMMENT '等级',
  `level_type` tinyint(1) unsigned NOT NULL COMMENT '称号类别 (0: 学生称号 1: 教师称号)',
  `level_desc` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '等级称号',
  `level_section` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '问题数量区间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_level_rule`
--

LOCK TABLES `tb_level_rule` WRITE;
/*!40000 ALTER TABLE `tb_level_rule` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_level_rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_question`
--

DROP TABLE IF EXISTS `tb_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_question` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `question_username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '提问者的用户名',
  `question_id` int(11) unsigned NOT NULL COMMENT '问题的ID',
  `question_title` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '问题标题',
  `quetion_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '问题内容(文字, 语音或图片的一种)',
  `question_score` int(11) unsigned NOT NULL COMMENT '问题悬赏积分',
  `question_category` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '问题分类(格式: 年级-科目, 如: 小学-英语)',
  `content_type` tinyint(1) unsigned NOT NULL COMMENT '内容类型 (0: 文字 1: 语音 2: 图片)',
  `question_time` date DEFAULT NULL COMMENT '提问时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_question`
--

LOCK TABLES `tb_question` WRITE;
/*!40000 ALTER TABLE `tb_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_score_rule`
--

DROP TABLE IF EXISTS `tb_score_rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_score_rule` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_operation_type` tinyint(4) unsigned NOT NULL COMMENT '用户操作类型 (0: 新用户登录 1: 提问 2: 回答 3: 被举报 4: 签到 5: 注册邀请码)',
  `user_operation_desc` varchar(300) DEFAULT NULL COMMENT '用户操作描述',
  `score_points` int(11) DEFAULT NULL COMMENT '积分处理',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_score_rule`
--

LOCK TABLES `tb_score_rule` WRITE;
/*!40000 ALTER TABLE `tb_score_rule` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_score_rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user`
--

DROP TABLE IF EXISTS `tb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `card_number` int(11) unsigned NOT NULL COMMENT '证件号码（必填）',
  `address` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '家庭住址',
  `grade` tinyint(2) unsigned NOT NULL COMMENT '年级 (必填)',
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '真实姓名（必填）',
  `birthday` date NOT NULL COMMENT '出生日期',
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '注册的用户名',
  `identifier` tinyint(1) unsigned NOT NULL COMMENT '身份标识(0: 学生 1: 教师)',
  `avatar_url` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '用户头像url',
  `phone_number` int(11) DEFAULT NULL COMMENT '手机号码',
  `sex` tinyint(1) unsigned NOT NULL COMMENT '性别 (0: 男 1: 女)',
  `card_type` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '证件类型 (0: 二代身份证 1: 其他)',
  `subject` varchar(11) DEFAULT NULL COMMENT '科目 (教师必填, 学生可选)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户数据表（存储用户的真实信息， 外键username与tb_account表关联）';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user`
--

LOCK TABLES `tb_user` WRITE;
/*!40000 ALTER TABLE `tb_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user_points`
--

DROP TABLE IF EXISTS `tb_user_points`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_user_points` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '注册的用户名',
  `points` int(11) unsigned NOT NULL COMMENT '积分',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user_points`
--

LOCK TABLES `tb_user_points` WRITE;
/*!40000 ALTER TABLE `tb_user_points` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_user_points` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-31  0:48:30
