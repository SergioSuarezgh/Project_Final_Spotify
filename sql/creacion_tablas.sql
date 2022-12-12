CREATE TABLE LISTA_EXITOS(
		dates DATE,
        uri VARCHAR(100),
        artist_name VARCHAR(200),
        track_name VARCHAR(200),
        sources VARCHAR (200),
        position INT,
        previous_rank INT,
        dif INT,
        peak_rank INT,
        days_on_chart INT,
        streams INT,
        CONSTRAINT dat_pk PRIMARY KEY (dates, artist_name, track_name)
        );
        
CREATE TABLE ARTIST(
		artist_name VARCHAR(200),
        style VARCHAR(200),
        CONSTRAINT art_pk PRIMARY KEY(artits_name));
        
CREATE TABLE EVENTOS(
		dates DATE,
        eventos VARCHAR(200),
        tipos VARCHAR (100),
        region VARCHAR (100),
        CONSTRAINT art_pk PRIMARY KEY(dates));
        
CREATE TABLE CLIMA(
		dates DATE,
        temp_max FLOAT,
        temp_min FLOAT,
        temp_media FLOAT,
        precipitacion FLOAT,
        CONSTRAINT art_pk PRIMARY KEY(dates));
        
CREATE TABLE MADRID(
		dates DATE,
        artist_name VARCHAR(200),
        track_name VARCHAR(200),
        position INT,
        previous_rank INT,
        peak_rank INT,
        days_on_chart INT,
        CONSTRAINT dat_pk PRIMARY KEY (dates, artist_name, track_name)
        );
        
        
CREATE TABLE MALAGA(
		dates DATE,
        artist_name VARCHAR(200),
        track_name VARCHAR(200),
        position INT,
        previous_rank INT,
        peak_rank INT,
        days_on_chart INT,
        CONSTRAINT dat_pk PRIMARY KEY (dates, artist_name, track_name)
        );
        
        
CREATE TABLE SEVILLA(
		dates DATE,
        artist_name VARCHAR(200),
        track_name VARCHAR(200),
        position INT,
        previous_rank INT,
        peak_rank INT,
        days_on_chart INT,
        CONSTRAINT dat_pk PRIMARY KEY (dates, artist_name, track_name)
        );
        
CREATE TABLE VALENCIA(
		dates DATE,
        artist_name VARCHAR(200),
        track_name VARCHAR(200),
        position INT,
        previous_rank INT,
        peak_rank INT,
        days_on_chart INT,
        CONSTRAINT dat_pk PRIMARY KEY (dates, artist_name, track_name)
        );
        
	CREATE TABLE BILBAO(
		dates DATE,
        artist_name VARCHAR(200),
        track_name VARCHAR(200),
        position INT,
        previous_rank INT,
        peak_rank INT,
        days_on_chart INT,
        CONSTRAINT dat_pk PRIMARY KEY (dates, artist_name, track_name)
        );
        
        CREATE TABLE BARCELONA(
		dates DATE,
        artist_name VARCHAR(200),
        track_name VARCHAR(200),
        position INT,
        previous_rank INT,
        peak_rank INT,
        days_on_chart INT,
        CONSTRAINT dat_pk PRIMARY KEY (dates, artist_name, track_name)
        );
        
        
        
        

        

        
        