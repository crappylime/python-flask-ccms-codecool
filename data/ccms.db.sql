BEGIN TRANSACTION;
CREATE TABLE "users" (
	`user_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`mail`	TEXT,
	`password`	CHAR(20) NOT NULL,
	`role`	TEXT NOT NULL
);
CREATE TABLE "teams" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT
);
CREATE TABLE "submissions" (
	`submission_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`assignment_id`	INTEGER NOT NULL,
	`user_id`	INTEGER NOT NULL,
	`content`	INTEGER NOT NULL,
	`date`	REAL NOT NULL,
	`points`	INTEGER
);
CREATE TABLE "members" (
	`team_id`	INTEGER,
	`Field2`	INTEGER
);
CREATE TABLE "attendances" (
	`attendance_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`user_id`	INTEGER NOT NULL,
	`date`	REAL NOT NULL,
	`status`	TEXT NOT NULL
);
CREATE TABLE "assignments" (
	`assignment_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`title`	TEXT NOT NULL,
	`content`	TEXT NOT NULL,
	`due_date`	REAL NOT NULL,
	`max_points`	INTEGER NOT NULL
);
COMMIT;
