-- Assume the user has already run `paster setup-app --name=whoismygov`
-- which creates the initial tables.
--  PROBLEM: migrations could suffer bit-rot as the model code evolves.
--  This whole migrations thing is a bit rickety for that reason...
--  need an approach more like that taken by "south" for django:
--  http://south.aeracode.org/
--  ... which explicitly decouples migrations from current model code.

-- CREATE TABLE elections (
-- 	id SERIAL NOT NULL, 
-- 	name VARCHAR(255) NOT NULL, 
-- 	date DATE NOT NULL, 
-- 	stagename VARCHAR(127) NOT NULL CHECK (stagename IN ('General', 'Primary', 'General Runoff', 'Primary Runoff')), 
-- 	PRIMARY KEY (id), 
-- 	CONSTRAINT election_uniqueness_constr  UNIQUE (name, date, stagename)
-- );

-- CREATE TABLE districts (
-- 	id SERIAL NOT NULL, 
-- 	state VARCHAR(255) NOT NULL, 
-- 	district_type VARCHAR(255) NOT NULL, 
-- 	level_name VARCHAR(255) NOT NULL, 
-- 	district_name VARCHAR(255) NOT NULL, 
-- 	geometry GEOMETRY, 
-- 	PRIMARY KEY (id)
-- );

-- CREATE TABLE races (
-- 	id SERIAL NOT NULL, 
-- 	election_id INTEGER NOT NULL, 
-- 	district_id INTEGER NOT NULL, 
-- 	office VARCHAR(255) NOT NULL, 
-- 	PRIMARY KEY (id), 
-- 	 FOREIGN KEY(election_id) REFERENCES elections (id), 
-- 	 FOREIGN KEY(district_id) REFERENCES districts (id)
-- );

-- CREATE TABLE people (
-- 	id SERIAL NOT NULL, 
-- 	fullname VARCHAR(255) NOT NULL, 
-- 	incumbent_office VARCHAR(255), 
-- 	incumbent_district INTEGER, 
-- 	race_id INTEGER, 
-- 	PRIMARY KEY (id), 
-- 	 FOREIGN KEY(incumbent_district) REFERENCES districts (id), 
-- 	 FOREIGN KEY(race_id) REFERENCES races (id)
-- );

-- CREATE TABLE people_meta (
-- 	id SERIAL NOT NULL, 
-- 	person_id INTEGER, 
-- 	meta_key VARCHAR(255) NOT NULL, 
-- 	meta_value TEXT NOT NULL, 
-- 	PRIMARY KEY (id), 
-- 	 FOREIGN KEY(person_id) REFERENCES people (id)
-- );

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


ALTER SEQUENCE districts_id_seq RESTART WITH 247;

-- People.


