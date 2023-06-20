CREATE TABLE Lieu (
  id SERIAL PRIMARY KEY, 
  Nom varchar(120),
  localisation varchar(120)
);
CREATE TABLE Utilisateurs (
  id SERIAL PRIMARY KEY, 
  Nom varchar(120),
  prenom varchar(120),
  email varchar(120),
  mdp varchar(120),
  idLieu INT,
  CONSTRAINT fk_lieu FOREIGN KEY (idLieu) REFERENCES Lieu(id)
);

CREATE TABLE Suivi (
  IdUtilisateurSuit INT,
  IdUtilisateurSuivi INT,
  CONSTRAINT pk_suivi PRIMARY KEY (IdUtilisateurSuit, IdUtilisateurSuivi),
  CONSTRAINT fk_suit FOREIGN KEY (IdUtilisateurSuit) REFERENCES Utilisateurs (id),
  CONSTRAINT fk_suivi FOREIGN KEY (IdUtilisateurSuivi) REFERENCES Utilisateurs (id),
  CONSTRAINT check_suivi_different_users CHECK (IdUtilisateurSuit <> IdUtilisateurSuivi)
);

CREATE TABLE Association (
  id SERIAL PRIMARY KEY, 
  Nom varchar(120)
);

CREATE TABLE AssociationUtilisateur (
  IdUtilisateur INT,
  IdAssociation INT,
  CONSTRAINT pk_associationutilisateur PRIMARY KEY (IdUtilisateur, IdAssociation),
  CONSTRAINT fk_utilisateur FOREIGN KEY (IdUtilisateur) REFERENCES Utilisateurs (id),
  CONSTRAINT fk_association FOREIGN KEY (IdAssociation) REFERENCES Association (id)
);



CREATE TABLE Groupe (
  id SERIAL PRIMARY KEY, 
  Nom varchar(120)
);

CREATE TABLE MembreGroupe (
 idGroupe INT,
 idUtilisateur INT,
 CONSTRAINT pk_membregroupe PRIMARY KEY (idGroupe, idUtilisateur),
 CONSTRAINT fk_groupe FOREIGN KEY (idGroupe) REFERENCES Groupe (id),
 CONSTRAINT fk_utilisateur FOREIGN KEY (idUtilisateur) REFERENCES Utilisateurs (id)
);

CREATE TABLE Concert (
  id SERIAL PRIMARY KEY, 
  Nom varchar(120),
  EnfantsPermis INT,
  Prix Int CHECK (Prix >= 0),
  PlacesDispo INT CHECK (PlacesDispo >= 0),
  Cause varchar(120),
  BesoinVolontaires INT,
  EspacesExterieur INT,
  idAssociation INT,
  idLieu INT,
  CONSTRAINT fk_lieu FOREIGN KEY (idLieu) REFERENCES Lieu(id),
  CONSTRAINT fk_association FOREIGN KEY (idAssociation) REFERENCES Association (id)
);

CREATE TABLE Organisateurs (
 idConcert INT,
 idOrganisateur INT,
 CONSTRAINT pk_organisateurs PRIMARY KEY (idConcert, idOrganisateur),
 CONSTRAINT fk_concert FOREIGN KEY (idConcert) REFERENCES Concert (id),
 CONSTRAINT fk_organisateur FOREIGN KEY (idOrganisateur) REFERENCES Utilisateurs (id)
);

CREATE TABLE LineUp (
  idGroupe INT, 
  idConcert INT,
  CONSTRAINT pk_lineup PRIMARY KEY (idGroupe, idConcert),
  CONSTRAINT fk_groupe FOREIGN KEY (idGroupe) REFERENCES Groupe (id),
  CONSTRAINT fk_concert FOREIGN KEY (idConcert) REFERENCES Concert (id)
);


CREATE TABLE Evenement (
 id SERIAL PRIMARY KEY, 
 IdConcert INT,
 Nom varchar(255),
 date Date,
 CONSTRAINT fk_concert FOREIGN KEY (IdConcert) REFERENCES Concert (id)
);

CREATE TABLE EvenementUtilisateur (
 idEvenement INT,
 idUtilisateur INT,
 type SMALLINT,
 CONSTRAINT pk_evenementutilisateur PRIMARY KEY (idEvenement, idUtilisateur),
 CONSTRAINT fk_evenement FOREIGN KEY (idEvenement) REFERENCES Evenement (id),
 CONSTRAINT fk_utilisateur FOREIGN KEY (idUtilisateur) REFERENCES Utilisateurs (id),
 CHECK (type IN (0, 1))
);

CREATE TABLE ArchiveConcert (
 idConcert INT,
 nbParticipants INT,
 CONSTRAINT pk_archiveconcert PRIMARY KEY (idConcert),
CONSTRAINT fk_concert FOREIGN KEY (idConcert) REFERENCES Concert (id)
);

CREATE TABLE Ressource (
id SERIAL PRIMARY KEY,
url varchar(255)
);

CREATE TABLE ArchiveRessource (
idArchive INT,
idRessource INT,
CONSTRAINT pk_archiveressource PRIMARY KEY (idArchive, idRessource),
CONSTRAINT fk_archiveconcert FOREIGN KEY (idArchive) REFERENCES ArchiveConcert (idConcert),
CONSTRAINT fk_ressource FOREIGN KEY (idRessource) REFERENCES Ressource (id)
);

CREATE TABLE Categorie (
id SERIAL PRIMARY KEY,
nom varchar(120)
);

