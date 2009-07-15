--
-- Generated from mysql2pgsql.perl
-- hand-hacked a bit by Paul Winkler


--
-- http://gborg.postgresql.org/project/mysql2psql/
-- (c) 2001 - 2007 Jose M. Duarte, Joseph Speigle
--

-- warnings are printed for drop tables if they do not exist
-- please see http://archives.postgresql.org/pgsql-novice/2004-10/msg00158.php

-- ##############################################################
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

-- MySQL dump 10.11
--
-- Host: localhost    Database: pvoter_org
-- ------------------------------------------------------
-- Server version	5.0.51a-24+lenny1


--
-- Table structure for table districts
--

DROP SEQUENCE IF EXISTS "districts_id_seq" CASCADE ;
DROP TABLE IF EXISTS "districts" CASCADE;


CREATE SEQUENCE "districts_id_seq"  START WITH 247 ;

CREATE TABLE  "districts" (
   "id" integer DEFAULT nextval('"districts_id_seq"') NOT NULL,
   "state"   varchar(255) NOT NULL, 
   "district_type"   varchar(255) NOT NULL, 
   "level_name"   varchar(255) NOT NULL, 
   "district_name"   varchar(255) NOT NULL, 
   primary key ("id")
)   ;

/*!40000 ALTER TABLE districts DISABLE KEYS */;

--
-- Dumping data for table districts
--

