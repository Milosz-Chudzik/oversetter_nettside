create database oversetter 

create table IF NOT EXISTS brukere (
    user_id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    email varchar(255) NOT NULL unique,
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
insert into ytelser (ytelse_id, beskrivelse, pris) values (2, 'oversettelse av dokument', '100kr');
insert into ytelser (ytelse_id, beskrivelse, pris) values (3, 'oversettelse i fysisk samtale' '100kr');