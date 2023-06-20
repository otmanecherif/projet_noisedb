import csv
from faker import Faker
import random
import string

fake = Faker()
# Fonction pour générer une chaîne aléatoire
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Générer des données aléatoires pour la table Utilisateurs
def generate_utilisateurs_data(num_rows):
    
    data = []
    for i in range(num_rows):
        nom = fake.last_name()
        prenom = fake.first_name()
        email = fake.email()
        mdp = generate_random_string(8)
        idLieu = random.randint(1, num_rows)
        data.append((i+1, nom, prenom, email, mdp,idLieu))
    return data

# Générer des données aléatoires pour la table Association
def generate_association_data(num_rows):

    data = []
    for i in range(num_rows):
        nom = fake.company()
        data.append((i+1, nom))
    return data
# Générer des données aléatoires pour la table Suivi
def generate_suivi_data(num_rows, max_user_id):
    data = []
    for i in range(num_rows):
        id_utilisateur_suit = i + 1
        id_utilisateur_suivi = random.randint(1, max_user_id)
        while id_utilisateur_suivi == id_utilisateur_suit:
            id_utilisateur_suivi = random.randint(1, max_user_id)
        data.append((id_utilisateur_suit, id_utilisateur_suivi))
    return data

def generate_association_utilisateur_data(num_rows, max_user_id, max_association_id):
    data = []
    for i in range(num_rows):
        id_utilisateur = random.randint(1, max_user_id)
        id_association = random.randint(1, max_association_id)
        data.append((id_utilisateur, id_association))
    return data
def generate_lieu_data(num_rows):
    data = []
    for i in range(num_rows):
        nom = fake.street_name()
        localisation = fake.city()
        data.append((i + 1, nom, localisation))
    return data
# Générer des données aléatoires pour la table Groupe
def generate_groupe_data(num_rows):
    data = []
    for i in range(num_rows):
        nom = fake.company()
        data.append((i + 1, nom))
    return data

# Générer des données aléatoires pour la table MembreGroupe
def generate_membre_groupe_data(num_rows, max_groupe_id, max_utilisateur_id):
    data = []
    for i in range(num_rows):
        id_groupe = random.randint(1, max_groupe_id)
        id_utilisateur = random.randint(1, max_utilisateur_id)
        data.append((id_groupe, id_utilisateur))
    return data

def generate_concert_data(num_rows, max_association_id):
    data = []
    for i in range(num_rows):
        nom = fake.company()
        enfants_permis = random.randint(0, 1)
        prix = random.randint(0, 100)
        places_dispo = random.randint(0, 1000)
        cause = fake.catch_phrase()
        besoin_volontaires = random.randint(0, 1)
        espaces_exterieur = random.randint(0, 1)
        id_association = random.randint(1, max_association_id)
        idLieu = random.randint(1, num_rows)
        data.append((i + 1, nom, enfants_permis, prix, places_dispo, cause, besoin_volontaires, espaces_exterieur, id_association, idLieu))
    return data

# Générer des données aléatoires pour la table Organisateurs
def generate_organisateurs_data(num_rows, max_concert_id, max_organisateur_id):
    data = []
    for i in range(num_rows):
        id_concert = random.randint(1, max_concert_id)
        id_organisateur = random.randint(1, max_organisateur_id)
        data.append((id_concert, id_organisateur))
    return data
# Générer des données aléatoires pour la table Lineup
def generate_lineup_data(num_rows, max_groupe_id, max_concert_id):
    data = []
    for i in range(num_rows):
        id_groupe = random.randint(1, max_groupe_id)
        id_concert = random.randint(1, max_concert_id)
        data.append((id_groupe, id_concert))
    return data

def generate_lieuconcert_data(num_rows, max_lieu_id, max_concert_id):
    data = []
    for i in range(num_rows):
        id_lieu = random.randint(1, max_lieu_id)
        id_concert = random.randint(1, max_concert_id)
        data.append((id_lieu, id_concert))
    return data
def generate_evenement_data(num_rows, max_concert_id):
    data = []
    for i in range(num_rows):
        id_concert = random.randint(1, max_concert_id)
        nom = fake.name()
        date = fake.date_between(start_date='-1y', end_date='+1y')
        data.append((i+1,id_concert, nom, date))
    return data
def generate_evenement_utilisateur_data(num_rows, max_evenement_id, max_utilisateur_id):
    data = []
    for i in range(num_rows):
        id_evenement = random.randint(1, max_evenement_id)
        id_utilisateur = random.randint(1, max_utilisateur_id)
        type = random.choice([0, 1])
        data.append((id_evenement, id_utilisateur, type))
    return data