INSERT INTO "districts" VALUES (1,E'NY',E'State Senate',E'State',E'District 1');
INSERT INTO "districts" VALUES (2,E'NY',E'State Senate',E'State',E'District 2');
INSERT INTO "districts" VALUES (3,E'NY',E'State Senate',E'State',E'District 3');
INSERT INTO "districts" VALUES (4,E'NY',E'State Senate',E'State',E'District 4');
INSERT INTO "districts" VALUES (5,E'NY',E'State Senate',E'State',E'District 5');
INSERT INTO "districts" VALUES (6,E'NY',E'State Senate',E'State',E'District 6');
INSERT INTO "districts" VALUES (7,E'NY',E'State Senate',E'State',E'District 7');
INSERT INTO "districts" VALUES (8,E'NY',E'State Senate',E'State',E'District 8');
INSERT INTO "districts" VALUES (9,E'NY',E'State Senate',E'State',E'District 9');
INSERT INTO "districts" VALUES (10,E'NY',E'State Senate',E'State',E'District 10');
INSERT INTO "districts" VALUES (11,E'NY',E'State Senate',E'State',E'District 11');
INSERT INTO "districts" VALUES (12,E'NY',E'State Senate',E'State',E'District 12');
INSERT INTO "districts" VALUES (13,E'NY',E'State Senate',E'State',E'District 13');
INSERT INTO "districts" VALUES (14,E'NY',E'State Senate',E'State',E'District 14');
INSERT INTO "districts" VALUES (15,E'NY',E'State Senate',E'State',E'District 15');
INSERT INTO "districts" VALUES (16,E'NY',E'State Senate',E'State',E'District 16');
INSERT INTO "districts" VALUES (17,E'NY',E'State Senate',E'State',E'District 17');
INSERT INTO "districts" VALUES (18,E'NY',E'State Senate',E'State',E'District 18');
INSERT INTO "districts" VALUES (19,E'NY',E'State Senate',E'State',E'District 19');
INSERT INTO "districts" VALUES (20,E'NY',E'State Senate',E'State',E'District 20');
INSERT INTO "districts" VALUES (21,E'NY',E'State Senate',E'State',E'District 21');
INSERT INTO "districts" VALUES (22,E'NY',E'State Senate',E'State',E'District 22');
INSERT INTO "districts" VALUES (23,E'NY',E'State Senate',E'State',E'District 23');
INSERT INTO "districts" VALUES (24,E'NY',E'State Senate',E'State',E'District 24');
INSERT INTO "districts" VALUES (25,E'NY',E'State Senate',E'State',E'District 25');
INSERT INTO "districts" VALUES (26,E'NY',E'State Senate',E'State',E'District 26');
INSERT INTO "districts" VALUES (27,E'NY',E'State Senate',E'State',E'District 27');
INSERT INTO "districts" VALUES (28,E'NY',E'State Senate',E'State',E'District 28');
INSERT INTO "districts" VALUES (29,E'NY',E'State Senate',E'State',E'District 29');
INSERT INTO "districts" VALUES (30,E'NY',E'State Senate',E'State',E'District 30');
INSERT INTO "districts" VALUES (31,E'NY',E'State Senate',E'State',E'District 31');
INSERT INTO "districts" VALUES (32,E'NY',E'State Senate',E'State',E'District 32');
INSERT INTO "districts" VALUES (33,E'NY',E'State Senate',E'State',E'District 33');
INSERT INTO "districts" VALUES (34,E'NY',E'State Senate',E'State',E'District 34');
INSERT INTO "districts" VALUES (35,E'NY',E'State Senate',E'State',E'District 35');
INSERT INTO "districts" VALUES (36,E'NY',E'State Senate',E'State',E'District 36');
INSERT INTO "districts" VALUES (37,E'NY',E'State Senate',E'State',E'District 37');
INSERT INTO "districts" VALUES (38,E'NY',E'State Senate',E'State',E'District 38');
INSERT INTO "districts" VALUES (39,E'NY',E'State Senate',E'State',E'District 39');
INSERT INTO "districts" VALUES (40,E'NY',E'State Senate',E'State',E'District 40');
INSERT INTO "districts" VALUES (41,E'NY',E'State Senate',E'State',E'District 41');
INSERT INTO "districts" VALUES (42,E'NY',E'State Senate',E'State',E'District 42');
INSERT INTO "districts" VALUES (43,E'NY',E'State Senate',E'State',E'District 43');
INSERT INTO "districts" VALUES (44,E'NY',E'State Senate',E'State',E'District 44');
INSERT INTO "districts" VALUES (45,E'NY',E'State Senate',E'State',E'District 45');
INSERT INTO "districts" VALUES (46,E'NY',E'State Senate',E'State',E'District 46');
INSERT INTO "districts" VALUES (47,E'NY',E'State Senate',E'State',E'District 47');
INSERT INTO "districts" VALUES (48,E'NY',E'State Senate',E'State',E'District 48');
INSERT INTO "districts" VALUES (49,E'NY',E'State Senate',E'State',E'District 49');
INSERT INTO "districts" VALUES (50,E'NY',E'State Senate',E'State',E'District 50');
INSERT INTO "districts" VALUES (51,E'NY',E'State Senate',E'State',E'District 51');
INSERT INTO "districts" VALUES (52,E'NY',E'State Senate',E'State',E'District 52');
INSERT INTO "districts" VALUES (53,E'NY',E'State Senate',E'State',E'District 53');
INSERT INTO "districts" VALUES (54,E'NY',E'State Senate',E'State',E'District 54');
INSERT INTO "districts" VALUES (55,E'NY',E'State Senate',E'State',E'District 55');
INSERT INTO "districts" VALUES (56,E'NY',E'State Senate',E'State',E'District 56');
INSERT INTO "districts" VALUES (57,E'NY',E'State Senate',E'State',E'District 57');
INSERT INTO "districts" VALUES (58,E'NY',E'State Senate',E'State',E'District 58');
INSERT INTO "districts" VALUES (59,E'NY',E'State Senate',E'State',E'District 59');
INSERT INTO "districts" VALUES (60,E'NY',E'State Senate',E'State',E'District 60');
INSERT INTO "districts" VALUES (61,E'NY',E'State Senate',E'State',E'District 61');
INSERT INTO "districts" VALUES (62,E'NY',E'State Senate',E'State',E'District 62');
INSERT INTO "districts" VALUES (63,E'NY',E'U.S. House',E'Federal',E'District 1');
INSERT INTO "districts" VALUES (64,E'NY',E'U.S. House',E'Federal',E'District 2');
INSERT INTO "districts" VALUES (65,E'NY',E'U.S. House',E'Federal',E'District 3');
INSERT INTO "districts" VALUES (66,E'NY',E'U.S. House',E'Federal',E'District 4');
INSERT INTO "districts" VALUES (67,E'NY',E'U.S. House',E'Federal',E'District 5');
INSERT INTO "districts" VALUES (68,E'NY',E'U.S. House',E'Federal',E'District 6');
INSERT INTO "districts" VALUES (69,E'NY',E'U.S. House',E'Federal',E'District 7');
INSERT INTO "districts" VALUES (70,E'NY',E'U.S. House',E'Federal',E'District 8');
INSERT INTO "districts" VALUES (71,E'NY',E'U.S. House',E'Federal',E'District 9');
INSERT INTO "districts" VALUES (72,E'NY',E'U.S. House',E'Federal',E'District 10');
INSERT INTO "districts" VALUES (73,E'NY',E'U.S. House',E'Federal',E'District 11');
INSERT INTO "districts" VALUES (74,E'NY',E'U.S. House',E'Federal',E'District 12');
INSERT INTO "districts" VALUES (75,E'NY',E'U.S. House',E'Federal',E'District 13');
INSERT INTO "districts" VALUES (76,E'NY',E'U.S. House',E'Federal',E'District 14');
INSERT INTO "districts" VALUES (77,E'NY',E'U.S. House',E'Federal',E'District 15');
INSERT INTO "districts" VALUES (78,E'NY',E'U.S. House',E'Federal',E'District 16');
INSERT INTO "districts" VALUES (79,E'NY',E'U.S. House',E'Federal',E'District 17');
INSERT INTO "districts" VALUES (80,E'NY',E'U.S. House',E'Federal',E'District 18');
INSERT INTO "districts" VALUES (81,E'NY',E'U.S. House',E'Federal',E'District 19');
INSERT INTO "districts" VALUES (82,E'NY',E'U.S. House',E'Federal',E'District 20');
INSERT INTO "districts" VALUES (83,E'NY',E'U.S. House',E'Federal',E'District 21');
INSERT INTO "districts" VALUES (84,E'NY',E'U.S. House',E'Federal',E'District 22');
INSERT INTO "districts" VALUES (85,E'NY',E'U.S. House',E'Federal',E'District 23');
INSERT INTO "districts" VALUES (86,E'NY',E'U.S. House',E'Federal',E'District 24');
INSERT INTO "districts" VALUES (87,E'NY',E'U.S. House',E'Federal',E'District 25');
INSERT INTO "districts" VALUES (88,E'NY',E'U.S. House',E'Federal',E'District 26');
INSERT INTO "districts" VALUES (89,E'NY',E'U.S. House',E'Federal',E'District 27');
INSERT INTO "districts" VALUES (90,E'NY',E'U.S. House',E'Federal',E'District 28');
INSERT INTO "districts" VALUES (91,E'NY',E'U.S. House',E'Federal',E'District 29');
INSERT INTO "districts" VALUES (92,E'NY',E'State Assembly',E'State',E'District 1');
INSERT INTO "districts" VALUES (93,E'NY',E'State Assembly',E'State',E'District 2');
INSERT INTO "districts" VALUES (94,E'NY',E'State Assembly',E'State',E'District 3');
INSERT INTO "districts" VALUES (95,E'NY',E'State Assembly',E'State',E'District 4');
INSERT INTO "districts" VALUES (96,E'NY',E'State Assembly',E'State',E'District 5');
INSERT INTO "districts" VALUES (97,E'NY',E'State Assembly',E'State',E'District 6');
INSERT INTO "districts" VALUES (98,E'NY',E'State Assembly',E'State',E'District 7');
INSERT INTO "districts" VALUES (99,E'NY',E'State Assembly',E'State',E'District 8');
INSERT INTO "districts" VALUES (100,E'NY',E'State Assembly',E'State',E'District 9');
INSERT INTO "districts" VALUES (101,E'NY',E'State Assembly',E'State',E'District 10');
INSERT INTO "districts" VALUES (102,E'NY',E'State Assembly',E'State',E'District 11');
INSERT INTO "districts" VALUES (103,E'NY',E'State Assembly',E'State',E'District 12');
INSERT INTO "districts" VALUES (104,E'NY',E'State Assembly',E'State',E'District 13');
INSERT INTO "districts" VALUES (105,E'NY',E'State Assembly',E'State',E'District 14');
INSERT INTO "districts" VALUES (106,E'NY',E'State Assembly',E'State',E'District 15');
INSERT INTO "districts" VALUES (107,E'NY',E'State Assembly',E'State',E'District 16');
INSERT INTO "districts" VALUES (108,E'NY',E'State Assembly',E'State',E'District 17');
INSERT INTO "districts" VALUES (109,E'NY',E'State Assembly',E'State',E'District 18');
INSERT INTO "districts" VALUES (110,E'NY',E'State Assembly',E'State',E'District 19');
INSERT INTO "districts" VALUES (111,E'NY',E'State Assembly',E'State',E'District 20');
INSERT INTO "districts" VALUES (112,E'NY',E'State Assembly',E'State',E'District 21');
INSERT INTO "districts" VALUES (113,E'NY',E'State Assembly',E'State',E'District 22');
INSERT INTO "districts" VALUES (114,E'NY',E'State Assembly',E'State',E'District 23');
INSERT INTO "districts" VALUES (115,E'NY',E'State Assembly',E'State',E'District 24');
INSERT INTO "districts" VALUES (116,E'NY',E'State Assembly',E'State',E'District 25');
INSERT INTO "districts" VALUES (117,E'NY',E'State Assembly',E'State',E'District 26');
INSERT INTO "districts" VALUES (118,E'NY',E'State Assembly',E'State',E'District 27');
INSERT INTO "districts" VALUES (119,E'NY',E'State Assembly',E'State',E'District 28');
INSERT INTO "districts" VALUES (120,E'NY',E'State Assembly',E'State',E'District 29');
INSERT INTO "districts" VALUES (121,E'NY',E'State Assembly',E'State',E'District 30');
INSERT INTO "districts" VALUES (122,E'NY',E'State Assembly',E'State',E'District 31');
INSERT INTO "districts" VALUES (123,E'NY',E'State Assembly',E'State',E'District 32');
INSERT INTO "districts" VALUES (124,E'NY',E'State Assembly',E'State',E'District 33');
INSERT INTO "districts" VALUES (125,E'NY',E'State Assembly',E'State',E'District 34');
INSERT INTO "districts" VALUES (126,E'NY',E'State Assembly',E'State',E'District 35');
INSERT INTO "districts" VALUES (127,E'NY',E'State Assembly',E'State',E'District 36');
INSERT INTO "districts" VALUES (128,E'NY',E'State Assembly',E'State',E'District 37');
INSERT INTO "districts" VALUES (129,E'NY',E'State Assembly',E'State',E'District 38');
INSERT INTO "districts" VALUES (130,E'NY',E'State Assembly',E'State',E'District 39');
INSERT INTO "districts" VALUES (131,E'NY',E'State Assembly',E'State',E'District 40');
INSERT INTO "districts" VALUES (132,E'NY',E'State Assembly',E'State',E'District 41');
INSERT INTO "districts" VALUES (133,E'NY',E'State Assembly',E'State',E'District 42');
INSERT INTO "districts" VALUES (134,E'NY',E'State Assembly',E'State',E'District 43');
INSERT INTO "districts" VALUES (135,E'NY',E'State Assembly',E'State',E'District 44');
INSERT INTO "districts" VALUES (136,E'NY',E'State Assembly',E'State',E'District 45');
INSERT INTO "districts" VALUES (137,E'NY',E'State Assembly',E'State',E'District 46');
INSERT INTO "districts" VALUES (138,E'NY',E'State Assembly',E'State',E'District 47');
INSERT INTO "districts" VALUES (139,E'NY',E'State Assembly',E'State',E'District 48');
INSERT INTO "districts" VALUES (140,E'NY',E'State Assembly',E'State',E'District 49');
INSERT INTO "districts" VALUES (141,E'NY',E'State Assembly',E'State',E'District 50');
INSERT INTO "districts" VALUES (142,E'NY',E'State Assembly',E'State',E'District 51');
INSERT INTO "districts" VALUES (143,E'NY',E'State Assembly',E'State',E'District 52');
INSERT INTO "districts" VALUES (144,E'NY',E'State Assembly',E'State',E'District 53');
INSERT INTO "districts" VALUES (145,E'NY',E'State Assembly',E'State',E'District 54');
INSERT INTO "districts" VALUES (146,E'NY',E'State Assembly',E'State',E'District 55');
INSERT INTO "districts" VALUES (147,E'NY',E'State Assembly',E'State',E'District 56');
INSERT INTO "districts" VALUES (148,E'NY',E'State Assembly',E'State',E'District 57');
INSERT INTO "districts" VALUES (149,E'NY',E'State Assembly',E'State',E'District 58');
INSERT INTO "districts" VALUES (150,E'NY',E'State Assembly',E'State',E'District 59');
INSERT INTO "districts" VALUES (151,E'NY',E'State Assembly',E'State',E'District 60');
INSERT INTO "districts" VALUES (152,E'NY',E'State Assembly',E'State',E'District 61');
INSERT INTO "districts" VALUES (153,E'NY',E'State Assembly',E'State',E'District 62');
INSERT INTO "districts" VALUES (154,E'NY',E'State Assembly',E'State',E'District 63');
INSERT INTO "districts" VALUES (155,E'NY',E'State Assembly',E'State',E'District 64');
INSERT INTO "districts" VALUES (156,E'NY',E'State Assembly',E'State',E'District 65');
INSERT INTO "districts" VALUES (157,E'NY',E'State Assembly',E'State',E'District 66');
INSERT INTO "districts" VALUES (158,E'NY',E'State Assembly',E'State',E'District 67');
INSERT INTO "districts" VALUES (159,E'NY',E'State Assembly',E'State',E'District 68');
INSERT INTO "districts" VALUES (160,E'NY',E'State Assembly',E'State',E'District 69');
INSERT INTO "districts" VALUES (161,E'NY',E'State Assembly',E'State',E'District 70');
INSERT INTO "districts" VALUES (162,E'NY',E'State Assembly',E'State',E'District 71');
INSERT INTO "districts" VALUES (163,E'NY',E'State Assembly',E'State',E'District 72');
INSERT INTO "districts" VALUES (164,E'NY',E'State Assembly',E'State',E'District 73');
INSERT INTO "districts" VALUES (165,E'NY',E'State Assembly',E'State',E'District 74');
INSERT INTO "districts" VALUES (166,E'NY',E'State Assembly',E'State',E'District 75');
INSERT INTO "districts" VALUES (167,E'NY',E'State Assembly',E'State',E'District 76');
INSERT INTO "districts" VALUES (168,E'NY',E'State Assembly',E'State',E'District 77');
INSERT INTO "districts" VALUES (169,E'NY',E'State Assembly',E'State',E'District 78');
INSERT INTO "districts" VALUES (170,E'NY',E'State Assembly',E'State',E'District 79');
INSERT INTO "districts" VALUES (171,E'NY',E'State Assembly',E'State',E'District 80');
INSERT INTO "districts" VALUES (172,E'NY',E'State Assembly',E'State',E'District 81');
INSERT INTO "districts" VALUES (173,E'NY',E'State Assembly',E'State',E'District 82');
INSERT INTO "districts" VALUES (174,E'NY',E'State Assembly',E'State',E'District 83');
INSERT INTO "districts" VALUES (175,E'NY',E'State Assembly',E'State',E'District 84');
INSERT INTO "districts" VALUES (176,E'NY',E'State Assembly',E'State',E'District 85');
INSERT INTO "districts" VALUES (177,E'NY',E'State Assembly',E'State',E'District 86');
INSERT INTO "districts" VALUES (178,E'NY',E'State Assembly',E'State',E'District 87');
INSERT INTO "districts" VALUES (179,E'NY',E'State Assembly',E'State',E'District 88');
INSERT INTO "districts" VALUES (180,E'NY',E'State Assembly',E'State',E'District 89');
INSERT INTO "districts" VALUES (181,E'NY',E'State Assembly',E'State',E'District 90');
INSERT INTO "districts" VALUES (182,E'NY',E'State Assembly',E'State',E'District 91');
INSERT INTO "districts" VALUES (183,E'NY',E'State Assembly',E'State',E'District 92');
INSERT INTO "districts" VALUES (184,E'NY',E'State Assembly',E'State',E'District 93');
INSERT INTO "districts" VALUES (185,E'NY',E'State Assembly',E'State',E'District 94');
INSERT INTO "districts" VALUES (186,E'NY',E'State Assembly',E'State',E'District 95');
INSERT INTO "districts" VALUES (187,E'NY',E'State Assembly',E'State',E'District 96');
INSERT INTO "districts" VALUES (188,E'NY',E'State Assembly',E'State',E'District 97');
INSERT INTO "districts" VALUES (189,E'NY',E'State Assembly',E'State',E'District 98');
INSERT INTO "districts" VALUES (190,E'NY',E'State Assembly',E'State',E'District 99');
INSERT INTO "districts" VALUES (191,E'NY',E'State Assembly',E'State',E'District 100');
INSERT INTO "districts" VALUES (192,E'NY',E'State Assembly',E'State',E'District 101');
INSERT INTO "districts" VALUES (193,E'NY',E'State Assembly',E'State',E'District 102');
INSERT INTO "districts" VALUES (194,E'NY',E'State Assembly',E'State',E'District 103');
INSERT INTO "districts" VALUES (195,E'NY',E'State Assembly',E'State',E'District 104');
INSERT INTO "districts" VALUES (196,E'NY',E'State Assembly',E'State',E'District 105');
INSERT INTO "districts" VALUES (197,E'NY',E'State Assembly',E'State',E'District 106');
INSERT INTO "districts" VALUES (198,E'NY',E'State Assembly',E'State',E'District 107');
INSERT INTO "districts" VALUES (199,E'NY',E'State Assembly',E'State',E'District 108');
INSERT INTO "districts" VALUES (200,E'NY',E'State Assembly',E'State',E'District 109');
INSERT INTO "districts" VALUES (201,E'NY',E'State Assembly',E'State',E'District 110');
INSERT INTO "districts" VALUES (202,E'NY',E'State Assembly',E'State',E'District 111');
INSERT INTO "districts" VALUES (203,E'NY',E'State Assembly',E'State',E'District 112');
INSERT INTO "districts" VALUES (204,E'NY',E'State Assembly',E'State',E'District 113');
INSERT INTO "districts" VALUES (205,E'NY',E'State Assembly',E'State',E'District 114');
INSERT INTO "districts" VALUES (206,E'NY',E'State Assembly',E'State',E'District 115');
INSERT INTO "districts" VALUES (207,E'NY',E'State Assembly',E'State',E'District 116');
INSERT INTO "districts" VALUES (208,E'NY',E'State Assembly',E'State',E'District 117');
INSERT INTO "districts" VALUES (209,E'NY',E'State Assembly',E'State',E'District 118');
INSERT INTO "districts" VALUES (210,E'NY',E'State Assembly',E'State',E'District 119');
INSERT INTO "districts" VALUES (211,E'NY',E'State Assembly',E'State',E'District 120');
INSERT INTO "districts" VALUES (212,E'NY',E'State Assembly',E'State',E'District 121');
INSERT INTO "districts" VALUES (213,E'NY',E'State Assembly',E'State',E'District 122');
INSERT INTO "districts" VALUES (214,E'NY',E'State Assembly',E'State',E'District 123');
INSERT INTO "districts" VALUES (215,E'NY',E'State Assembly',E'State',E'District 124');
INSERT INTO "districts" VALUES (216,E'NY',E'State Assembly',E'State',E'District 125');
INSERT INTO "districts" VALUES (217,E'NY',E'State Assembly',E'State',E'District 126');
INSERT INTO "districts" VALUES (218,E'NY',E'State Assembly',E'State',E'District 127');
INSERT INTO "districts" VALUES (219,E'NY',E'State Assembly',E'State',E'District 128');
INSERT INTO "districts" VALUES (220,E'NY',E'State Assembly',E'State',E'District 129');
INSERT INTO "districts" VALUES (221,E'NY',E'State Assembly',E'State',E'District 130');
INSERT INTO "districts" VALUES (222,E'NY',E'State Assembly',E'State',E'District 131');
INSERT INTO "districts" VALUES (223,E'NY',E'State Assembly',E'State',E'District 132');
INSERT INTO "districts" VALUES (224,E'NY',E'State Assembly',E'State',E'District 133');
INSERT INTO "districts" VALUES (225,E'NY',E'State Assembly',E'State',E'District 134');
INSERT INTO "districts" VALUES (226,E'NY',E'State Assembly',E'State',E'District 135');
INSERT INTO "districts" VALUES (227,E'NY',E'State Assembly',E'State',E'District 136');
INSERT INTO "districts" VALUES (228,E'NY',E'State Assembly',E'State',E'District 137');
INSERT INTO "districts" VALUES (229,E'NY',E'State Assembly',E'State',E'District 138');
INSERT INTO "districts" VALUES (230,E'NY',E'State Assembly',E'State',E'District 139');
INSERT INTO "districts" VALUES (231,E'NY',E'State Assembly',E'State',E'District 140');
INSERT INTO "districts" VALUES (232,E'NY',E'State Assembly',E'State',E'District 141');
INSERT INTO "districts" VALUES (233,E'NY',E'State Assembly',E'State',E'District 142');
INSERT INTO "districts" VALUES (234,E'NY',E'State Assembly',E'State',E'District 143');
INSERT INTO "districts" VALUES (235,E'NY',E'State Assembly',E'State',E'District 144');
INSERT INTO "districts" VALUES (236,E'NY',E'State Assembly',E'State',E'District 145');
INSERT INTO "districts" VALUES (237,E'NY',E'State Assembly',E'State',E'District 146');
INSERT INTO "districts" VALUES (238,E'NY',E'State Assembly',E'State',E'District 147');
INSERT INTO "districts" VALUES (239,E'NY',E'State Assembly',E'State',E'District 148');
INSERT INTO "districts" VALUES (240,E'NY',E'State Assembly',E'State',E'District 149');
INSERT INTO "districts" VALUES (241,E'NY',E'State Assembly',E'State',E'District 150');
INSERT INTO "districts" VALUES (242,E'NY',E'U.S. Senate',E'Federal',E'Senior Seat');
INSERT INTO "districts" VALUES (243,E'NY',E'U.S. Senate',E'Federal',E'Junior Seat');
INSERT INTO "districts" VALUES (244,E'NY',E'U.S. Senate',E'Federal',E'District I');
INSERT INTO "districts" VALUES (245,E'NY',E'U.S. Senate',E'Federal',E'District II');
INSERT INTO "districts" VALUES (246,E'NY',E'U.S. Senate',E'Federal',E'District III');