CREATE TABLE SousCategorie (
idParent INT,
idFils INT,
CONSTRAINT pk_souscategorie PRIMARY KEY (idParent, idFils),
CONSTRAINT fk_categorie FOREIGN KEY (idParent) REFERENCES Categorie (id),
CONSTRAINT fk_souscategorie FOREIGN KEY (idFils) REFERENCES Categorie (id),
CONSTRAINT check_suivi_different_categories CHECK (idParent <> idFils)
);

CREATE TABLE Morceau (
id SERIAL PRIMARY KEY,
nom varchar(255),
idGroupe INT,
idCategorie INT,
CONSTRAINT fk_categorie FOREIGN KEY (idCategorie) REFERENCES Categorie (id),
CONSTRAINT fk_groupe FOREIGN KEY (idGroupe) REFERENCES Groupe (id)
);

CREATE TABLE PlaylistUtilisateur (
id SERIAL PRIMARY KEY,
idOwner INT,
nom varchar(255),
CONSTRAINT fk_utilisateur FOREIGN KEY (idUtilisateur) REFERENCES Utilisateurs (id)
);
CREATE TABLE PlaylistGroupe (
id SERIAL PRIMARY KEY,
idGroupe INT,
nom varchar(255),
CONSTRAINT fk_groupe FOREIGN KEY (idGroupe) REFERENCES Groupe (id)
);

CREATE TABLE PlaylistMorceau (
idMorceau INT,
idPlaylist INT,
CONSTRAINT pk_playlistmorceau PRIMARY KEY (idMorceau, idPlaylist),
CONSTRAINT fk_morceau FOREIGN KEY (idMorceau) REFERENCES Morceau (id),
CONSTRAINT fk_playlist FOREIGN KEY (idPlaylist) REFERENCES PlaylistUtilisateur (id)
);

CREATE TABLE Note (
note INT CHECK (Note >= 0 AND Note < 11),
idMorceau INT,
idUtilisateur INT,
CONSTRAINT pk_note PRIMARY KEY (idMorceau, idUtilisateur),
CONSTRAINT fk_morceau FOREIGN KEY (idMorceau) REFERENCES Morceau (id),
CONSTRAINT fk_utilisateur FOREIGN KEY (idUtilisateur) REFERENCES Utilisateurs (id)
);

CREATE TABLE AvisMorceau (
commentaire varchar(255),
idMorceau INT,
idUtilisateur INT,
CONSTRAINT pk_avismorceau PRIMARY KEY (idMorceau, idUtilisateur),
CONSTRAINT fk_morceau FOREIGN KEY (idMorceau) REFERENCES Morceau (id),
CONSTRAINT fk_utilisateur FOREIGN KEY (idUtilisateur) REFERENCES Utilisateurs (id)
);

CREATE TABLE AvisGroupe (
commentaire varchar(255),
idGroupe INT,
idUtilisateur INT,
CONSTRAINT pk_avisgroupe PRIMARY KEY (idGroupe, idUtilisateur),
CONSTRAINT fk_groupe FOREIGN KEY (idGroupe) REFERENCES Groupe (id),
CONSTRAINT fk_utilisateur FOREIGN KEY (idUtilisateur) REFERENCES Utilisateurs (id)
);

CREATE TABLE AvisConcert (
commentaire varchar(255),
idConcert INT,
idUtilisateur INT,
CONSTRAINT pk_avisconcert PRIMARY KEY (idConcert, idUtilisateur),
CONSTRAINT fk_concert FOREIGN KEY (idConcert) REFERENCES Concert (id),
CONSTRAINT fk_utilisateur FOREIGN KEY (idUtilisateur) REFERENCES Utilisateurs (id)
);

CREATE TABLE Tag (
id SERIAL PRIMARY KEY,
nom varchar(120)
);

CREATE TABLE TagPlaylist (
idTag INT,
idPlaylist INT,
CONSTRAINT pk_tagplaylist PRIMARY KEY (idTag, idPlaylist),
CONSTRAINT fk_tag FOREIGN KEY (idTag) REFERENCES Tag (id),
CONSTRAINT fk_playlist FOREIGN KEY (idPlaylist) REFERENCES PlaylistUtilisateur (id)
);

CREATE TABLE TagLieu (
idTag INT,
idLieu INT,
CONSTRAINT pk_taglieu PRIMARY KEY (idTag, idLieu),
CONSTRAINT fk_tag FOREIGN KEY (idTag) REFERENCES Tag (id),
CONSTRAINT fk_lieu FOREIGN KEY (idLieu) REFERENCES Lieu (id)
);

CREATE TABLE TagEvenement (
idTag INT,
idEvenement INT,
CONSTRAINT pk_tagevenement PRIMARY KEY (idTag, idEvenement),
CONSTRAINT fk_tag FOREIGN KEY (idTag) REFERENCES Tag (id),
CONSTRAINT fk_evenement FOREIGN KEY (idEvenement) REFERENCES Evenement (id)
);

CREATE TABLE TagGroupe (
idTag INT,
idGroupe INT,
CONSTRAINT pk_taggroupe PRIMARY KEY (idTag, idGroupe),
CONSTRAINT fk_tag FOREIGN KEY (idTag) REFERENCES Tag (id),
CONSTRAINT fk_groupe FOREIGN KEY (idGroupe) REFERENCES Groupe (id)
);


CREATE TABLE TagCategorie (
  idTag INT,
  idCategorie INT,
  CONSTRAINT pk_tagcategorie PRIMARY KEY (idTag, idCategorie),
  CONSTRAINT fk_tag FOREIGN KEY (idTag) REFERENCES Tag (id),
  CONSTRAINT fk_categorie FOREIGN KEY (idCategorie) REFERENCES Categorie (id)
);