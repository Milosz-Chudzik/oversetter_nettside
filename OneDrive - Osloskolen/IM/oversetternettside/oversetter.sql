create database oversetter 

create table IF NOT EXISTS brukere (
    user_id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    username varchar(255) NOT NULL,
    fornavn varchar(255) NOT NULL,
    etternavn varchar(255) NOT NULL,
    telefon int(8) UNIQUE NOT NULL,
    passord varchar(255) NOT NULL
);

create table IF NOT EXISTS bestillinger (
    bestilling_id int AUTO_INCREMENT primary key NOT NULL,
    bestillingsdato datetime NOT NULL,
    user_id int NOT NULL,
    ytelse_id int NOT NULL,
    FOREIGN KEY (user_id) REFERENCES brukere(user_id),
    FOREIGN KEY (ytelse_id) REFERENCES ytelser(ytelse_id)
);

create table IF NOT EXISTS ytelser (
    ytelse_id int AUTO_INCREMENT primary key NOT NULL,
    beskrivelse text NOT NULL,
    pris varchar(255) NOT NULL
);

insert into ytelser (ytelse_id, beskrivelse, pris) values (1, 'oversettelse av bok', '200kr');