/*!40000 ALTER TABLE districts ENABLE KEYS */;



--
-- Table structure for table districts_meta
--



DROP SEQUENCE IF EXISTS "districts_meta_id_seq" CASCADE ;
DROP TABLE IF EXISTS "districts_meta" CASCADE;


CREATE SEQUENCE "districts_meta_id_seq"  START WITH 248 ;

CREATE TABLE  "districts_meta" (
   "id" integer DEFAULT nextval('"districts_meta_id_seq"') NOT NULL,
   "district_id"   int default NULL, 
   "meta_key"   varchar(255) NOT NULL, 
   "meta_value"   text NOT NULL, 
   primary key ("id")
)   ;

/*!40000 ALTER TABLE districts_meta DISABLE KEYS */;

--
-- Dumping data for table districts_meta
--

INSERT INTO "districts_meta" VALUES (1,1,E'official',E'Kenneth LaValle');
INSERT INTO "districts_meta" VALUES (2,2,E'official',E'John Flanagan');
INSERT INTO "districts_meta" VALUES (3,3,E'official',E'Brian Foley');
INSERT INTO "districts_meta" VALUES (4,4,E'official',E'Owen Johnson');
INSERT INTO "districts_meta" VALUES (5,5,E'official',E'Carl Marcellino');
INSERT INTO "districts_meta" VALUES (6,6,E'official',E'Kemp Hannon');
INSERT INTO "districts_meta" VALUES (7,7,E'official',E'Craig Johnson');
INSERT INTO "districts_meta" VALUES (8,8,E'official',E'Charles Fuschillo');
INSERT INTO "districts_meta" VALUES (9,9,E'official',E'Dean Skelos');
INSERT INTO "districts_meta" VALUES (10,10,E'official',E'Shirley Huntley');
INSERT INTO "districts_meta" VALUES (11,11,E'official',E'Frank Padavan');
INSERT INTO "districts_meta" VALUES (12,12,E'official',E'George Onorato');
INSERT INTO "districts_meta" VALUES (13,13,E'official',E'Hiram Monserrate');
INSERT INTO "districts_meta" VALUES (14,14,E'official',E'Malcolm Smith');
INSERT INTO "districts_meta" VALUES (15,15,E'official',E'Joseph Addabbo Jr.');
INSERT INTO "districts_meta" VALUES (16,16,E'official',E'Toby Ann Stavisky');
INSERT INTO "districts_meta" VALUES (17,17,E'official',E'Martin Dilan');
INSERT INTO "districts_meta" VALUES (18,18,E'official',E'Velmanette Montgomery');
INSERT INTO "districts_meta" VALUES (19,19,E'official',E'John Sampson');
INSERT INTO "districts_meta" VALUES (20,20,E'official',E'Eric Adams');
INSERT INTO "districts_meta" VALUES (21,21,E'official',E'Kevin Parker');
INSERT INTO "districts_meta" VALUES (22,22,E'official',E'Martin Golden');
INSERT INTO "districts_meta" VALUES (23,23,E'official',E'Diane Savino');
INSERT INTO "districts_meta" VALUES (24,24,E'official',E'Andrew Lanza');
INSERT INTO "districts_meta" VALUES (25,25,E'official',E'Daniel Squadron');
INSERT INTO "districts_meta" VALUES (26,26,E'official',E'Liz Krueger');
INSERT INTO "districts_meta" VALUES (27,27,E'official',E'Carl Kruger');
INSERT INTO "districts_meta" VALUES (28,28,E'official',E'JosÃ© Serrano');
INSERT INTO "districts_meta" VALUES (29,29,E'official',E'Thomas Duane');
INSERT INTO "districts_meta" VALUES (30,30,E'official',E'Bill Perkins');
INSERT INTO "districts_meta" VALUES (31,31,E'official',E'Eric Schneiderman');
INSERT INTO "districts_meta" VALUES (32,32,E'official',E'Ruben Diaz');
INSERT INTO "districts_meta" VALUES (33,33,E'official',E'Pedro Espada');
INSERT INTO "districts_meta" VALUES (34,34,E'official',E'Jeffrey Klein');
INSERT INTO "districts_meta" VALUES (35,35,E'official',E'Andrea Stewart-Cousins');
INSERT INTO "districts_meta" VALUES (36,36,E'official',E'Ruth Hassell-Thompson');
INSERT INTO "districts_meta" VALUES (37,37,E'official',E'Suzi Oppenheimer');
INSERT INTO "districts_meta" VALUES (38,38,E'official',E'Thomas Morahan');
INSERT INTO "districts_meta" VALUES (39,39,E'official',E'William Larkin');
INSERT INTO "districts_meta" VALUES (40,40,E'official',E'Vincent Leibell');
INSERT INTO "districts_meta" VALUES (41,41,E'official',E'Stephen Saland');
INSERT INTO "districts_meta" VALUES (42,42,E'official',E'John Bonacic');
INSERT INTO "districts_meta" VALUES (43,43,E'official',E'Roy McDonald');
INSERT INTO "districts_meta" VALUES (44,44,E'official',E'Hugh Farley');
INSERT INTO "districts_meta" VALUES (45,45,E'official',E'Elizabeth O\'C. Little');
INSERT INTO "districts_meta" VALUES (46,46,E'official',E'Neil Breslin');
INSERT INTO "districts_meta" VALUES (47,47,E'official',E'Joseph Griffo');
INSERT INTO "districts_meta" VALUES (48,48,E'official',E'Darrel Aubertine');
INSERT INTO "districts_meta" VALUES (49,49,E'official',E'David Valesky');
INSERT INTO "districts_meta" VALUES (50,50,E'official',E'John DeFrancisco');
INSERT INTO "districts_meta" VALUES (51,51,E'official',E'James Seward');
INSERT INTO "districts_meta" VALUES (52,52,E'official',E'Thomas Libous');
INSERT INTO "districts_meta" VALUES (53,53,E'official',E'George Winner');
INSERT INTO "districts_meta" VALUES (54,54,E'official',E'Michael Nozzolio');
INSERT INTO "districts_meta" VALUES (55,55,E'official',E'James Alesi');
INSERT INTO "districts_meta" VALUES (56,56,E'official',E'Joseph Robach');
INSERT INTO "districts_meta" VALUES (57,57,E'official',E'Catharine Young');
INSERT INTO "districts_meta" VALUES (58,58,E'official',E'William Stachowski');
INSERT INTO "districts_meta" VALUES (59,59,E'official',E'Dale Volker');
INSERT INTO "districts_meta" VALUES (60,60,E'official',E'Antoine Thompson');
INSERT INTO "districts_meta" VALUES (61,61,E'official',E'Michael Ranzenhofer');
INSERT INTO "districts_meta" VALUES (62,62,E'official',E'George Maziarz');
INSERT INTO "districts_meta" VALUES (63,63,E'official',E'Timothy Bishop');
INSERT INTO "districts_meta" VALUES (64,64,E'official',E'Steve Israel');
INSERT INTO "districts_meta" VALUES (65,65,E'official',E'Peter King');
INSERT INTO "districts_meta" VALUES (66,66,E'official',E'Carolyn McCarthy');
INSERT INTO "districts_meta" VALUES (67,67,E'official',E'Gary Ackerman');
INSERT INTO "districts_meta" VALUES (68,68,E'official',E'Gregory Meeks');
INSERT INTO "districts_meta" VALUES (69,69,E'official',E'Joseph Crowley');
INSERT INTO "districts_meta" VALUES (70,70,E'official',E'Jerrold Nadler');
INSERT INTO "districts_meta" VALUES (71,71,E'official',E'Anthony David Weiner');
INSERT INTO "districts_meta" VALUES (72,72,E'official',E'Edolphus Towns');
INSERT INTO "districts_meta" VALUES (73,73,E'official',E'Yvette Clarke');
INSERT INTO "districts_meta" VALUES (74,74,E'official',E'Nydia VelÃ¡zquez');
INSERT INTO "districts_meta" VALUES (75,75,E'official',E'Michael McMahon');
INSERT INTO "districts_meta" VALUES (76,76,E'official',E'Carolyn Maloney');
INSERT INTO "districts_meta" VALUES (77,77,E'official',E'Charles Rangel');
INSERT INTO "districts_meta" VALUES (78,78,E'official',E'JosÃ© Serrano');
INSERT INTO "districts_meta" VALUES (79,79,E'official',E'Eliot Engel');
INSERT INTO "districts_meta" VALUES (80,80,E'official',E'Nita Lowey');
INSERT INTO "districts_meta" VALUES (81,81,E'official',E'John Hall');
INSERT INTO "districts_meta" VALUES (82,83,E'official',E'Paul Tonko');
INSERT INTO "districts_meta" VALUES (83,84,E'official',E'Maurice Hinchey');
INSERT INTO "districts_meta" VALUES (84,85,E'official',E'John McHugh');
INSERT INTO "districts_meta" VALUES (85,86,E'official',E'Michael Arcuri');
INSERT INTO "districts_meta" VALUES (86,87,E'official',E'Daniel Maffei');
INSERT INTO "districts_meta" VALUES (87,88,E'official',E'Christopher Lee');
INSERT INTO "districts_meta" VALUES (88,89,E'official',E'Brian Higgins');
INSERT INTO "districts_meta" VALUES (89,90,E'official',E'Louise Slaughter');
INSERT INTO "districts_meta" VALUES (90,91,E'official',E'Eric Massa');
INSERT INTO "districts_meta" VALUES (91,92,E'official',E'Marc Alessi');
INSERT INTO "districts_meta" VALUES (92,93,E'official',E'Fred Thiele');
INSERT INTO "districts_meta" VALUES (93,94,E'official',E'Patricia Eddington');
INSERT INTO "districts_meta" VALUES (94,95,E'official',E'Steven Englebright');
INSERT INTO "districts_meta" VALUES (95,96,E'official',E'Ginny Fields');
INSERT INTO "districts_meta" VALUES (96,97,E'official',E'Philip Ramos');
INSERT INTO "districts_meta" VALUES (97,98,E'official',E'Michael Fitzpatrick');
INSERT INTO "districts_meta" VALUES (98,99,E'official',E'Philip Boyle');
INSERT INTO "districts_meta" VALUES (99,100,E'official',E'Andrew Raia');
INSERT INTO "districts_meta" VALUES (100,101,E'official',E'James Conte');
INSERT INTO "districts_meta" VALUES (101,102,E'official',E'Robert Sweeney');
INSERT INTO "districts_meta" VALUES (102,103,E'official',E'Joseph Saladino');
INSERT INTO "districts_meta" VALUES (103,104,E'official',E'Charles Lavine');
INSERT INTO "districts_meta" VALUES (104,105,E'official',E'Robert Barra');
INSERT INTO "districts_meta" VALUES (105,106,E'official',E'Robert Walker');
INSERT INTO "districts_meta" VALUES (106,107,E'official',E'Michelle Schimel');
INSERT INTO "districts_meta" VALUES (107,108,E'official',E'Tom McKevitt');
INSERT INTO "districts_meta" VALUES (108,109,E'official',E'Earlene Hooper');
INSERT INTO "districts_meta" VALUES (109,110,E'official',E'David McDonaugh');
INSERT INTO "districts_meta" VALUES (110,111,E'official',E'Harvey Weisenberg');
INSERT INTO "districts_meta" VALUES (111,112,E'official',E'Thomas Alfano');
INSERT INTO "districts_meta" VALUES (112,113,E'official',E'Grace Meng');
INSERT INTO "districts_meta" VALUES (113,114,E'official',E'Audrey Pheffer');
INSERT INTO "districts_meta" VALUES (114,115,E'official',E'Mark Weprin');
INSERT INTO "districts_meta" VALUES (115,116,E'official',E'Rory Lancman');
INSERT INTO "districts_meta" VALUES (116,117,E'official',E'Ann-Margaret Carrozza');
INSERT INTO "districts_meta" VALUES (117,118,E'official',E'Nettie Mayersohn');
INSERT INTO "districts_meta" VALUES (118,119,E'official',E'Andrew Hevesi');
INSERT INTO "districts_meta" VALUES (119,120,E'official',E'William Scarborough');
INSERT INTO "districts_meta" VALUES (120,121,E'official',E'Margaret Markey');
INSERT INTO "districts_meta" VALUES (121,122,E'official',E'Michele Titus');
INSERT INTO "districts_meta" VALUES (122,123,E'official',E'Vivian Cook');
INSERT INTO "districts_meta" VALUES (123,124,E'official',E'Barbara Clark');
INSERT INTO "districts_meta" VALUES (124,125,E'official',E'Michael DenDekker');
INSERT INTO "districts_meta" VALUES (125,126,E'official',E'Jeffrion Aubry');
INSERT INTO "districts_meta" VALUES (126,127,E'official',E'Michael Gianaris');
INSERT INTO "districts_meta" VALUES (127,128,E'official',E'Catherine Nolan');
INSERT INTO "districts_meta" VALUES (128,129,E'official',E'Anthony Seminerio');
INSERT INTO "districts_meta" VALUES (129,130,E'official',E'JosÃ© Peralta');
INSERT INTO "districts_meta" VALUES (130,131,E'official',E'Inez Barron');
INSERT INTO "districts_meta" VALUES (131,132,E'official',E'Helene Weinstein');
INSERT INTO "districts_meta" VALUES (132,133,E'official',E'Rhoda Jacobs');
INSERT INTO "districts_meta" VALUES (133,134,E'official',E'Karim Camara');
INSERT INTO "districts_meta" VALUES (134,135,E'official',E'James Brennan');
INSERT INTO "districts_meta" VALUES (135,136,E'official',E'Steven Cymbrowitz');
INSERT INTO "districts_meta" VALUES (136,137,E'official',E'Alec Brook-Krasny');
INSERT INTO "districts_meta" VALUES (137,138,E'official',E'William Colton');
INSERT INTO "districts_meta" VALUES (138,139,E'official',E'Dov Hikind');
INSERT INTO "districts_meta" VALUES (139,140,E'official',E'Peter Abbate');
INSERT INTO "districts_meta" VALUES (140,141,E'official',E'Joseph Lentol');
INSERT INTO "districts_meta" VALUES (141,142,E'official',E'Felix Ortiz');
INSERT INTO "districts_meta" VALUES (142,143,E'official',E'Joan Millman');
INSERT INTO "districts_meta" VALUES (143,144,E'official',E'Vito Lopez');
INSERT INTO "districts_meta" VALUES (144,145,E'official',E'Darryl Towns');
INSERT INTO "districts_meta" VALUES (145,146,E'official',E'William Boyland');
INSERT INTO "districts_meta" VALUES (146,147,E'official',E'Annette Robinson');
INSERT INTO "districts_meta" VALUES (147,148,E'official',E'Hakeem Jeffries');
INSERT INTO "districts_meta" VALUES (148,149,E'official',E'N. Nick Perry');
INSERT INTO "districts_meta" VALUES (149,150,E'official',E'Alan Maisel');
INSERT INTO "districts_meta" VALUES (150,151,E'official',E'D. Hyer-Spencer');
INSERT INTO "districts_meta" VALUES (151,152,E'official',E'Matthew Titone');
INSERT INTO "districts_meta" VALUES (152,153,E'official',E'Louis Tobacco');
INSERT INTO "districts_meta" VALUES (153,154,E'official',E'Michael Cusick');
INSERT INTO "districts_meta" VALUES (154,155,E'official',E'Sheldon Silver');
INSERT INTO "districts_meta" VALUES (155,156,E'official',E'Micah Kellner');
INSERT INTO "districts_meta" VALUES (156,157,E'official',E'Deborah Glick');
INSERT INTO "districts_meta" VALUES (157,158,E'official',E'Linda Rosenthal');
INSERT INTO "districts_meta" VALUES (158,159,E'official',E'Adam Powell');
INSERT INTO "districts_meta" VALUES (159,160,E'official',E'Daniel O\'Donnell');
INSERT INTO "districts_meta" VALUES (160,161,E'official',E'Keith Wright');
INSERT INTO "districts_meta" VALUES (161,162,E'official',E'Herman Farrell');
INSERT INTO "districts_meta" VALUES (162,163,E'official',E'Adriano Espaillat');
INSERT INTO "districts_meta" VALUES (163,164,E'official',E'Jonathan Bing');
INSERT INTO "districts_meta" VALUES (164,165,E'official',E'Brian Kavanagh');
INSERT INTO "districts_meta" VALUES (165,166,E'official',E'Richard Gottfried');
INSERT INTO "districts_meta" VALUES (166,167,E'official',E'Peter Rivera');
INSERT INTO "districts_meta" VALUES (167,168,E'official',E'Aurelia Greene');
INSERT INTO "districts_meta" VALUES (168,169,E'official',E'Jose Rivera');
INSERT INTO "districts_meta" VALUES (169,170,E'official',E'Michael Benjamin');
INSERT INTO "districts_meta" VALUES (170,171,E'official',E'Naomi Rivera');
INSERT INTO "districts_meta" VALUES (171,172,E'official',E'Jeffrey Dinowitz');
INSERT INTO "districts_meta" VALUES (172,173,E'official',E'Michael Benedetto');
INSERT INTO "districts_meta" VALUES (173,174,E'official',E'Carl Heastie');
INSERT INTO "districts_meta" VALUES (174,175,E'official',E'Carmen Arroyo');
INSERT INTO "districts_meta" VALUES (175,176,E'official',E'Ruben Diaz');
INSERT INTO "districts_meta" VALUES (176,177,E'official',E'Nelson Castro');
INSERT INTO "districts_meta" VALUES (177,178,E'official',E'James Pretlow');
INSERT INTO "districts_meta" VALUES (178,179,E'official',E'Amy Paulin');
INSERT INTO "districts_meta" VALUES (179,180,E'official',E'Adam Bradley');
INSERT INTO "districts_meta" VALUES (180,181,E'official',E'Sandra Galef');
INSERT INTO "districts_meta" VALUES (181,182,E'official',E'George Latimer');
INSERT INTO "districts_meta" VALUES (182,183,E'official',E'Richard Brodsky');
INSERT INTO "districts_meta" VALUES (183,184,E'official',E'Mike Spano');
INSERT INTO "districts_meta" VALUES (184,185,E'official',E'Kenneth Zebrowski');
INSERT INTO "districts_meta" VALUES (185,186,E'official',E'Ellen Jaffee');
INSERT INTO "districts_meta" VALUES (186,187,E'official',E'Nancy Calhoun');
INSERT INTO "districts_meta" VALUES (187,188,E'official',E'Ann Rabbitt');
INSERT INTO "districts_meta" VALUES (188,189,E'official',E'Aileen Gunther');
INSERT INTO "districts_meta" VALUES (189,190,E'official',E'Gregory Ball');
INSERT INTO "districts_meta" VALUES (190,191,E'official',E'Frank Skartados');
INSERT INTO "districts_meta" VALUES (191,192,E'official',E'Kevin Cahill');
INSERT INTO "districts_meta" VALUES (192,193,E'official',E'Joel Miller');
INSERT INTO "districts_meta" VALUES (193,194,E'official',E'Marcus Molinaro');
INSERT INTO "districts_meta" VALUES (194,195,E'official',E'John McEneny');
INSERT INTO "districts_meta" VALUES (195,196,E'official',E'George Amedore');
INSERT INTO "districts_meta" VALUES (196,197,E'official',E'Ronald Canestrari');
INSERT INTO "districts_meta" VALUES (197,198,E'official',E'Clifford Crouch');
INSERT INTO "districts_meta" VALUES (198,199,E'official',E'Timothy Gordon');
INSERT INTO "districts_meta" VALUES (199,200,E'official',E'Robert Reilly');
INSERT INTO "districts_meta" VALUES (200,201,E'official',E'James Tedisco');
INSERT INTO "districts_meta" VALUES (201,202,E'official',E'William Magee');
INSERT INTO "districts_meta" VALUES (202,203,E'official',E'Tony Jordan');
INSERT INTO "districts_meta" VALUES (203,204,E'official',E'Teresa Sayward');
INSERT INTO "districts_meta" VALUES (204,205,E'official',E'Janet Duprey');
INSERT INTO "districts_meta" VALUES (205,206,E'official',E'David Townsend');
INSERT INTO "districts_meta" VALUES (206,207,E'official',E'RoAnn Destito');
INSERT INTO "districts_meta" VALUES (207,208,E'official',E'Marc Butler');
INSERT INTO "districts_meta" VALUES (208,209,E'official',E'Addie Russell');
INSERT INTO "districts_meta" VALUES (209,210,E'official',E'Joan Christensen');
INSERT INTO "districts_meta" VALUES (210,211,E'official',E'William Magnarelli');
INSERT INTO "districts_meta" VALUES (211,212,E'official',E'Albert Stirpe');
INSERT INTO "districts_meta" VALUES (212,213,E'official',E'Dierdre Scozzafava');
INSERT INTO "districts_meta" VALUES (213,214,E'official',E'Gary Finch');
INSERT INTO "districts_meta" VALUES (214,215,E'official',E'William Barclay');
INSERT INTO "districts_meta" VALUES (215,216,E'official',E'Barbara Lifton');
INSERT INTO "districts_meta" VALUES (216,217,E'official',E'Donna Lupardo');
INSERT INTO "districts_meta" VALUES (217,218,E'official',E'Peter Lopez');
INSERT INTO "districts_meta" VALUES (218,219,E'official',E'Robert Oaks');
INSERT INTO "districts_meta" VALUES (219,220,E'official',E'Brian Kolb');
INSERT INTO "districts_meta" VALUES (220,221,E'official',E'Joseph Errigo');
INSERT INTO "districts_meta" VALUES (221,222,E'official',E'Susan John');
INSERT INTO "districts_meta" VALUES (222,223,E'official',E'Joseph Morelle');
INSERT INTO "districts_meta" VALUES (223,224,E'official',E'David Gantt');
INSERT INTO "districts_meta" VALUES (224,225,E'official',E'Bill Reilich');
INSERT INTO "districts_meta" VALUES (225,226,E'official',E'David Koon');
INSERT INTO "districts_meta" VALUES (226,227,E'official',E'James Bacalles');
INSERT INTO "districts_meta" VALUES (227,228,E'official',E'Thomas O\'Mara');
INSERT INTO "districts_meta" VALUES (228,229,E'official',E'Francine DelMonte');
INSERT INTO "districts_meta" VALUES (229,230,E'official',E'Stephen Hawley');
INSERT INTO "districts_meta" VALUES (230,231,E'official',E'Robin Schimminger');
INSERT INTO "districts_meta" VALUES (231,232,E'official',E'Crystal Peoples');
INSERT INTO "districts_meta" VALUES (232,233,E'official',E'Jane Corwin');
INSERT INTO "districts_meta" VALUES (233,234,E'official',E'Dennis Gabryszak');
INSERT INTO "districts_meta" VALUES (234,235,E'official',E'William Hoyt');
INSERT INTO "districts_meta" VALUES (235,236,E'official',E'Mark Schroeder');
INSERT INTO "districts_meta" VALUES (236,237,E'official',E'Jack Quinn');
INSERT INTO "districts_meta" VALUES (237,238,E'official',E'Daniel Burling');
INSERT INTO "districts_meta" VALUES (238,239,E'official',E'James Hayes');
INSERT INTO "districts_meta" VALUES (239,240,E'official',E'Joe Giglio');
INSERT INTO "districts_meta" VALUES (240,241,E'official',E'William Parment');
INSERT INTO "districts_meta" VALUES (241,242,E'Official',E'Charles Schumer');
INSERT INTO "districts_meta" VALUES (242,243,E'official',E'Kirsten Gillibrand');

/*!40000 ALTER TABLE districts_meta ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
CREATE INDEX "districts_meta_district_id_idx" ON "districts_meta" USING btree ("district_id");
