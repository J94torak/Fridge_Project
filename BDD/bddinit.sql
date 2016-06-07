DROP DATABASE IF EXISTS bddproject;
CREATE DATABASE bddproject CHARACTER SET 'utf8';
USE bddproject;

CREATE TABLE IF NOT EXISTS Elem_connu (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    code_barres VARCHAR(40) NOT NULL UNIQUE,
    nom VARCHAR(40) NOT NULL UNIQUE,
	description TEXT,
	image_adress TEXT, 
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS Elem_frigo (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    code_barres VARCHAR(40) NOT NULL,
    date_peremp DATE,
    date_entree DATE,
    PRIMARY KEY (id),
	CONSTRAINT fk_code_barres
		FOREIGN KEY (code_barres)
		REFERENCES Elem_connu(code_barres)
)
ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS Liste_course (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    code_barres VARCHAR(40) NOT NULL,
    nb_elem SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;

#source /home/seb/Fridge_Project/BDD/bddinit.sql
