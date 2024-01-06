CREATE TABLE application1 (
  login varchar(128) NOT NULL DEFAULT '',
  pass varchar(32) NOT NULL DEFAULT '',
  id int(10) unsigned NOT NULL AUTO_INCREMENT,
  name varchar(128) NOT NULL DEFAULT '',
  email varchar(20) NOT NULL DEFAULT '',
  year int(254) NOT NULL DEFAULT 0,
  gender varchar(10) NOT NULL DEFAULT 'male',
  limbs int(10) NOT NULL DEFAULT 4,
  bio varchar(30) NOT NULL DEFAULT '',
  PRIMARY KEY (id)
);

  CREATE TABLE abb
  (
    ID_abb int(4) unsigned NOT NULL AUTO_INCREMENT,
    abb varchar(15) NOT NULL DEFAULT '',
    PRIMARY KEY(ID_abb)
  );
  INSERT INTO abb SET abb='Fly';
  INSERT INTO abb SET abb='Night vision';
  