def generate_archive_concert_data(num_rows, max_concert_id):
    data = []
    for i in range(num_rows):
        id_concert = i+1
        nb_participants = random.randint(0, 1000)
        data.append((id_concert, nb_participants))
    return data
def generate_ressource_data(num_rows):
    data = []
    for i in range(num_rows):
        url = fake.url()
        data.append((i+1,url))
    return data
def generate_archive_ressource_data(num_rows, max_archive_id, max_ressource_id):
    data = []
    for i in range(num_rows):
        id_archive = i+1
        id_ressource = random.randint(1, max_ressource_id)
        data.append((id_archive, id_ressource))
    return data
def generate_categorie_data(num_rows):
    data = []
    for i in range(num_rows):
        nom = fake.word()
        data.append((i+1,nom,))
    return data

# Générer des données aléatoires pour la table SousCategorie
def generate_sous_categorie_data(num_rows, max_categorie_id):
    data = []
    for i in range(num_rows):
        id_parent = random.randint(1, max_categorie_id)
        id_fils = random.randint(1, max_categorie_id)
        while id_parent == id_fils:
            id_fils = random.randint(1, max_categorie_id)
        data.append((id_parent, id_fils))
    return data
def generate_morceau_data(num_rows, max_groupe_id, max_categorie_id):
    data = []
    for i in range(num_rows):
        id_morceau = i + 1
        nom = fake.word()
        id_groupe = random.randint(1, max_groupe_id)
        id_categorie = random.randint(1, max_categorie_id)
        data.append((id_morceau, nom, id_groupe, id_categorie))
    return data

# Générer des données aléatoires pour la table PlaylistUtilisateur
def generate_playlist_utilisateur_data(num_rows, max_user_id):
    data = []
    for i in range(num_rows):
        id_playlist = i + 1
        id_owner = random.randint(1, max_user_id)
        nom = fake.word()
        data.append((id_playlist, id_owner, nom))
    return data

def generate_playlist_groupe_data(num_rows, max_user_id):
    data = []
    for i in range(num_rows):
        id_playlist = i + 1
        id_groupe = random.randint(1, max_user_id)
        nom = fake.word()
        data.append((id_playlist, id_groupe, nom))
    return data

def generate_playlist_morceau_data(num_rows, max_morceau_id, max_playlist_id):
    data = []
    for i in range(num_rows):
        id_morceau = random.randint(1, max_morceau_id)
        id_playlist = random.randint(1, max_playlist_id)
        data.append((id_morceau, id_playlist))
    return data

# Générer des données aléatoires pour la table Note
def generate_note_data(num_rows, max_morceau_id, max_user_id):
    data = []
    for i in range(num_rows):
        note = random.randint(0, 10)
        id_morceau = random.randint(1, max_morceau_id)
        id_utilisateur = random.randint(1, max_user_id)
        data.append((note, id_morceau, id_utilisateur))
    return data
def generate_avis_morceau_data(num_rows, max_morceau_id, max_user_id):
    data = []
    for i in range(num_rows):
        commentaire = fake.text(max_nb_chars=255)
        id_morceau = random.randint(1, max_morceau_id)
        id_utilisateur = random.randint(1, max_user_id)
        data.append((commentaire, id_morceau, id_utilisateur))
    return data

def generate_avis_groupe_data(num_rows, max_groupe_id, max_user_id):
    data = []
    for i in range(num_rows):
        commentaire = fake.text(max_nb_chars=255)
        id_groupe = random.randint(1, max_groupe_id)
        id_utilisateur = random.randint(1, max_user_id)
        data.append((commentaire, id_groupe, id_utilisateur))
    return data

def generate_avis_concert_data(num_rows, max_concert_id, max_user_id):
    data = []
    for i in range(num_rows):
        commentaire = fake.text(max_nb_chars=255)
        id_concert = random.randint(1, max_concert_id)
        id_utilisateur = random.randint(1, max_user_id)
        data.append((commentaire, id_concert, id_utilisateur))
    return data



def generate_tag_data(num_rows):
    data = []
    for i in range(num_rows):
        nom = fake.word()
        data.append((i+1,nom))
    return data


# Générer des données aléatoires pour la table TagPlaylist
def generate_tag_playlist_data(num_rows, max_tag_id, max_playlist_id):
    data = []
    for i in range(num_rows):
        id_tag = random.randint(1, max_tag_id)
        id_playlist = random.randint(1, max_playlist_id)
        data.append((id_tag, id_playlist))
    return data

# Générer des données aléatoires pour la table TagEvenement

