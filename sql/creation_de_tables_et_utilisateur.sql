# 3. creation de la base de donnée RNE
create DATABASE IF NOT EXISTS  RNE;
# 4.  creation de tables
create table elus(
code_insee varchar(10)
, mode_de_scrutin varchar(20)
, numliste varchar(10)
, code_nuance_de_la_liste varchar(10)
, numero_du_candidat_dans_la_liste varchar(10)
, tour varchar(10)
, nom varchar(100)
, prenom varchar(100)
, sexe varchar(1)
, Date_de_naissance datetime
, code_profession varchar(2)
, libelle_profession varchar(100)
, nationalite varchar(5)
);
create table population(
Code_insee varchar(5)
, Population_legale Int(7)
);
create table nuancier(
code varchar(4)
, libelle varchar(50)
, ordre varchar(2)
, definition varchar(500)
);
create table villes (
id varchar(5)
, departement_code varchar(10)
, code_insee varchar(10)
, zip_code varchar(20)
, name varchar(100)
);
create table categorie (
Code varchar(10)
, Nb_d_emplois int(5)
, Artisans_commerçants_chefs_d_entreprise int(5)
, Cadres_et_professions_intellectuelles_superieures int(5)
, Professions_intermedaires int(5)
, Employes int(5)
, Ouvriers int(5) 
);
create table departements(
id varchar(5)
, region_code varchar(3)
, code varchar(3)
, name varchar(100)
, nom_normalise varchar(100)
);

# 5. creation d'un nouvelle utilisateur RNE_user


create user 'RNE_user'@'localhost' identified by 'RNE_pasword';
GRANT ALL ON RNE.* TO 'RNE_user'@'localhost';


