-- MySQL dump 10.13  Distrib 5.6.26, for osx10.10 (x86_64)
--
-- Host: 192.168.1.106    Database: Question_Answer_Platform
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
-- Table structure for table `tb_about_us_template`
--

DROP TABLE IF EXISTS `tb_about_us_template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_about_us_template` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_about_us_template`
--

LOCK TABLES `tb_about_us_template` WRITE;
/*!40000 ALTER TABLE `tb_about_us_template` DISABLE KEYS */;
INSERT INTO `tb_about_us_template` VALUES (1,'哈尔滨市共有教师10万人，中小学学生100万人，目前缺乏有效的沟通桥梁。哈尔滨教育互动平台致力于打造人人乐用的学习服务平台，通过高效、智能、精准地匹配师生资源，为老师及学生提供多种增值服务和学习工具，创建一个专业、简单、智能、安全的高品质学习服务的第三方平台，让学习变得更加容易、平等和高效，让所有有知识、技能、才华的人都能够在这个平台上成为老师，让所有需要知识、技能、才华的人都能够在这个平台上找到他们学习的榜样。在让跟谁学成为一种生活方式的同时，跟谁学也在全力打造更富活力、更加健康的教育生态圈。');
/*!40000 ALTER TABLE `tb_about_us_template` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_account`
--

DROP TABLE IF EXISTS `tb_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_account` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT ' 账户用户名 (强制为邮箱地址)',
  `password` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '账户密码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COMMENT='登录账户表（存储账户信息: 用户名和密码）';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_account`
--