def generate_tag_evenement_data(num_rows, max_tag_id, max_evenement_id):
    data = []
    for i in range(num_rows):
        id_tag = random.randint(1, max_tag_id)
        id_evenement = random.randint(1, max_evenement_id)
        data.append((id_tag, id_evenement))
    return data

# Générer des données aléatoires pour la table TagGroupe
def generate_tag_groupe_data(num_rows, max_tag_id, max_groupe_id):
    data = []
    for i in range(num_rows):
        id_tag = random.randint(1, max_tag_id)
        id_groupe = random.randint(1, max_groupe_id)
        data.append((id_tag, id_groupe))
    return data

# Générer des données aléatoires pour la table TagLieu
def generate_tag_lieu_data(num_rows, max_tag_id, max_lieu_id):
    data = []
    for i in range(num_rows):
        id_tag = random.randint(1, max_tag_id)
        id_lieu = random.randint(1, max_lieu_id)
        data.append((id_tag, id_lieu))
    return data


# Générer des données aléatoires pour la table TagCategorie
def generate_tag_categorie_data(num_rows, max_tag_id, max_categorie_id):
    data = []
    for i in range(num_rows):
        id_tag = random.randint(1, max_tag_id)
        id_categorie = random.randint(1, max_categorie_id)
        data.append((id_tag, id_categorie))
    return data

# Générer les données pour les tables avec 10 lignes
num_rows = 10
utilisateurs_data = generate_utilisateurs_data(num_rows)
association_data = generate_association_data(num_rows)
suivi_data = generate_suivi_data(num_rows, num_rows)
association_utilisateur_data = generate_association_utilisateur_data(num_rows, num_rows, num_rows)
lieu_data = generate_lieu_data(num_rows)
groupe_data = generate_groupe_data(num_rows)
membre_groupe_data = generate_membre_groupe_data(num_rows, num_rows, num_rows)
concert_data = generate_concert_data(num_rows, num_rows)
organisateurs_data = generate_organisateurs_data(num_rows, num_rows, num_rows)
lineup_data = generate_lineup_data(num_rows, num_rows, num_rows)
lieuconcert_data = generate_lieuconcert_data(num_rows, num_rows, num_rows)
evenement_data = generate_evenement_data(num_rows, num_rows)
evenement_utilisateur_data = generate_evenement_utilisateur_data(num_rows, num_rows, num_rows)
archive_concert_data = generate_archive_concert_data(num_rows, num_rows)
ressource_data = generate_ressource_data(num_rows)
archive_ressource_data = generate_archive_ressource_data(num_rows, num_rows, num_rows)
categorie_data = generate_categorie_data(num_rows)
sous_categorie_data = generate_sous_categorie_data(num_rows, num_rows)
morceau_data = generate_morceau_data(num_rows, num_rows, num_rows)
playlist_utilisateur_data = generate_playlist_utilisateur_data(num_rows, num_rows)
playlist_groupe_data = generate_playlist_groupe_data(num_rows, num_rows)
playlist_morceau_data = generate_playlist_morceau_data(num_rows, num_rows, num_rows)
note_data = generate_note_data(num_rows, num_rows, num_rows)
avis_morceau_data = generate_avis_morceau_data(num_rows, num_rows, num_rows)
avis_concert_data = generate_avis_concert_data(num_rows, num_rows, num_rows)
avis_groupe_data = generate_avis_groupe_data(num_rows, num_rows, num_rows)
tag_data = generate_tag_data(num_rows)
tag_playlist_data = generate_tag_playlist_data(num_rows, num_rows, num_rows)
tag_categorie_data = generate_tag_categorie_data(num_rows, num_rows, num_rows)
tag_evenement_data = generate_tag_evenement_data(num_rows, num_rows, num_rows)
tag_groupe_data = generate_tag_groupe_data(num_rows, num_rows, num_rows)
tag_lieu_data = generate_tag_lieu_data(num_rows, num_rows, num_rows)




