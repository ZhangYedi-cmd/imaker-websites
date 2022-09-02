/*
 Navicat Premium Data Transfer

 Source Server         : 49.232.14.242
 Source Server Type    : MySQL
 Source Server Version : 50650
 Source Host           : localhost:3306
 Source Schema         : imaker

 Target Server Type    : MySQL
 Target Server Version : 50650
 File Encoding         : 65001

 Date: 12/10/2021 10:59:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('561447ff1e90');

-- ----------------------------
-- Table structure for association
-- ----------------------------
DROP TABLE IF EXISTS `association`;
CREATE TABLE `association`  (
  `student_id` int(11) NULL DEFAULT NULL,
  `tutor_id` int(11) NULL DEFAULT NULL,
  INDEX `student_id`(`student_id`) USING BTREE,
  INDEX `tutor_id`(`tutor_id`) USING BTREE,
  CONSTRAINT `association_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`uid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `association_ibfk_2` FOREIGN KEY (`tutor_id`) REFERENCES `tutor` (`uid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of association
-- ----------------------------
INSERT INTO `association` VALUES (23, 5);
INSERT INTO `association` VALUES (23, 10);
INSERT INTO `association` VALUES (24, 5);
INSERT INTO `association` VALUES (24, 10);
INSERT INTO `association` VALUES (30, 21);
INSERT INTO `association` VALUES (30, 22);
INSERT INTO `association` VALUES (30, 23);
INSERT INTO `association` VALUES (31, 26);
INSERT INTO `association` VALUES (32, 21);
INSERT INTO `association` VALUES (32, 22);
INSERT INTO `association` VALUES (32, 23);
INSERT INTO `association` VALUES (33, 20);
INSERT INTO `association` VALUES (33, 25);
INSERT INTO `association` VALUES (34, 19);
INSERT INTO `association` VALUES (35, 21);
INSERT INTO `association` VALUES (35, 22);
INSERT INTO `association` VALUES (35, 23);
INSERT INTO `association` VALUES (37, 20);
INSERT INTO `association` VALUES (37, 25);
INSERT INTO `association` VALUES (38, 20);
INSERT INTO `association` VALUES (38, 25);
INSERT INTO `association` VALUES (39, 21);
INSERT INTO `association` VALUES (39, 22);
INSERT INTO `association` VALUES (39, 23);
INSERT INTO `association` VALUES (40, 20);
INSERT INTO `association` VALUES (40, 25);
INSERT INTO `association` VALUES (41, 20);
INSERT INTO `association` VALUES (41, 25);
INSERT INTO `association` VALUES (42, 19);
INSERT INTO `association` VALUES (42, 29);
INSERT INTO `association` VALUES (43, 20);
INSERT INTO `association` VALUES (43, 25);
INSERT INTO `association` VALUES (44, 26);
INSERT INTO `association` VALUES (44, 27);
INSERT INTO `association` VALUES (44, 28);
INSERT INTO `association` VALUES (45, 21);
INSERT INTO `association` VALUES (45, 22);
INSERT INTO `association` VALUES (45, 23);
INSERT INTO `association` VALUES (46, 26);
INSERT INTO `association` VALUES (46, 27);
INSERT INTO `association` VALUES (46, 28);
INSERT INTO `association` VALUES (47, 21);
INSERT INTO `association` VALUES (47, 22);
INSERT INTO `association` VALUES (47, 23);
INSERT INTO `association` VALUES (48, 21);
INSERT INTO `association` VALUES (48, 22);
INSERT INTO `association` VALUES (48, 23);
INSERT INTO `association` VALUES (49, 19);
INSERT INTO `association` VALUES (49, 29);
INSERT INTO `association` VALUES (50, 20);
INSERT INTO `association` VALUES (50, 25);
INSERT INTO `association` VALUES (51, 21);
INSERT INTO `association` VALUES (51, 22);
INSERT INTO `association` VALUES (51, 23);
INSERT INTO `association` VALUES (52, 30);
INSERT INTO `association` VALUES (53, 30);
INSERT INTO `association` VALUES (54, 20);
INSERT INTO `association` VALUES (54, 25);
INSERT INTO `association` VALUES (55, 30);

-- ----------------------------
-- Table structure for group
-- ----------------------------
DROP TABLE IF EXISTS `group`;
CREATE TABLE `group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of group
-- ----------------------------
INSERT INTO `group` VALUES (1, '前端');
INSERT INTO `group` VALUES (4, 'Rust');
INSERT INTO `group` VALUES (5, 'C语言');
INSERT INTO `group` VALUES (6, '设计');
INSERT INTO `group` VALUES (9, 'Python');
INSERT INTO `group` VALUES (10, '嵌入式');
INSERT INTO `group` VALUES (11, 'Java');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `uniLearn` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `interview_time` date NULL DEFAULT NULL,
  `group_id` int(11) NULL DEFAULT NULL,
  `campus` enum('河西校区','泰达校区') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '泰达校区',
  `tel` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `introduce` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `major` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `academy` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `annotation` varchar(10000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grade` int(11) NULL DEFAULT NULL,
  `status` enum('第一轮面试','第二轮面试','第三轮面试','通过','不通过','未审核') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email_status` enum('已发送','未发送') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '未发送',
  `rate` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`uid`) USING BTREE,
  INDEX `group_id`(`group_id`) USING BTREE,
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 56 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (2, '张业頔', '20011204', '178320369@qq.com', '2021-09-25', 1, '河西校区', '12312312', '123123123123', '机械', '机械', '123123123', 2020, '不通过', '已发送', 5);
INSERT INTO `student` VALUES (17, 'sd', 'sadas', 'asdas', '2021-09-07', NULL, '河西校区', 'asd', 'sadas', 'sadas', 'asdas', NULL, 20, NULL, '未发送', 0);
INSERT INTO `student` VALUES (23, 'zyzdadsdas1111', '1231231231', '178320369@qq.com', NULL, 1, '河西校区', '123123', '12312312312312', '12313231', '1231231231', NULL, 2012, '第一轮面试', '已发送', 0);
INSERT INTO `student` VALUES (24, 'zyzdadsdas11111', '1231231231', '178320369@qq.com', NULL, 1, '河西校区', '123123', '12312312312312', '12313231', '1231231231', NULL, 2012, NULL, '未发送', 0);
INSERT INTO `student` VALUES (30, '颜行健', '21204105', '2634807452@qq.com', NULL, 5, '泰达校区', '13632410649', '18岁，是学生，未婚，兴趣爱好十分广泛，会点ps，pr，blender，metasequoia在学原画，c语言，是垃圾', '中澳财管', '经管', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (31, '方贵庭', '21061111', '1454495636@qq.com', NULL, 6, '泰达校区', '18922093972', '我很开心来到创新实验室的招新群，我会努力通过面试，争取加入的！', '包装工程', '轻工科学与工程学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (32, '沈孟情', '21121420', '2598729414@qq.com', NULL, 5, '泰达校区', '18355055441', '想要成为很厉害的人，想要会很多东西！就是一只菜鸟，没事还有时间成长，今年不行明年嘻嘻，还有还有，5G冲浪选手...国家二级抬杠运动员，独自自强，落落大方！嘻嘻', '英语', '外国语', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (33, '孙晨皓', '20010815', '2402983805@qq.com', NULL, 9, '泰达校区', '13783008351', '我叫孙晨皓，20级人工智能学院大数据专业，从机械学院转专业过来的，想参加实验室提升自己的能力', '大数据', '人工智能学院', NULL, 2020, NULL, '未发送', 0);
INSERT INTO `student` VALUES (34, '韦莫杰鸣', '21054111', '1327521531@qq.com', NULL, 1, '泰达校区', '13397782166', '曾经学过一些东西，做过网站前端', '环境科学与工程', '海洋与环境学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (35, '辛帅兵', '20610117', '3174259866@qq.com', NULL, 5, '泰达校区', '19553460873', '本人大二学生，c语言和厉害的人比起来只能算是入门，不敢妄言，愿意进入工作室尽心研究，积极参加各种活动。', '人工智能', '人工智能学院', NULL, 2020, NULL, '未发送', 0);
INSERT INTO `student` VALUES (37, '单笑轩', '，21087405', 'sxx2671533862@163.com', NULL, 9, '泰达校区', '13783836016', '大家好，我是单笑轩，来自经管学院的物管专业。对于实验室，我很感兴趣。我最喜欢实验室的那种氛围。喜欢实验室的那种很忙的状态，每个人都在忙于自己的事情。对于Python我从B站上看了几节视频，感到很有趣，但是我自己是一个小白（就是啥都不会）。很想加入实验室这里，提高自我。（编不下去了，就到这里了）', '物流管理与工程类', '经济与管理学院', NULL, 20, NULL, '未发送', 0);
INSERT INTO `student` VALUES (38, '何韦森', '21103310', 'sakitam2373@gmail.com', NULL, 9, '泰达校区', '13820644137', '本人是一个热爱计算机相关的菜鸟。在高中及以前阶段的学习中我有过一些Linux基础，学过一点点C，有一些Python基础，写过几个小型项目。\n用过的Linux:Debian、Ubuntu、Archlinux、CentOS...\n会一点基础PS，Pr。\n我的Github主页：https://github.com/Sakitami。\n我的博客：https://blog.skihome.xyz', '软件工程', '人工智能', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (39, '余思舰', '21032308', '2879954692@qq.com', NULL, 5, '泰达校区', '15109083662', '我不是计算机相关专业学生，但我仍然对计算机充满兴趣。我最想了解的是计算机程序是如何运行起来的 所以我兴趣方向是c语言。之前我对程序的运行原理只停留在好奇，但在假期我知道学校有创新实验室这个学生组织之后我便努力将好奇转换成行动，虽然我努力自学了一段时间c语言，但我在c语言上仍然是一个菜鸡所以我希望在实验室中提高自己c语言能力，并成功加入创新实验室。', '高分子材料与工程', '化工与材料学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (40, '井彤彤', '21206139', '15893216455@163.com', NULL, 9, '泰达校区', '18822753537', '本人性格开朗阳光，热爱学习，品德优良。热衷参加各类比赛以及学科竞赛，积极友好以在团队中积极配合，友好互助。对科协神往已久，学习过一点Pr PS对计算机编程很感兴趣，不过一直没有机会，科协的环境非常适合我。我刻苦努力，不怕秃头，为热爱的事情一往无前。希望科协给我一个锻炼的机会，万分感谢。', '生物工程酿造与蒸馏', '生物工程', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (41, '史师赫', '21206219', '23247702@qq.com', NULL, 9, '泰达校区', '13811600193', '我小时候就对编程产生了兴趣，在小学时加入了校单片机编程队。在中学时，我对编程兴趣不减，但苦于学业压力没能继续学习，但是当时正值网络兴起之际，我在网上发现了许多编程大神，让我看到了编程的酷炫。这为我打开了新世界的大门。到了大学我终于有了自己的时间，终于可以追逐我的爱好了。我很珍惜这次学习的机会，希望学长学姐们可以考虑我', '酿造与蒸馏', '生物学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (42, '徐佳艺', '21103428', '3227023459@qq.com', NULL, 1, '泰达校区', '188885740119', '学长学姐们好！我是电脑小白一个，基本算是零基础，但是我有热情有冲劲，对电脑方面有浓厚的兴趣，也非常希望能加入实验室这个大家庭。平时业余爱好是钢琴和架子鼓。希望学长学姐能给我一个向你们学习的机会！', '软件工程', '人工智能学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (43, '刘志业', '20105119', '2861160067@qq.com', NULL, 9, '泰达校区', '13435328800', '技能:掌握一定的c语言、Python、tkinter、pygame、爬虫基础与进阶、scrapy框架、sql语句、Django后端框架，了解一些简单html、css、js基础，目前刚开始学linux命令。\n方向:希望以后当一名后端码农。\n简短介绍:贪玩又努力，不难相处，向往有良好学习氛围的团队（创客）。', '智能科学与技术', '人工智能', NULL, 2020, NULL, '未发送', 0);
INSERT INTO `student` VALUES (44, '陈晨', '21088224', 'cc1795286739@163.com', NULL, 6, '泰达校区', '13230790289', '  大家好，我叫陈晨，是21级人力资源管理2班的一名学生，来自燕赵之地河北，很高兴能有机会认识实验室。\n   我的兴趣爱好是看小说听音乐，也希望在大学发现自己更加喜欢的东西！比如我想进咱们的设计组，就是比较喜欢ps。\n  在生活中本人是一个活泼开朗的人，喜欢和别人交流，非常喜欢干活！ 在学习上，我自认为自己是一个执行力较强的人，在高中被学校评为沧州市“三好学生”，平时通过自己努力也多次考进年级前五', '人力资源管理', '经济与管理', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (45, '胡锦添', '21087214', '384607415@qq.com', NULL, 5, '泰达校区', '18888509180', '为什么一定要填自我介绍QAQ', '物流管理与工程类', '经济与管理学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (46, '裘粟', '21181231', '2373490803@qq.com', NULL, 6, '泰达校区', '18888798677', '有一定的ps基础，现在也在接单，在一些汉化组工作，有嵌字经验。做艺术团工作室的迎新晚会志愿者，制作晚会的主vi。mc建筑党玩家，设计创造过一些小型建筑，对平面设计兴趣浓厚，希望学习pr与id等。', '国际经济与贸易', '经济与管理学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (47, '赵阳', '21101222', '3511515208@qq.com', NULL, 5, '泰达校区', '18649210992', '我的名字是赵阳，来自人工智能学院计科二班，为人积极向上，具有一定的理科思维，热爱学习，喜欢探索，自律性较好并且学习能力很强，本心对于c语言和编程拥有和大的兴趣和爱好，所以想要加入这样一个具有活力和能量的组织，希望能在这里认识更多志同道合的人一起进步，一起变得更加优秀。', '计算机科学与技术', '人工智能', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (48, '宋迎党', '21101121', '2889015731@qq.com', NULL, 5, '泰达校区', '13256255258', '  我来自人工智能学院的计算机科学与技术专业，对C语言怀有浓厚的兴趣，作为一名志愿成为前端工程师的小白，我想在大一学好C语言，为以后的路打好基础。虽然我没有很好的预习，但是肯吃苦，能下功夫。希望前辈可以给我这次学习的机会。', '计算机科学与技术', '人工智能学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (49, '侯嘉诺', '21201405', '2249665308@qq.com', NULL, 1, '泰达校区', '13832174379', '大佬们好，我是零基础小白，最近刚开学的时候先接触了C语言，然后懵懵的看到了二维数组那里，我比较喜欢咱们这里的氛围，都能找到一群志同道合，钻研技术的伙伴们，我虽然才刚接触编程语言，技术还没入门，但我对这方面比较感兴趣，有较大热情。我超级喜欢这里的氛围，尤其是有一起上进的小伙伴们，希望能与大家共同学习一起进步', '中日计算机科学与技术', '人工智能学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (50, '张雪晴', '21101225', '2013311929@qq.com', NULL, 9, '泰达校区', '18512208193', '我来自天津市宝坻区，性格乐观开朗，做事认真负责，有耐心，对计算机很感兴趣，但没有具体接触过，想要系统地学习。', '计算机科学与技术', '人工智能', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (51, '赵晓曼', '21101328', '2936353537@qq.con', NULL, 5, '泰达校区', '18859695262', '我对各种语言都有兴趣学习，既然选择了这样一个专业，就需要多多学习，我以前没有接触过计算机方向的领域，但是我相信在我的努力下能寻找到自己感兴趣的领域并将其学精学实在。', '计科', '人工智能', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (52, '徐文涛', '21057204', '1194177192@qq.com', NULL, 11, '泰达校区', '15293035068', '学长学姐好，我叫徐文涛，来自甘肃临夏。我平时喜欢折腾计算机，手机，也非常关注各类新数码产品，曾在酷安发布过一篇刷机教程，并认真回复过评论区的很多问题。对于数码产品有着极高的热情，乐于接受新事物，新方法。平时也喜欢制作一些高达模型，所以也具有一定的动手能力，也在高中时期帮同学们解决过一些手机，电脑上的问题。所以我希望能在实验室找到一些有着相同爱好的朋友，能和他们互相学习，互相进步，获取一些新知识。', '海洋资源开发技术', '海洋与环境学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (53, '李依凡', '20142320', '1242391930@qq.com', NULL, 11, '泰达校区', '15383119312', '你好。我目前水平和基础一般，和大一小白差不多，但在努力学了已经。我最近规划就是打好基础，先入好门，才接触编程不久。大一下是跟老师学过VB的，C语言是自学的，JAVA目前也在自学，都学的不是特别细特别好，希望可以得到指导帮助（？。说说我自己再，我性格开朗，和同学们相处的也不错，团队协作能力还行，成绩也还行，还挺喜欢学习的，希望将来多参加一点比赛想和大神切磋交流，没啥爱好，就喜欢听听黑怕看看小说和剧。', '数字媒体技术', '人工智能', NULL, 2020, NULL, '未发送', 0);
INSERT INTO `student` VALUES (54, '王香雪', '21181326', '3504565504@qq.com', NULL, 9, '泰达校区', '15222434312', '对python有浓厚兴趣，有一些基础，想要对python进行更一步的学习，高中获得过生物竞赛一等奖，数学竞赛二等奖', '国际经济与贸易', '经济与管理学院', NULL, 2021, NULL, '未发送', 0);
INSERT INTO `student` VALUES (55, '刘天宇', '21142309', '1073926249@qq.com', NULL, 11, '泰达校区', '16696888835', '我的名字是刘天宇，来自河南焦作。性格开朗，喜欢接触新事物，爱好多，正在努力成为一个自律的人，养生，争取不秃头', '食品科学与工程', '食品科学与工程', NULL, 2021, NULL, '未发送', 0);

-- ----------------------------
-- Table structure for tutor
-- ----------------------------
DROP TABLE IF EXISTS `tutor`;
CREATE TABLE `tutor`  (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salt` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `campus` enum('河西校区','泰达校区') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '泰达校区',
  `group_id` int(11) NULL DEFAULT NULL,
  `qq` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `roleType` enum('tutor','leader') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT 'tutor',
  `status` enum('已审核','未审核') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '未审核',
  PRIMARY KEY (`uid`) USING BTREE,
  INDEX `group_id`(`group_id`) USING BTREE,
  CONSTRAINT `tutor_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tutor
-- ----------------------------
INSERT INTO `tutor` VALUES (5, 'zyd-admin', 'df0229ee5af2b85242d10bf841ae5711', 'fEePoZvYXyERPVTD', '123', '河西校区', 1, '178320369@qq.com', 'leader', '未审核');
INSERT INTO `tutor` VALUES (8, 'lianux-admin', 'df0229ee5af2b85242d10bf841ae5711', 'fEePoZvYXyERPVTD', '178320360@qq.com', '泰达校区', 4, '178320369@qq.com', 'leader', '未审核');
INSERT INTO `tutor` VALUES (9, 'xiaojian-admin', 'df0229ee5af2b85242d10bf841ae5711', 'fEePoZvYXyERPVTD', NULL, '河西校区', 5, '', 'leader', '未审核');
INSERT INTO `tutor` VALUES (10, '张业頔', 'ae506b557bbeb9dbed624cc68b2b7e18', 'e6wEkzyP3NJvKoVE', '123', '河西校区', 1, '123456', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (19, '陈文宇', '6ea40d3a1dcf84a939e0a666236abd17', 'uzkUv0p6b5oEY289', 'qaz123456', '泰达校区', 1, '2575890158', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (20, '徐以鹏', '8e169c9f8acd0a452c38ba969490b71e', 'sioIvrnzfVSv4a5B', '20020102XYPxyp', '泰达校区', 9, '2511864242', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (21, '钱建海', '19f8c92d723f064c65152a81d303c503', 'KC1o4WlVyBZAD5C3', 'qjh20060419', '泰达校区', 5, '1397932042', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (22, '宋新晨', 'cf0e2d45a5f56fdb19ef0b3994358fa1', 'VjlJnW1o8qbRwOBG', 'Song20020114', '泰达校区', 5, 'song20020114', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (23, '陈钰霖', '55216805c9797caec70ffee609ee0978', 'Ssq2GkVI3XaQIgh5', 'q2453303961', '泰达校区', 5, '2453303961', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (24, '刘建华', '5b50a159348150cbef4e7357692c2a9a', 'Wzz0SuBkNMqGpqAG', '3177227893lJH', '泰达校区', 10, '3177227893', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (25, '李阳', 'd9866ec44a06ec65912b8c1848bdb9c5', 'TWHG5aViCH1atRQj', '20011123wy', '泰达校区', 9, '3115783713', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (26, '马诗诗', '5462b0a2ae1a8f3a7a303c56bbc899fc', 'behiB2FJLRm8WoOl', 'Vukyu664168', '泰达校区', 6, '1434236033', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (27, '朱佳雯', '8b7307bd8918599715656ababce7b687', 'v3DKwPLYuAcs1PWY', 'zjw20020506', '泰达校区', 6, '907701138', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (28, '18063112陈雯', '2edf278b39f50c7fe9b6edf8099a3801', 'YCXGX1rvcSAwGlC6', 'chenwen0320/', '泰达校区', 6, '1959003910', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (29, '王浩然', 'f39605ae7dfda3a12d5b1d854afd35c8', 'h9jNQ11xpwatiHeE', 'whr20010831', '泰达校区', 1, '1845812998', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (30, '陈泽佳', '849d6d7cf1d38b5344aff32cebd41855', 'wGjmYV7j2lQORTQo', '123', '泰达校区', 11, '1143144598', 'tutor', '未审核');
INSERT INTO `tutor` VALUES (31, '叶富川', 'eab7938cfa796e37a5b712d4b2350afe', 'XftLhS7BWh0C1Dev', '2097639788', '泰达校区', 10, '2097639788', 'tutor', '未审核');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
