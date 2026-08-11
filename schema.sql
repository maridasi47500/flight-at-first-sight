CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists airport(
        id integer primary key autoincrement,
        name text,
            city_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            phone text,
            email text,
            country_id text,
            password text,
            listener text,
            musician text,
            favorite_genre_id text,
            musicalinstrument_id text,
            artist_composer_or_band_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists musical_genre(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists artist_composer_or_band(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists photos(
        id integer primary key autoincrement,
        airport_id text,
            pic text,
            description text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists musicalinstrument(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists person(
        id integer primary key autoincrement,
        name text,
            email text,
            phone text,
            country_id text,
            musicalinstrument_id text,
            oracle text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists photoshavepeople(
        id integer primary key autoincrement,
        person_id text,
            photos_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists country(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists city(
        id integer primary key autoincrement,
        name text,
            country_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