# Écrire les données dans les fichiers CSV
utilisateurs_filename = 'utilisateurs.csv'
association_filename = 'association.csv'
suivi_filename = 'suivi.csv'
association_utilisateur_filename = 'association_utilisateur.csv'
lieu_filename = 'lieu.csv'
filename_groupe = 'groupe.csv'
filename_membre_groupe = 'membre_groupe.csv'
filename_concert = 'concert.csv'
filename_organisateurs = 'organisateurs.csv'
filename_lineup = 'lineup.csv'
filename_lieuconcert = 'lieuconcert.csv'
filename_evenement = 'evenement.csv'
filename_evenement_utilisateur = 'evenement_utilisateur.csv'
filename_archive_concert = 'archive_concert.csv'
filename_ressource = 'ressource.csv'
filename_archive_ressource = 'archive_ressource.csv'
filename_categorie = 'categorie.csv'
filename_sous_categorie = 'sous_categorie.csv'
filename_morceau = 'morceau.csv'
filename_groupe = 'groupe.csv'
filename_concert = 'concert.csv'
filename_playlist_utilisateur = 'playlist_utilisateur.csv'
filename_playlist_groupe = 'playlist_groupe.csv'
filename_playlist_morceau = 'playlist_morceau.csv'
filename_note = 'note.csv'
filename = 'avis_morceau.csv'
filename_avis_concert = 'avis_concert.csv'
filename_avis_groupe = 'avis_groupe.csv'
tag_filename = 'tag.csv'
tag_playlist_filename = 'tag_playlist.csv'
tag_evenement_filename = 'tag_evenement.csv'
tag_groupe_filename = 'tag_groupe.csv'
tag_lieu_filename = 'tag_lieu.csv'
tag_categorie_filename = 'tag_categorie.csv'

#Ecrire les donnes
with open(filename_lineup, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idGroupe", "idConcert"])
    writer.writerows(lineup_data)
with open(filename_organisateurs, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idConcert", "idOrganisateur"])
    writer.writerows(organisateurs_data)
with open(filename_concert, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "Nom", "EnfantsPermis", "Prix", "PlacesDispo", "Cause", "BesoinVolontaires", "EspacesExterieur", "idAssociation","idLieu"])
    writer.writerows(concert_data)
with open(lieu_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "Nom", "Localisation"])
    writer.writerows(lieu_data)
with open(association_utilisateur_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["IdUtilisateur", "IdAssociation"])
    writer.writerows(association_utilisateur_data)


with open(suivi_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["IdUtilisateurSuit", "IdUtilisateurSuivi"])
    writer.writerows(suivi_data)
with open(utilisateurs_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "Nom", "Prenom", "Email", "Mdp","idLieu"])
    writer.writerows(utilisateurs_data)

with open(association_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "Nom"])
    writer.writerows(association_data)
with open(filename_groupe, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id","Nom"])
    writer.writerows(groupe_data)
with open(filename_membre_groupe, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idGroupe", "idUtilisateur"])
    writer.writerows(membre_groupe_data)
with open(filename_lieuconcert, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idLieu", "idConcert"])
    writer.writerows(lieuconcert_data)
with open(filename_evenement, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id","IdConcert", "Nom", "date"])
    writer.writerows(evenement_data)
with open(filename_evenement_utilisateur, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idEvenement", "idUtilisateur", "type"])
    writer.writerows(evenement_utilisateur_data)
with open(filename_archive_concert, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idConcert", "nbParticipants"])
    writer.writerows(archive_concert_data)
with open(filename_ressource, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id","url"])
    writer.writerows(ressource_data)
with open(filename_archive_ressource, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idArchive", "idRessource"])
    writer.writerows(archive_ressource_data)
with open(filename_categorie, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id","nom"])
    writer.writerows(categorie_data)
with open(filename_sous_categorie, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idParent", "idFils"])
    writer.writerows(sous_categorie_data)
with open(filename_morceau, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "nom", "idGroupe", "idCategorie"])
    writer.writerows(morceau_data)
with open(filename_playlist_utilisateur, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "idOwner", "nom"])
    writer.writerows(playlist_utilisateur_data)
with open(filename_playlist_groupe, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "idgroupe", "nom"])
    writer.writerows(playlist_groupe_data)
with open(filename_playlist_morceau, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idMorceau", "idPlaylist"])
    writer.writerows(playlist_morceau_data)
with open(filename_note, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["note", "idMorceau", "idUtilisateur"])
    writer.writerows(note_data)
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["commentaire", "idMorceau", "idUtilisateur"])
    writer.writerows(avis_morceau_data)

with open(filename_avis_groupe, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["commentaire", "idGroupe", "idUtilisateur"])
    writer.writerows(avis_groupe_data)

with open(filename_avis_concert, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["commentaire", "idConcert", "idUtilisateur"])
    writer.writerows(avis_concert_data)

with open(tag_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id","nom"])
    writer.writerows(tag_data)

with open(tag_playlist_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idTag", "idPlaylist"])
    writer.writerows(tag_playlist_data)

with open(tag_lieu_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idTag", "idLieu"])
    writer.writerows(tag_lieu_data)

with open(tag_groupe_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idTag", "idGroupe"])
    writer.writerows(tag_groupe_data)

with open(tag_evenement_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idTag", "idEvenement"])
    writer.writerows(tag_evenement_data)

with open(tag_categorie_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["idTag", "idCategorie"])
    writer.writerows(tag_categorie_data)

print(f"Fichiers CSV générés avec succès.")
