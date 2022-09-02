/*
 Navicat Premium Data Transfer

 Source Server         : mysql-data
 Source Server Type    : MySQL
 Source Server Version : 50650
 Source Host           : localhost:3306
 Source Schema         : imaker

 Target Server Type    : MySQL
 Target Server Version : 50650
 File Encoding         : 65001

 Date: 12/10/2021 11:00:22
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
INSERT INTO `alembic_version` VALUES ('9ace33f47d6f');

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
-- Table structure for group
-- ----------------------------
DROP TABLE IF EXISTS `group`;
CREATE TABLE `group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of group
-- ----------------------------
INSERT INTO `group` VALUES (1, '前端');
INSERT INTO `group` VALUES (2, '后端');
INSERT INTO `group` VALUES (4, 'Rust');
INSERT INTO `group` VALUES (5, 'C语言');
INSERT INTO `group` VALUES (6, '设计');

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
  `email_status` enum('已发送','未发送') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '未发送',
  `rate` int(11) NULL DEFAULT NULL,
  `status` enum('第一轮面试','第二轮面试','第三轮面试','通过','不通过','未审核') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '未审核',
  PRIMARY KEY (`uid`) USING BTREE,
  INDEX `group_id`(`group_id`) USING BTREE,
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (2, '张业頔', '20011204', '178320369@qq.com', '2021-09-25', 1, '河西校区', '12312312', '123123123123', '机械', '机械', '123123123', 2020, '已发送', 3, '不通过');
INSERT INTO `student` VALUES (3, 'zyddadsasd', '123123123', '123123123@qq.com', NULL, 1, '河西校区', '123123123', '12312312', '12312', '123123', NULL, 2012, '未发送', 0, '未审核');

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
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tutor
-- ----------------------------
INSERT INTO `tutor` VALUES (8, 'lianux-admin', 'df0229ee5af2b85242d10bf841ae5711', 'fEePoZvYXyERPVTD', '178320360@qq.com', '泰达校区', 4, '178320369@qq.com', 'leader', '未审核');
INSERT INTO `tutor` VALUES (9, 'xiaojian-admin', 'df0229ee5af2b85242d10bf841ae5711', 'fEePoZvYXyERPVTD', NULL, '河西校区', 5, '', 'leader', '未审核');

SET FOREIGN_KEY_CHECKS = 1;
