/**
    Author: Cloyd Van S. Secuya
    Date of Creation: July 12, 2022
    Description:
        A script for creating a schema for the Jester's Tavern Database. 
        MySQL is the RDBMS used for this project, and it is where important core files will be stored. 
        The database will be used for user authentication as well.
        Like in the following: 
            TABLE: jester_music
                1. music_ID
                3. music_title
                4. music_artist
                4. music_album
                5. music_path_to_DIR
            
            TABLE: jester_users
                1. ID_auth
                2. f_name
                3. l_name
                4. userName
                5. user_pwd
*/

-- Start creating a MySQL Database named Simple_db
CREATE Database Jester_DB; 

/**
    @NOTE: 
        We want to populate the database for initialization purposes with 
            1. at least 5 musics 
            2. at least 1 user for ADMIN role ?
        Okay, we do this just to make sure that the database is filled in!!! 
*/

-- Tables

CREATE TABLE Jester_DB.jester_users 
(
    ID_auth             VARCHAR(50)     NOT NULL,
    f_name              VARCHAR(50)     NOT NULL,
    l_name              VARCHAR(50)     NOT NULL,
    userName            VARCHAR(30)     NOT NULL,
    user_pwd            VARCHAR(60)     NOT NULL
);

CREATE TABLE Jester_DB.jester_music
(
    music_ID            VARCHAR(50)     NOT NULL, 
    music_title         VARCHAR(150)    NOT NULL, 
    music_artist        VARCHAR(150)    NOT NULL,
    music_album         VARCHAR(150)    NOT NULL,
    music_path_to_DIR   VARCHAR(150)    NOT NULL, 
    lyric_path_to_DIR   VARCHAR(150)    NOT NULL 
);