INSERT INTO "people" VALUES (1,E'Kenneth LaValle',E'official',1);
INSERT INTO "people" VALUES (2,E'John Flanagan',E'official',2);
INSERT INTO "people" VALUES (3,E'Brian Foley',E'official',3);
INSERT INTO "people" VALUES (4,E'Owen Johnson',E'official',4);
INSERT INTO "people" VALUES (5,E'Carl Marcellino',E'official',5);
INSERT INTO "people" VALUES (6,E'Kemp Hannon',E'official',6);
INSERT INTO "people" VALUES (7,E'Craig Johnson',E'official',7);
INSERT INTO "people" VALUES (8,E'Charles Fuschillo',E'official',8);
INSERT INTO "people" VALUES (9,E'Dean Skelos',E'official',9);
INSERT INTO "people" VALUES (10,E'Shirley Huntley',E'official',10);
INSERT INTO "people" VALUES (11,E'Frank Padavan',E'official',11);
INSERT INTO "people" VALUES (12,E'George Onorato',E'official',12);
INSERT INTO "people" VALUES (13,E'Hiram Monserrate',E'official',13);
INSERT INTO "people" VALUES (14,E'Malcolm Smith',E'official',14);
INSERT INTO "people" VALUES (15,E'Joseph Addabbo Jr.',E'official',15);
INSERT INTO "people" VALUES (16,E'Toby Ann Stavisky',E'official',16);
INSERT INTO "people" VALUES (17,E'Martin Dilan',E'official',17);
INSERT INTO "people" VALUES (18,E'Velmanette Montgomery',E'official',18);
INSERT INTO "people" VALUES (19,E'John Sampson',E'official',19);
INSERT INTO "people" VALUES (20,E'Eric Adams',E'official',20);
INSERT INTO "people" VALUES (21,E'Kevin Parker',E'official',21);
INSERT INTO "people" VALUES (22,E'Martin Golden',E'official',22);
INSERT INTO "people" VALUES (23,E'Diane Savino',E'official',23);
INSERT INTO "people" VALUES (24,E'Andrew Lanza',E'official',24);
INSERT INTO "people" VALUES (25,E'Daniel Squadron',E'official',25);
INSERT INTO "people" VALUES (26,E'Liz Krueger',E'official',26);
INSERT INTO "people" VALUES (27,E'Carl Kruger',E'official',27);
INSERT INTO "people" VALUES (28,E'JosÃ© Serrano',E'official',28);
INSERT INTO "people" VALUES (29,E'Thomas Duane',E'official',29);
INSERT INTO "people" VALUES (30,E'Bill Perkins',E'official',30);
INSERT INTO "people" VALUES (31,E'Eric Schneiderman',E'official',31);
INSERT INTO "people" VALUES (32,E'Ruben Diaz',E'official',32);
INSERT INTO "people" VALUES (33,E'Pedro Espada',E'official',33);
INSERT INTO "people" VALUES (34,E'Jeffrey Klein',E'official',34);
INSERT INTO "people" VALUES (35,E'Andrea Stewart-Cousins',E'official',35);
INSERT INTO "people" VALUES (36,E'Ruth Hassell-Thompson',E'official',36);
INSERT INTO "people" VALUES (37,E'Suzi Oppenheimer',E'official',37);
INSERT INTO "people" VALUES (38,E'Thomas Morahan',E'official',38);
INSERT INTO "people" VALUES (39,E'William Larkin',E'official',39);
INSERT INTO "people" VALUES (40,E'Vincent Leibell',E'official',40);
INSERT INTO "people" VALUES (41,E'Stephen Saland',E'official',41);
INSERT INTO "people" VALUES (42,E'John Bonacic',E'official',42);
INSERT INTO "people" VALUES (43,E'Roy McDonald',E'official',43);
INSERT INTO "people" VALUES (44,E'Hugh Farley',E'official',44);
INSERT INTO "people" VALUES (45,E'Elizabeth O\'C. Little',E'official',45);
-- '
INSERT INTO "people" VALUES (46,E'Neil Breslin',E'official',46);
INSERT INTO "people" VALUES (47,E'Joseph Griffo',E'official',47);
INSERT INTO "people" VALUES (48,E'Darrel Aubertine',E'official',48);
INSERT INTO "people" VALUES (49,E'David Valesky',E'official',49);
INSERT INTO "people" VALUES (50,E'John DeFrancisco',E'official',50);
INSERT INTO "people" VALUES (51,E'James Seward',E'official',51);
INSERT INTO "people" VALUES (52,E'Thomas Libous',E'official',52);
INSERT INTO "people" VALUES (53,E'George Winner',E'official',53);
INSERT INTO "people" VALUES (54,E'Michael Nozzolio',E'official',54);
INSERT INTO "people" VALUES (55,E'James Alesi',E'official',55);
INSERT INTO "people" VALUES (56,E'Joseph Robach',E'official',56);
INSERT INTO "people" VALUES (57,E'Catharine Young',E'official',57);
INSERT INTO "people" VALUES (58,E'William Stachowski',E'official',58);
INSERT INTO "people" VALUES (59,E'Dale Volker',E'official',59);
INSERT INTO "people" VALUES (60,E'Antoine Thompson',E'official',60);
INSERT INTO "people" VALUES (61,E'Michael Ranzenhofer',E'official',61);
INSERT INTO "people" VALUES (62,E'George Maziarz',E'official',62);
INSERT INTO "people" VALUES (63,E'Timothy Bishop',E'official',63);
INSERT INTO "people" VALUES (64,E'Steve Israel',E'official',64);
INSERT INTO "people" VALUES (65,E'Peter King',E'official',65);
INSERT INTO "people" VALUES (66,E'Carolyn McCarthy',E'official',66);
INSERT INTO "people" VALUES (67,E'Gary Ackerman',E'official',67);
INSERT INTO "people" VALUES (68,E'Gregory Meeks',E'official',68);
INSERT INTO "people" VALUES (69,E'Joseph Crowley',E'official',69);
INSERT INTO "people" VALUES (70,E'Jerrold Nadler',E'official',70);
INSERT INTO "people" VALUES (71,E'Anthony David Weiner',E'official',71);
INSERT INTO "people" VALUES (72,E'Edolphus Towns',E'official',72);
INSERT INTO "people" VALUES (73,E'Yvette Clarke',E'official',73);
INSERT INTO "people" VALUES (74,E'Nydia VelÃ¡zquez',E'official',74);
INSERT INTO "people" VALUES (75,E'Michael McMahon',E'official',75);
INSERT INTO "people" VALUES (76,E'Carolyn Maloney',E'official',76);
INSERT INTO "people" VALUES (77,E'Charles Rangel',E'official',77);
INSERT INTO "people" VALUES (78,E'JosÃ© Serrano',E'official',78);
INSERT INTO "people" VALUES (79,E'Eliot Engel',E'official',79);
INSERT INTO "people" VALUES (80,E'Nita Lowey',E'official',80);
INSERT INTO "people" VALUES (81,E'John Hall',E'official',81);
INSERT INTO "people" VALUES (82,E'Paul Tonko',E'official',83);
INSERT INTO "people" VALUES (83,E'Maurice Hinchey',E'official',84);
INSERT INTO "people" VALUES (84,E'John McHugh',E'official',85);
INSERT INTO "people" VALUES (85,E'Michael Arcuri',E'official',86);
INSERT INTO "people" VALUES (86,E'Daniel Maffei',E'official',87);
INSERT INTO "people" VALUES (87,E'Christopher Lee',E'official',88);
INSERT INTO "people" VALUES (88,E'Brian Higgins',E'official',89);
INSERT INTO "people" VALUES (89,E'Louise Slaughter',E'official',90);
INSERT INTO "people" VALUES (90,E'Eric Massa',E'official',91);
INSERT INTO "people" VALUES (91,E'Marc Alessi',E'official',92);
INSERT INTO "people" VALUES (92,E'Fred Thiele',E'official',93);
INSERT INTO "people" VALUES (93,E'Patricia Eddington',E'official',94);
INSERT INTO "people" VALUES (94,E'Steven Englebright',E'official',95);
INSERT INTO "people" VALUES (95,E'Ginny Fields',E'official',96);
INSERT INTO "people" VALUES (96,E'Philip Ramos',E'official',97);
INSERT INTO "people" VALUES (97,E'Michael Fitzpatrick',E'official',98);
INSERT INTO "people" VALUES (98,E'Philip Boyle',E'official',99);
INSERT INTO "people" VALUES (99,E'Andrew Raia',E'official',100);
INSERT INTO "people" VALUES (100,E'James Conte',E'official',101);
INSERT INTO "people" VALUES (101,E'Robert Sweeney',E'official',102);
INSERT INTO "people" VALUES (102,E'Joseph Saladino',E'official',103);
INSERT INTO "people" VALUES (103,E'Charles Lavine',E'official',104);
INSERT INTO "people" VALUES (104,E'Robert Barra',E'official',105);
INSERT INTO "people" VALUES (105,E'Robert Walker',E'official',106);
INSERT INTO "people" VALUES (106,E'Michelle Schimel',E'official',107);
INSERT INTO "people" VALUES (107,E'Tom McKevitt',E'official',108);
INSERT INTO "people" VALUES (108,E'Earlene Hooper',E'official',109);
INSERT INTO "people" VALUES (109,E'David McDonaugh',E'official',110);
INSERT INTO "people" VALUES (110,E'Harvey Weisenberg',E'official',111);
INSERT INTO "people" VALUES (111,E'Thomas Alfano',E'official',112);
INSERT INTO "people" VALUES (112,E'Grace Meng',E'official',113);
INSERT INTO "people" VALUES (113,E'Audrey Pheffer',E'official',114);
INSERT INTO "people" VALUES (114,E'Mark Weprin',E'official',115);
INSERT INTO "people" VALUES (115,E'Rory Lancman',E'official',116);
INSERT INTO "people" VALUES (116,E'Ann-Margaret Carrozza',E'official',117);
INSERT INTO "people" VALUES (117,E'Nettie Mayersohn',E'official',118);
INSERT INTO "people" VALUES (118,E'Andrew Hevesi',E'official',119);
INSERT INTO "people" VALUES (119,E'William Scarborough',E'official',120);
INSERT INTO "people" VALUES (120,E'Margaret Markey',E'official',121);
INSERT INTO "people" VALUES (121,E'Michele Titus',E'official',122);
INSERT INTO "people" VALUES (122,E'Vivian Cook',E'official',123);
INSERT INTO "people" VALUES (123,E'Barbara Clark',E'official',124);
INSERT INTO "people" VALUES (124,E'Michael DenDekker',E'official',125);
INSERT INTO "people" VALUES (125,E'Jeffrion Aubry',E'official',126);
INSERT INTO "people" VALUES (126,E'Michael Gianaris',E'official',127);
INSERT INTO "people" VALUES (127,E'Catherine Nolan',E'official',128);
INSERT INTO "people" VALUES (128,E'Anthony Seminerio',E'official',129);
INSERT INTO "people" VALUES (129,E'JosÃ© Peralta',E'official',130);
INSERT INTO "people" VALUES (130,E'Inez Barron',E'official',131);
INSERT INTO "people" VALUES (131,E'Helene Weinstein',E'official',132);
INSERT INTO "people" VALUES (132,E'Rhoda Jacobs',E'official',133);
INSERT INTO "people" VALUES (133,E'Karim Camara',E'official',134);
INSERT INTO "people" VALUES (134,E'James Brennan',E'official',135);
INSERT INTO "people" VALUES (135,E'Steven Cymbrowitz',E'official',136);
INSERT INTO "people" VALUES (136,E'Alec Brook-Krasny',E'official',137);
INSERT INTO "people" VALUES (137,E'William Colton',E'official',138);
INSERT INTO "people" VALUES (138,E'Dov Hikind',E'official',139);
INSERT INTO "people" VALUES (139,E'Peter Abbate',E'official',140);
INSERT INTO "people" VALUES (140,E'Joseph Lentol',E'official',141);
INSERT INTO "people" VALUES (141,E'Felix Ortiz',E'official',142);
INSERT INTO "people" VALUES (142,E'Joan Millman',E'official',143);
INSERT INTO "people" VALUES (143,E'Vito Lopez',E'official',144);
INSERT INTO "people" VALUES (144,E'Darryl Towns',E'official',145);
INSERT INTO "people" VALUES (145,E'William Boyland',E'official',146);
INSERT INTO "people" VALUES (146,E'Annette Robinson',E'official',147);
INSERT INTO "people" VALUES (147,E'Hakeem Jeffries',E'official',148);
INSERT INTO "people" VALUES (148,E'N. Nick Perry',E'official',149);
INSERT INTO "people" VALUES (149,E'Alan Maisel',E'official',150);
INSERT INTO "people" VALUES (150,E'D. Hyer-Spencer',E'official',151);
INSERT INTO "people" VALUES (151,E'Matthew Titone',E'official',152);
INSERT INTO "people" VALUES (152,E'Louis Tobacco',E'official',153);
INSERT INTO "people" VALUES (153,E'Michael Cusick',E'official',154);
INSERT INTO "people" VALUES (154,E'Sheldon Silver',E'official',155);
INSERT INTO "people" VALUES (155,E'Micah Kellner',E'official',156);
INSERT INTO "people" VALUES (156,E'Deborah Glick',E'official',157);
INSERT INTO "people" VALUES (157,E'Linda Rosenthal',E'official',158);
INSERT INTO "people" VALUES (158,E'Adam Powell',E'official',159);
INSERT INTO "people" VALUES (159,E'Daniel O\'Donnell',E'official',160);
-- '
INSERT INTO "people" VALUES (160,E'Keith Wright',E'official',161);
INSERT INTO "people" VALUES (161,E'Herman Farrell',E'official',162);
INSERT INTO "people" VALUES (162,E'Adriano Espaillat',E'official',163);
INSERT INTO "people" VALUES (163,E'Jonathan Bing',E'official',164);
INSERT INTO "people" VALUES (164,E'Brian Kavanagh',E'official',165);
INSERT INTO "people" VALUES (165,E'Richard Gottfried',E'official',166);
INSERT INTO "people" VALUES (166,E'Peter Rivera',E'official',167);
INSERT INTO "people" VALUES (167,E'Aurelia Greene',E'official',168);
INSERT INTO "people" VALUES (168,E'Jose Rivera',E'official',169);
INSERT INTO "people" VALUES (169,E'Michael Benjamin',E'official',170);
INSERT INTO "people" VALUES (170,E'Naomi Rivera',E'official',171);
INSERT INTO "people" VALUES (171,E'Jeffrey Dinowitz',E'official',172);
INSERT INTO "people" VALUES (172,E'Michael Benedetto',E'official',173);
INSERT INTO "people" VALUES (173,E'Carl Heastie',E'official',174);
INSERT INTO "people" VALUES (174,E'Carmen Arroyo',E'official',175);
INSERT INTO "people" VALUES (175,E'Ruben Diaz',E'official',176);
INSERT INTO "people" VALUES (176,E'Nelson Castro',E'official',177);
INSERT INTO "people" VALUES (177,E'James Pretlow',E'official',178);
INSERT INTO "people" VALUES (178,E'Amy Paulin',E'official',179);
INSERT INTO "people" VALUES (179,E'Adam Bradley',E'official',180);
INSERT INTO "people" VALUES (180,E'Sandra Galef',E'official',181);
INSERT INTO "people" VALUES (181,E'George Latimer',E'official',182);
INSERT INTO "people" VALUES (182,E'Richard Brodsky',E'official',183);
INSERT INTO "people" VALUES (183,E'Mike Spano',E'official',184);
INSERT INTO "people" VALUES (184,E'Kenneth Zebrowski',E'official',185);
INSERT INTO "people" VALUES (185,E'Ellen Jaffee',E'official',186);
INSERT INTO "people" VALUES (186,E'Nancy Calhoun',E'official',187);
INSERT INTO "people" VALUES (187,E'Ann Rabbitt',E'official',188);
INSERT INTO "people" VALUES (188,E'Aileen Gunther',E'official',189);
INSERT INTO "people" VALUES (189,E'Gregory Ball',E'official',190);
INSERT INTO "people" VALUES (190,E'Frank Skartados',E'official',191);
INSERT INTO "people" VALUES (191,E'Kevin Cahill',E'official',192);
INSERT INTO "people" VALUES (192,E'Joel Miller',E'official',193);
INSERT INTO "people" VALUES (193,E'Marcus Molinaro',E'official',194);
INSERT INTO "people" VALUES (194,E'John McEneny',E'official',195);
INSERT INTO "people" VALUES (195,E'George Amedore',E'official',196);
INSERT INTO "people" VALUES (196,E'Ronald Canestrari',E'official',197);
INSERT INTO "people" VALUES (197,E'Clifford Crouch',E'official',198);
INSERT INTO "people" VALUES (198,E'Timothy Gordon',E'official',199);
INSERT INTO "people" VALUES (199,E'Robert Reilly',E'official',200);
INSERT INTO "people" VALUES (200,E'James Tedisco',E'official',201);
INSERT INTO "people" VALUES (201,E'William Magee',E'official',202);
INSERT INTO "people" VALUES (202,E'Tony Jordan',E'official',203);
INSERT INTO "people" VALUES (203,E'Teresa Sayward',E'official',204);
INSERT INTO "people" VALUES (204,E'Janet Duprey',E'official',205);
INSERT INTO "people" VALUES (205,E'David Townsend',E'official',206);
INSERT INTO "people" VALUES (206,E'RoAnn Destito',E'official',207);
INSERT INTO "people" VALUES (207,E'Marc Butler',E'official',208);
INSERT INTO "people" VALUES (208,E'Addie Russell',E'official',209);
INSERT INTO "people" VALUES (209,E'Joan Christensen',E'official',210);
INSERT INTO "people" VALUES (210,E'William Magnarelli',E'official',211);
INSERT INTO "people" VALUES (211,E'Albert Stirpe',E'official',212);
INSERT INTO "people" VALUES (212,E'Dierdre Scozzafava',E'official',213);
INSERT INTO "people" VALUES (213,E'Gary Finch',E'official',214);
INSERT INTO "people" VALUES (214,E'William Barclay',E'official',215);
INSERT INTO "people" VALUES (215,E'Barbara Lifton',E'official',216);
INSERT INTO "people" VALUES (216,E'Donna Lupardo',E'official',217);
INSERT INTO "people" VALUES (217,E'Peter Lopez',E'official',218);
INSERT INTO "people" VALUES (218,E'Robert Oaks',E'official',219);
INSERT INTO "people" VALUES (219,E'Brian Kolb',E'official',220);
INSERT INTO "people" VALUES (220,E'Joseph Errigo',E'official',221);
INSERT INTO "people" VALUES (221,E'Susan John',E'official',222);
INSERT INTO "people" VALUES (222,E'Joseph Morelle',E'official',223);
INSERT INTO "people" VALUES (223,E'David Gantt',E'official',224);
INSERT INTO "people" VALUES (224,E'Bill Reilich',E'official',225);
INSERT INTO "people" VALUES (225,E'David Koon',E'official',226);
INSERT INTO "people" VALUES (226,E'James Bacalles',E'official',227);
INSERT INTO "people" VALUES (227,E'Thomas O\'Mara',E'official',228);
-- '
INSERT INTO "people" VALUES (228,E'Francine DelMonte',E'official',229);
INSERT INTO "people" VALUES (229,E'Stephen Hawley',E'official',230);
INSERT INTO "people" VALUES (230,E'Robin Schimminger',E'official',231);
INSERT INTO "people" VALUES (231,E'Crystal Peoples',E'official',232);
INSERT INTO "people" VALUES (232,E'Jane Corwin',E'official',233);
INSERT INTO "people" VALUES (233,E'Dennis Gabryszak',E'official',234);
INSERT INTO "people" VALUES (234,E'William Hoyt',E'official',235);
INSERT INTO "people" VALUES (235,E'Mark Schroeder',E'official',236);
INSERT INTO "people" VALUES (236,E'Jack Quinn',E'official',237);
INSERT INTO "people" VALUES (237,E'Daniel Burling',E'official',238);
INSERT INTO "people" VALUES (238,E'James Hayes',E'official',239);
INSERT INTO "people" VALUES (239,E'Joe Giglio',E'official',240);
INSERT INTO "people" VALUES (240,E'William Parment',E'official',241);
INSERT INTO "people" VALUES (241,E'Charles Schumer',E'Official',242);
INSERT INTO "people" VALUES (242,E'Kirsten Gillibrand',E'official',243);

-- Having manually specified ids, we need to update the autoincr id sequence,
-- argh.

ALTER SEQUENCE people_id_seq RESTART WITH 243;

-- hand-written stuff to get the right incumbent info in.

UPDATE people SET incumbent_office = (
  SELECT districts.district_type FROM districts 
    WHERE districts.id = people.incumbent_district);
