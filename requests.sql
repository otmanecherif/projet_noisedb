-- 1- donner la liste des organisateurs par concert: 
SELECT Concert.Nom AS NomConcert, Utilisateurs.Nom, Utilisateurs.Prenom
FROM Concert
JOIN Organisateurs ON Concert.id = Organisateurs.idConcert
JOIN Utilisateurs ON Organisateurs.idOrganisateur = Utilisateurs.id
ORDER BY Concert.Nom;

-- 2-auto-jointure : donner la liste des utilisateurs qui ont le meme prenom :
SELECT DISTINCT LEAST(u1.id, u2.id) AS IdUtilisateur1, GREATEST(u1.id, u2.id) AS IdUtilisateur2, u1.Prenom AS NomUtilisateur1, u2.Prenom AS NomUtilisateur2
FROM Utilisateurs u1
JOIN Utilisateurs u2 ON u1.Prenom = u2.Prenom
WHERE u1.id <> u2.id AND u1.id < u2.id;

--3-une sous-requête corrélée: donner la liste des utilisateurs qui sont des organisateurs:
SELECT *
FROM Utilisateurs u
WHERE EXISTS (
    SELECT 1
    FROM Organisateurs o
    WHERE o.idOrganisateur = u.id
);

-- 4-une sous-requête dans le FROM : selectionner la liste des groupe qui ont un nombre de concert >= 2 
SELECT *
FROM (
  SELECT idGroupe, COUNT(*) AS nbConcerts
  FROM LineUp
  GROUP BY idGroupe
) AS subquery
WHERE nbConcerts >= 2;

-- 5- sous requete dans le where: la liste des concert ou la localisation est a paris:
SELECT *
FROM Concert
WHERE idLieu IN (
  SELECT id
  FROM Lieu
  WHERE localisation = 'paris'
);

-- 6- agregats avec groupeBy et having : la liste des prix moyens par groupe ou le prix >= 50:
SELECT G.id, G.Nom, AVG(C.Prix) AS PrixMoyen
FROM Groupe G
INNER JOIN LineUp L ON G.id = L.idGroupe
INNER JOIN Concert C ON L.idConcert = C.id
GROUP BY G.id
HAVING AVG(C.Prix) >= 50;

-- 7-agregats avec groupeBy et having : le nombre de concert organisé par association ou le nombre de concert > 1:
SELECT A.id, A.Nom, COUNT(*) AS NombreConcerts
FROM Association A
INNER JOIN Concert C ON A.id = C.idAssociation
GROUP BY A.id, A.Nom
HAVING COUNT(*) > 1;


-- 8- requête impliquant le calcul de deux agrégats: selectionner la moyenne des maximum et minimum des prix de concert par association
SELECT AVG(maximums) AS MoyenneMaximums, AVG(minimums) AS MoyenneMinimums
FROM (
  SELECT MAX(Prix) AS maximums, MIN(Prix) AS minimums
  FROM Concert
  GROUP BY idAssociation
) AS R;

-- 9-LEFT JOIN: afficher le nombre de concert par lieu
SELECT Lieu.Nom AS NomLieu, COUNT(Concert.id) AS NombreConcerts
FROM Lieu
LEFT JOIN Concert ON Lieu.id = Concert.idLieu
GROUP BY Lieu.id, Lieu.Nom;

-- 10- RIGHT JOIN: toutes les associations, avec le nom du concert associé
SELECT Association.id, Association.Nom, Concert.Nom AS ConcertNom
FROM Association
RIGHT JOIN Concert ON Association.id = Concert.idAssociation;

--11- FULL JOIN: tous les utilisateurs et leurs commentaires associés, que ce soit sur des morceaux, des groupes ou des concerts.
SELECT Utilisateurs.Nom, AvisMorceau.commentaire AS CommentaireMorceau, AvisGroupe.commentaire AS CommentaireGroupe, AvisConcert.commentaire AS CommentaireConcert
FROM Utilisateurs
FULL JOIN AvisMorceau ON Utilisateurs.id = AvisMorceau.idUtilisateur
FULL JOIN AvisGroupe ON Utilisateurs.id = AvisGroupe.idUtilisateur
FULL JOIN AvisConcert ON Utilisateurs.id = AvisConcert.idUtilisateur;

--12- selectionner le concert avec le plus de places disponibles
SELECT Concert.*
FROM Concert
WHERE Concert.placesdispo = (SELECT MAX(placesdispo) FROM Concert);

--13- le morceau qui a la meilleure note moyenne
SELECT Morceau.*, AVG(Note.note) AS MoyenneNote
FROM Morceau
JOIN Note ON Morceau.id = Note.idMorceau
GROUP BY Morceau.id
ORDER BY MoyenneNote DESC
LIMIT 1;

-- 14- les cinq morceaux ayant reçu le plus grand nombre d'avis,
SELECT Morceau.*, COUNT(AvisMorceau.idMorceau) AS NombreAvis
FROM Morceau
LEFT JOIN AvisMorceau ON Morceau.id = AvisMorceau.idMorceau
GROUP BY Morceau.id
ORDER BY NombreAvis DESC
LIMIT 5;


-- 15- une requete exprimant une condition de totalité avec des sous requêtes corrélées: recuperer les concerts qui n'ont aucune places disponibles
SELECT id
FROM Concert c
WHERE NOT EXISTS (
  SELECT *
  FROM Lieu l
  WHERE l.id = c.idLieu
    AND c.PlacesDispo > 0
);
--16- une requete exprimant une condition de totalité avec de l’agrégation:
--sélectionner uniquement les lieux qui ont au moins 2 concert associé:
SELECT Lieu.id, Lieu.Nom
FROM Lieu
JOIN Concert ON Lieu.id = Concert.idLieu
GROUP BY Lieu.id, Lieu.Nom
HAVING COUNT(Concert.id) > 1;

--Les deux requêtes qui renverraient le même résultat si les tables ne contient pas de nulls et des resultats différent sinon:
-- selectionner les lieux qui ont un concert correspondant
--17- 
SELECT Lieu.id, Lieu.Nom
FROM Lieu
INNER JOIN Concert ON Lieu.id = Concert.idLieu;

-- 18- 
SELECT Lieu.id, Lieu.Nom
FROM Lieu
LEFT JOIN Concert ON Lieu.id = Concert.idLieu;

--19- requete recursive: selectionner la liste des utilisateurs lié a l'utilisateur d'id = 1
WITH RECURSIVE SuiviHierarchy AS (
  SELECT IdUtilisateurSuit, IdUtilisateurSuivi
  FROM Suivi
  WHERE IdUtilisateurSuit = 1  
  UNION

  SELECT s.IdUtilisateurSuit, s.IdUtilisateurSuivi
  FROM Suivi s
  INNER JOIN SuiviHierarchy sh ON s.IdUtilisateurSuit = sh.IdUtilisateurSuivi
  WHERE s.IdUtilisateurSuit <> s.IdUtilisateurSuivi
)
SELECT *
FROM SuiviHierarchy;

-- 20- requete avec fenetrage: le nombre total de concerts auxquels chaque utilisateur a participé
SELECT distinct u.id, u.nom, u.prenom, COUNT(e.idConcert) OVER (PARTITION BY u.id) AS total_concerts
FROM Utilisateurs u
LEFT JOIN EvenementUtilisateur eu ON u.id = eu.idUtilisateur
LEFT JOIN Evenement e ON eu.idEvenement = e.id
GROUP BY u.id, u.nom, u.prenom, e.idConcert;