LOCK TABLES `tb_account` WRITE;
/*!40000 ALTER TABLE `tb_account` DISABLE KEYS */;
INSERT INTO `tb_account` VALUES (1,'flyfish@ifeiyu.net','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846'),(2,'daijun74@163.com','7e6a4309ddf6e8866679f61ace4f621b0e3455ebac2e831a60f13cd1'),(3,'1553556149@qq.com','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846'),(4,'heavenfox@126.com','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846'),(5,'nobody@ifeiyu.net','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846'),(6,'flyfish13@ifeiyu.net','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846'),(7,'flyfish120@ifeiyu.net','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846'),(8,'caiyuanpei@vip.qq.com','e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'),(9,'caiyuanpei1@vip.qq.com','e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'),(10,'caiyuanpei2@vip.qq.com','e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'),(11,'caiyuanpei3@vip.qq.com','e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'),(12,'caiyuanpei4@vip.qq.com','e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'),(13,'da@da.com','f8cdb04495ded47615258f9dc6a3f4707fd2405434fefc3cbf4ef4e6'),(14,'qflyfish@ifeiyu.net','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846'),(15,'flyfish15@ifeiyu.net','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846');
/*!40000 ALTER TABLE `tb_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_ad`
--

DROP TABLE IF EXISTS `tb_ad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_ad` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ad_title` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '信息标题',
  `ad_author` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '发表者的用户名',
  `ad_time` date DEFAULT NULL COMMENT '发布时间',
  `ad_content` text CHARACTER SET utf8 COLLATE utf8_bin COMMENT '正文',
  `ad_screenshot` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '图片url',
  `ad_option_content` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '可选内容 (视频信息)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告/公告信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_ad`
--

LOCK TABLES `tb_ad` WRITE;
/*!40000 ALTER TABLE `tb_ad` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_ad` ENABLE KEYS */;
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
  `answer_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '回答的内容 (文字)',
  `answer_pic_url` varchar(150) DEFAULT NULL COMMENT '回答相关的图片url',
  `answer_sound_url` varchar(150) DEFAULT NULL COMMENT '回答相关的录音url',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='回答表';
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
  `ask_question_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '追问问题的ID (主键)',
  `ask_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '追问内容 (文字)',
  `ask_pic_url` varchar(150) DEFAULT NULL COMMENT '追问相关的图片url',
  `ask_sound_url` varchar(150) DEFAULT NULL COMMENT '追问相关的录音url',
  `ask_time` date DEFAULT NULL COMMENT '追问时间',
  `original_question_id` int(11) unsigned NOT NULL COMMENT '所属问题的ID',
  `be_asked_username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '' COMMENT '被追问的用户',
  `ask_order` int(11) unsigned NOT NULL COMMENT '追问次序（方便检索所有相关的追问和追答）',
  PRIMARY KEY (`ask_question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='追问表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_ask`
--

LOCK TABLES `tb_ask` WRITE;
/*!40000 ALTER TABLE `tb_ask` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_ask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_feedback`
--

DROP TABLE IF EXISTS `tb_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_feedback` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL COMMENT '用户名',
  `content` text COMMENT '反馈内容',
  `feed_time` datetime DEFAULT NULL COMMENT '提交反馈的时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_feedback`
--

LOCK TABLES `tb_feedback` WRITE;
/*!40000 ALTER TABLE `tb_feedback` DISABLE KEYS */;
INSERT INTO `tb_feedback` VALUES (1,'flyfish@ifeiyu.net','hello','2015-08-19 00:20:24'),(2,'flyfish@ifeiyu.net','hello','2015-08-19 15:08:34'),(3,'daijun74@163.com','Test','2015-08-19 15:10:15'),(4,'flyfish@ifeiyu.net','wawo','2015-08-20 11:15:03'),(5,'flyfish@ifeiyu.net','wawo','2015-08-20 11:20:48'),(6,'flyfish@ifeiyu.net','wawo','2015-08-20 11:26:00'),(7,'flyfish@ifeiyu.net','wawo','2015-08-20 11:32:37'),(8,'flyfish@ifeiyu.net','wawo','2015-08-20 11:33:35'),(9,'flyfish@ifeiyu.net','wawo','2015-08-20 11:44:56'),(10,'flyfish@ifeiyu.net','wawo','2015-08-21 22:46:57'),(11,'flyfish@ifeiyu.net','wawo','2015-08-21 22:47:12'),(12,'flyfish@ifeiyu.net','wawo','2015-08-21 22:47:58'),(13,'flyfish@ifeiyu.net','wawo','2015-08-21 22:48:42'),(14,'flyfish@ifeiyu.net','wawo','2015-08-21 23:06:08'),(15,'flyfish@ifeiyu.net','wawo','2015-08-21 23:06:49'),(16,'flyfish@ifeiyu.net','wawo','2015-08-21 23:17:56'),(17,'flyfish@ifeiyu.net','wawo','2015-08-21 23:18:23'),(18,'flyfish@ifeiyu.net','wawo','2015-08-21 23:18:30'),(19,'flyfish@ifeiyu.net','wawo','2015-08-21 23:26:27'),(20,'flyfish@ifeiyu.net','wawo','2015-08-21 23:48:58'),(21,'flyfish@ifeiyu.net','wawo','2015-08-21 23:49:36'),(22,'flyfish@ifeiyu.net','wawo','2015-08-21 23:56:28'),(23,'flyfish@ifeiyu.net','wawo','2015-08-22 00:25:03'),(24,'flyfish@ifeiyu.net','wawo','2015-08-22 00:27:02'),(25,'flyfish@ifeiyu.net','wawo','2015-08-22 00:29:23'),(26,'flyfish@ifeiyu.net','wawo','2015-08-22 00:54:16'),(27,'flyfish@ifeiyu.net','wawo','2015-08-22 00:55:04'),(28,'flyfish@ifeiyu.net','wawo','2015-08-22 00:55:40'),(29,'flyfish@ifeiyu.net','wawo','2015-08-22 01:03:22'),(30,'flyfish@ifeiyu.net','wawo','2015-08-22 19:43:55'),(31,'flyfish@ifeiyu.net','wawo','2015-08-22 19:44:24'),(32,'flyfish@ifeiyu.net','wawo','2015-08-22 19:44:44'),(33,'flyfish@ifeiyu.net','wawo','2015-08-22 21:35:40'),(34,'flyfish@ifeiyu.net','wawo','2015-08-22 22:50:33'),(35,'da@da.com','nihao xiongdi men','2015-08-23 07:11:52'),(36,'flyfish@ifeiyu.net','wawo','2015-08-23 11:22:57'),(37,'flyfish@ifeiyu.net','wawo','2015-08-23 12:28:19'),(38,'flyfish@ifeiyu.net','wawo','2015-08-23 12:31:27'),(39,'flyfish@ifeiyu.net','wawo','2015-08-24 23:14:23'),(40,'flyfish@ifeiyu.net','wawo','2015-08-24 23:14:57'),(41,'flyfish@ifeiyu.net','wawo','2015-08-24 23:16:49'),(42,'flyfish@ifeiyu.net','wawo','2015-08-24 23:17:08'),(43,'flyfish@ifeiyu.net','wawo','2015-08-24 23:17:33'),(44,'flyfish@ifeiyu.net','wawo','2015-08-24 23:35:20'),(45,'flyfish@ifeiyu.net','wawo','2015-08-25 22:16:30'),(46,'flyfish@ifeiyu.net','wawo','2015-08-25 22:17:27'),(47,'flyfish@ifeiyu.net','wawo','2015-08-25 22:19:49'),(48,'flyfish@ifeiyu.net','wawo','2015-08-25 23:26:10'),(49,'flyfish@ifeiyu.net','wawo','2015-08-25 23:29:35'),(50,'flyfish@ifeiyu.net','wawo','2015-08-25 23:29:54');
/*!40000 ALTER TABLE `tb_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_grade_template`
--

DROP TABLE IF EXISTS `tb_grade_template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_grade_template` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `grade_value` tinyint(2) unsigned NOT NULL COMMENT '年级数值',
  `grade` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '年级描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='年级模板表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_grade_template`
--

LOCK TABLES `tb_grade_template` WRITE;
/*!40000 ALTER TABLE `tb_grade_template` DISABLE KEYS */;
INSERT INTO `tb_grade_template` VALUES (1,1,'小学'),(2,2,'初中'),(3,3,'高中');
/*!40000 ALTER TABLE `tb_grade_template` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户等级';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_level`
--

LOCK TABLES `tb_level` WRITE;
/*!40000 ALTER TABLE `tb_level` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_level_rule_template`
--

DROP TABLE IF EXISTS `tb_level_rule_template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_level_rule_template` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `level` int(11) unsigned NOT NULL COMMENT '等级',
  `level_type` tinyint(1) unsigned NOT NULL COMMENT '称号类别 (0: 学生称号 1: 教师称号)',
  `level_desc` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '等级称号',
  `level_section` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '问题数量区间, [m, n]表示m<=x<n',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COMMENT='等级评价标准表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_level_rule_template`
--

LOCK TABLES `tb_level_rule_template` WRITE;
/*!40000 ALTER TABLE `tb_level_rule_template` DISABLE KEYS */;
INSERT INTO `tb_level_rule_template` VALUES (1,1,0,'学渣','[0, 100]'),(2,1,1,'菜鸟教师','[0, 100]'),(3,2,0,'学弟','[100, 200]'),(4,2,1,'初级教师','[100, 200]'),(5,3,0,'学长','[200, 300]'),(6,3,1,'中级教师','[200, 300]'),(7,4,0,'学霸','[300, 600]'),(8,4,1,'高级教师','[300, 600]'),(9,5,0,'学神','[600, 1000000]'),(10,5,1,'超级教师','[600, 1000000]');
/*!40000 ALTER TABLE `tb_level_rule_template` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_question`
--

DROP TABLE IF EXISTS `tb_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_question` (
  `question_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '问题ID (主键)',
  `question_username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '提问者的用户名',
  `question_head` int(11) unsigned NOT NULL COMMENT '系统随机注入的头部信息ID (与tb_question_header_template表关联)',
  `question_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '问题内容(文字)',
  `question_pic_url` varchar(150) DEFAULT NULL COMMENT '问题相关的图片url',
  `question_sound_url` varchar(150) DEFAULT NULL COMMENT '问题相关的录音url',
  `question_score` int(11) unsigned NOT NULL COMMENT '问题悬赏积分',
  `question_grade` tinyint(1) unsigned NOT NULL COMMENT '问题所属的年级',
  `question_subject` tinyint(4) unsigned NOT NULL COMMENT '问题所属的科目',
  `question_time` datetime DEFAULT NULL COMMENT '提问时间',
  `question_status` tinyint(1) unsigned NOT NULL COMMENT '问题当前的状态 (0: 未解决 1: 已解决)',
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8 COMMENT='提问表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_question`
--

LOCK TABLES `tb_question` WRITE;
/*!40000 ALTER TABLE `tb_question` DISABLE KEYS */;
INSERT INTO `tb_question` VALUES (2,'flyfish',0,'zzzz','','',10,2,4,'2015-08-20 00:00:00',0),(3,'flyfish@ifeiyu.net',0,'世界这么大, 你不想取看看吗？','','',20,1,4,'2015-08-20 10:23:12',0),(4,'flyfish@ifeiyu.net',0,'世界这么大, 你不想取看看吗？','','',20,1,4,'2015-08-20 10:27:08',0),(5,'flyfish@ifeiyu.net',0,'世界这么大, 你不想取看看吗？','','',20,1,4,'2015-08-20 10:30:47',0),(6,'flyfish@ifeiyu.net',0,'世界这么大, 你不想取看看吗？','','',20,1,4,'2015-08-20 10:32:34',0),(7,'flyfish@ifeiyu.net',0,'世界这么大, 你不想取看看吗？','','',20,1,4,'2015-08-20 10:33:02',0),(8,'flyfish@ifeiyu.net',0,'世界这么大, 你不想取看看吗？','','',20,1,4,'2015-08-20 10:35:10',0),(9,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-20 10:35:37',0),(10,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-20 10:38:15',0),(11,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-20 10:44:32',0),(12,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-20 10:46:40',0),(13,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-20 10:47:45',0),(14,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-20 10:49:14',0),(15,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-20 10:57:20',0),(16,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-20 10:58:38',0),(17,'caiyuanpei@vip.qq.com',0,'hello world','','',10,2,7,'2015-08-23 11:09:45',0),(18,'caiyuanpei@vip.qq.com',0,'hello world','','',10,2,7,'2015-08-23 11:12:36',0),(19,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-23 11:26:31',0),(20,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-23 12:28:11',0),(21,'caiyuanpei@vip.qq.com',0,'hello world','','',10,3,7,'2015-08-23 15:28:38',0),(22,'flyfish@ifeiyu.net',0,'','','',0,1,1,'2015-08-24 00:21:54',0),(23,'flyfish@ifeiyu.net',0,'','','',0,1,1,'2015-08-24 00:22:09',0),(24,'flyfish@ifeiyu.net',0,'oil明明哦','','',0,1,1,'2015-08-24 00:22:57',0),(25,'flyfish@ifeiyu.net',0,'','','',0,1,1,'2015-08-24 01:54:43',0),(26,'flyfish@ifeiyu.net',0,'哦哦哦','','',5,1,1,'2015-08-24 06:25:53',0),(27,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 22:42:24',0),(28,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 22:43:50',0),(29,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 22:46:47',0),(30,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 22:48:25',0),(31,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:14:02',0),(32,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:36:13',0),(33,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:39:57',0),(34,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:41:21',0),(35,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:41:40',0),(36,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:43:30',0),(37,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:44:13',0),(38,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:46:57',0),(39,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:47:37',0),(40,'flyfish@ifeiyu.net',0,'hello','','',20,1,4,'2015-08-24 23:47:59',0),(41,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-25 22:20:10',0),(42,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-25 22:21:05',0),(43,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-25 22:24:21',0),(44,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-25 22:27:35',0),(45,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-25 23:39:31',0),(46,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-26 00:21:52',0),(47,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-26 00:27:11',0),(48,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-26 00:28:05',0),(49,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-26 01:12:53',0),(50,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-26 01:13:17',0),(51,'flyfish@ifeiyu.net',0,'hello',NULL,NULL,20,1,4,'2015-08-26 01:14:58',0);
/*!40000 ALTER TABLE `tb_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_question_collection`
--

DROP TABLE IF EXISTS `tb_question_collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_question_collection` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `question_id` int(11) unsigned NOT NULL COMMENT '收藏问题的ID',
  `collecter_username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '收藏者的用户名 ',
  `collect_time` datetime DEFAULT NULL COMMENT '收藏时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='问题收藏表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_question_collection`
--

LOCK TABLES `tb_question_collection` WRITE;
/*!40000 ALTER TABLE `tb_question_collection` DISABLE KEYS */;
INSERT INTO `tb_question_collection` VALUES (1,3,'flyfish@ifeiyu.net',NULL),(2,1001,'flyfish@ifeiyu.net',NULL);
/*!40000 ALTER TABLE `tb_question_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_question_header_template`
--

DROP TABLE IF EXISTS `tb_question_header_template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_question_header_template` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `header_id` int(11) unsigned NOT NULL COMMENT '信息头部ID',
  `header_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '信息头部内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_question_header_template`
--

LOCK TABLES `tb_question_header_template` WRITE;
/*!40000 ALTER TABLE `tb_question_header_template` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_question_header_template` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_relation`
--

DROP TABLE IF EXISTS `tb_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_relation` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '用户名A',
  `other_username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '用户名B',
  `relation_type` tinyint(1) unsigned NOT NULL COMMENT '关系类型 (0: 关注 1: 被关注)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='用户关注/粉丝表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_relation`
--

LOCK TABLES `tb_relation` WRITE;
/*!40000 ALTER TABLE `tb_relation` DISABLE KEYS */;
INSERT INTO `tb_relation` VALUES (1,'flyfish@ifeiyu.net','flyfish13@ifeiyu.net',0),(2,'flyfish13@ifeiyu.net','flyfish@ifeiyu.net',1);
/*!40000 ALTER TABLE `tb_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_report`
--

DROP TABLE IF EXISTS `tb_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_report` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `question_id` int(11) unsigned NOT NULL COMMENT '被举报的问题ID',
  `reporter_username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '' COMMENT '举报者的用户名',
  `report_status` tinyint(1) unsigned NOT NULL COMMENT '举报当前的状态 (0: 待处理 1: 废弃（虚假举报） 2: 已处理 (情况属实))',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='问题举报表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_report`
--

LOCK TABLES `tb_report` WRITE;
/*!40000 ALTER TABLE `tb_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_reset`
--

DROP TABLE IF EXISTS `tb_reset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_reset` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '用户名',
  `reset_time` date DEFAULT NULL COMMENT '重置时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户找回密码记录表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_reset`
--

LOCK TABLES `tb_reset` WRITE;
/*!40000 ALTER TABLE `tb_reset` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_reset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_score_rule_template`
--

DROP TABLE IF EXISTS `tb_score_rule_template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_score_rule_template` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_operation_type` tinyint(4) unsigned NOT NULL COMMENT '用户操作类型 (0: 新用户登录 1: 提问 2: 回答 3: 被举报 4: 签到 5: 注册邀请码)',
  `user_operation_desc` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '用户操作描述',
  `score_points` int(11) DEFAULT NULL COMMENT '积分处理',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COMMENT='积分评估标准表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_score_rule_template`
--

LOCK TABLES `tb_score_rule_template` WRITE;
/*!40000 ALTER TABLE `tb_score_rule_template` DISABLE KEYS */;
INSERT INTO `tb_score_rule_template` VALUES (1,1,'新用户登陆',20),(2,2,'提问',5),(3,3,'回答被采纳',5),(4,4,'回答未被采纳',1),(5,5,'问题被举报,管理员核实后删除',-20),(6,6,'签到',10),(7,7,'邀请⽤户',10);
/*!40000 ALTER TABLE `tb_score_rule_template` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_share_template`
--

DROP TABLE IF EXISTS `tb_share_template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_share_template` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `share_channel_type` tinyint(2) unsigned NOT NULL COMMENT '分享渠道的类型',
  `share_channel` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '分享渠道',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告/公告分享模板表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_share_template`
--

LOCK TABLES `tb_share_template` WRITE;
/*!40000 ALTER TABLE `tb_share_template` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_share_template` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_sign`
--

DROP TABLE IF EXISTS `tb_sign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_sign` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '签到者的用户名',
  `sign_time` datetime DEFAULT NULL COMMENT '签到日期 (每天仅允许签到一次)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='用户签到表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_sign`
--

LOCK TABLES `tb_sign` WRITE;
/*!40000 ALTER TABLE `tb_sign` DISABLE KEYS */;
INSERT INTO `tb_sign` VALUES (1,'flyfish@ifeiyu.net','2015-08-15 22:46:57'),(2,'flyfish@ifeiyu.net','2015-08-16 23:06:08'),(3,'flyfish@ifeiyu.net','2015-08-17 23:06:49'),(4,'flyfish@ifeiyu.net','2015-08-18 23:17:56'),(5,'flyfish@ifeiyu.net','2015-08-19 23:18:23'),(6,'flyfish@ifeiyu.net','2015-08-20 23:18:30'),(7,'flyfish@ifeiyu.net','2015-08-21 23:48:58'),(8,'flyfish@ifeiyu.net','2015-08-22 00:25:03'),(9,'flyfish@ifeiyu.net','2015-08-23 11:22:57'),(10,'flyfish@ifeiyu.net','2015-08-24 00:19:08'),(11,'flyfish@ifeiyu.net','2015-08-25 22:16:30');
/*!40000 ALTER TABLE `tb_sign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_subject_template`
--

DROP TABLE IF EXISTS `tb_subject_template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_subject_template` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `subject_value` tinyint(4) unsigned NOT NULL COMMENT '科目的取值',
  `subject` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '科目描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COMMENT='科目模板表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_subject_template`
--

LOCK TABLES `tb_subject_template` WRITE;
/*!40000 ALTER TABLE `tb_subject_template` DISABLE KEYS */;
INSERT INTO `tb_subject_template` VALUES (1,1,'数学'),(2,2,'语文'),(3,3,'英语'),(4,4,'生物'),(5,5,'政治'),(6,6,'历史'),(7,7,'地理'),(8,8,'物理'),(9,9,'化学');
/*!40000 ALTER TABLE `tb_subject_template` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user`
--

DROP TABLE IF EXISTS `tb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `card_number` char(12) DEFAULT NULL COMMENT '证件号码',
  `address` varchar(50) DEFAULT '' COMMENT '家庭住址',
  `grade` tinyint(1) NOT NULL COMMENT '年级 (必填)[0: 小学 1: 初中 2: 高中]',
  `name` varchar(30) DEFAULT '' COMMENT '真实姓名',
  `birthday` date DEFAULT NULL COMMENT '出生日期',
  `username` varchar(50) NOT NULL DEFAULT '' COMMENT '注册的用户名 (邮箱地址)',
  `identifier` tinyint(1) NOT NULL COMMENT '身份标识(0: 学生 1: 教师)',
  `avatar_url` varchar(100) DEFAULT NULL COMMENT '用户头像url',
  `phone_number` char(12) DEFAULT NULL COMMENT '手机号码',
  `sex` tinyint(1) DEFAULT NULL COMMENT '性别 (0: 男 1: 女)',
  `subject` tinyint(4) DEFAULT NULL COMMENT '科目 (教师必填, 学生可选)',
  `serial_number` char(9) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '工作证号 (该项仅针对教师，长度8位)',
  `invitation_code` char(11) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '邀请码',
  `nickname` varchar(50) DEFAULT NULL COMMENT '昵称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COMMENT='用户数据表（存储用户的真实信息， 外键username与tb_account表关联）';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user`
--

LOCK TABLES `tb_user` WRITE;
/*!40000 ALTER TABLE `tb_user` DISABLE KEYS */;
INSERT INTO `tb_user` VALUES (1,'','',1,'',NULL,'flyfish@ifeiyu.net',0,'','17681711922',NULL,NULL,NULL,NULL,'cls1991'),(2,'','',1,'',NULL,'daijun74@163.com',0,'','',NULL,NULL,NULL,NULL,NULL),(3,'','',2,'',NULL,'1553556149@qq.com',0,'','',NULL,NULL,NULL,NULL,NULL),(4,'','',1,'',NULL,'heavenfox@126.com',1,'','',NULL,4,'12345678',NULL,NULL),(5,'','',1,'',NULL,'nobody@ifeiyu.net',1,'','',NULL,4,'12345678',NULL,NULL),(6,'11111111111','where',1,'张三','2015-09-11','flyfish13@ifeiyu.net',1,'/data/avatars/flyfish.png','00000000000',0,4,'12345678',NULL,NULL),(7,NULL,'',1,'',NULL,'flyfish120@ifeiyu.net',1,NULL,NULL,NULL,4,'12345678','',NULL),(8,NULL,'',3,'',NULL,'caiyuanpei@vip.qq.com',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,NULL,'',3,'',NULL,'caiyuanpei1@vip.qq.com',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(10,NULL,'',3,'',NULL,'caiyuanpei2@vip.qq.com',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11,NULL,'',3,'',NULL,'caiyuanpei3@vip.qq.com',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(12,NULL,'',3,'',NULL,'caiyuanpei4@vip.qq.com',1,NULL,NULL,NULL,2,'12345678',NULL,NULL),(13,NULL,'',1,'',NULL,'da@da.com',1,NULL,NULL,NULL,1,'123456',NULL,NULL),(14,NULL,'',1,'',NULL,'qflyfish@ifeiyu.net',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(15,'111111111111','where',1,'张三','2015-09-11','flyfish15@ifeiyu.net',1,'/qap_server/uploads/user/avatar/default.png','000000000000',0,4,'12345678',NULL,NULL);
/*!40000 ALTER TABLE `tb_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user_log`
--

DROP TABLE IF EXISTS `tb_user_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_user_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '注册的用户名',
  `login_time` datetime DEFAULT NULL COMMENT '登录时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `my_key` (`username`,`login_time`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='用户等级';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user_log`
--

LOCK TABLES `tb_user_log` WRITE;
/*!40000 ALTER TABLE `tb_user_log` DISABLE KEYS */;
INSERT INTO `tb_user_log` VALUES (1,'flyfish@ifeiyu.net','2015-08-25 22:16:30'),(2,'flyfish@ifeiyu.net','2015-08-25 22:17:27'),(3,'flyfish@ifeiyu.net','2015-08-25 22:19:48'),(4,'flyfish@ifeiyu.net','2015-08-25 23:29:54');
/*!40000 ALTER TABLE `tb_user_log` ENABLE KEYS */;
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
  `point_type` tinyint(4) unsigned NOT NULL COMMENT '积分类型',
  `point_value` int(11) unsigned NOT NULL COMMENT '积分',
  PRIMARY KEY (`id`),
  UNIQUE KEY `my_key` (`username`,`point_type`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COMMENT='用户积分表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user_points`
--

LOCK TABLES `tb_user_points` WRITE;
/*!40000 ALTER TABLE `tb_user_points` DISABLE KEYS */;
INSERT INTO `tb_user_points` VALUES (1,'flyfish@ifeiyu.net',6,90),(10,'flyfish@ifeiyu.net',1,20),(12,'flyfish@ifeiyu.net',2,55);
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

-- Dump completed on 2015-08-26  1:19:43
