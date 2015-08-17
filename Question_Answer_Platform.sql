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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='登录账户表（存储账户信息: 用户名和密码）';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_account`
--

LOCK TABLES `tb_account` WRITE;
/*!40000 ALTER TABLE `tb_account` DISABLE KEYS */;
INSERT INTO `tb_account` VALUES (1,'flyfish','345ca077818ab58966b92260d7769ab231c86fd5380a26196abc0846');
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
  `anwser_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '回答的内容 (文字, 语音或图片的一种)',
  `content_type` tinyint(1) unsigned NOT NULL COMMENT '回答内容的类型 (0: 文字 1: 语音 2: 图片)',
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
  `ask_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '追问内容 (文字, 语音或图片的一种)',
  `content_type` tinyint(1) unsigned NOT NULL COMMENT '追问内容类型 (0: 文字 1: 语音 2: 图片)',
  `ask_time` date DEFAULT NULL COMMENT '追问时间',
  `original_quetion_id` int(11) unsigned NOT NULL COMMENT '所属问题的ID',
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
INSERT INTO `tb_level_rule_template` VALUES (1,1,0,'学渣','[0, 100]'),(2,1,1,'菜鸟教师','[0, 100]'),(3,2,0,'学弟','[100, 200]'),(4,2,1,'初级教师','[100, 200]'),(5,3,0,'学长','[200, 300]'),(6,3,1,'中级教师','[200, 300]'),(7,4,0,'学霸','[300, 600]'),(8,4,1,'高级教师','[300, 600]'),(9,5,0,'学神','[600, -1]'),(10,5,1,'超级教师','[600, -1]');
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
  `content_type` tinyint(1) unsigned NOT NULL COMMENT '内容类型 (1: 文字 2: 语音 3: 图片)',
  `quetion_content` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '问题内容(文字, 语音或图片的一种)',
  `question_score` int(11) unsigned NOT NULL COMMENT '问题悬赏积分',
  `question_grade` tinyint(1) unsigned NOT NULL COMMENT '问题所属的年级',
  `question_subject` tinyint(4) unsigned NOT NULL COMMENT '问题所属的科目',
  `question_time` date DEFAULT NULL COMMENT '提问时间',
  `question_status` tinyint(1) unsigned NOT NULL COMMENT '问题当前的状态 (0: 未解决 1: 已解决)',
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='提问表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_question`
--

LOCK TABLES `tb_question` WRITE;
/*!40000 ALTER TABLE `tb_question` DISABLE KEYS */;
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
  `quesiton_id` int(11) unsigned NOT NULL COMMENT '问题ID',
  `collecter_username` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '收藏者的用户名 ',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='问题收藏表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_question_collection`
--

LOCK TABLES `tb_question_collection` WRITE;
/*!40000 ALTER TABLE `tb_question_collection` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户关注/粉丝表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_relation`
--

LOCK TABLES `tb_relation` WRITE;
/*!40000 ALTER TABLE `tb_relation` DISABLE KEYS */;
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
INSERT INTO `tb_score_rule_template` VALUES (1,1,'新用户登陆',20),(2,2,'学生提问奖励',5),(3,3,'⽼师回答奖励被采纳',5),(4,4,'老师回答未被采纳',1),(5,5,'问题被举报,管理员核实后删除',-20),(6,6,'每⽇签到',10),(7,7,'邀请新⽤户(邀请时产生验证码,⽤户根据验证码)',10);
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
  `sign_time` date DEFAULT NULL COMMENT '签到日期 (每天仅允许签到一次)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户签到表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_sign`
--

LOCK TABLES `tb_sign` WRITE;
/*!40000 ALTER TABLE `tb_sign` DISABLE KEYS */;
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
  `card_number` char(11) DEFAULT '' COMMENT '证件号码',
  `address` varchar(50) DEFAULT '' COMMENT '家庭住址',
  `grade` tinyint(1) NOT NULL COMMENT '年级 (必填)[0: 小学 1: 初中 2: 高中]',
  `name` varchar(30) DEFAULT '' COMMENT '真实姓名',
  `birthday` date DEFAULT NULL COMMENT '出生日期',
  `username` varchar(50) NOT NULL DEFAULT '' COMMENT '注册的用户名 (邮箱地址)',
  `identifier` tinyint(1) NOT NULL COMMENT '身份标识(0: 学生 1: 教师)',
  `avatar_url` varchar(50) DEFAULT '' COMMENT '用户头像url',
  `phone_number` char(11) DEFAULT '' COMMENT '手机号码',
  `sex` tinyint(1) DEFAULT NULL COMMENT '性别 (0: 男 1: 女)',
  `subject` tinyint(4) DEFAULT NULL COMMENT '科目 (教师必填, 学生可选)',
  `serial_number` char(8) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '工作证号 (该项仅针对教师，长度8位)',
  `invitation_code` char(11) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '邀请码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户数据表（存储用户的真实信息， 外键username与tb_account表关联）';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user`
--

LOCK TABLES `tb_user` WRITE;
/*!40000 ALTER TABLE `tb_user` DISABLE KEYS */;
INSERT INTO `tb_user` VALUES (1,'','',1,'',NULL,'flyfish',0,'','13581711922',NULL,NULL,NULL,NULL);
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
  `point_type` tinyint(4) unsigned NOT NULL COMMENT '积分类型',
  `point_value` int(11) unsigned NOT NULL COMMENT '积分',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户积分表';
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

-- Dump completed on 2015-08-17 22:33:41
