#!/usr/bin/env python
# coding: utf-8

# In[164]:


"""1. Ecrire une fonction python r_names() qui admet pour entrer une de ces chaînes de caractères et qui retourne 
une liste de nom de colonnes"""

names_elus = "code (insee)	mode de scrutin	num liste	code (nuance de la liste)	numéro du candidat dans la liste	" 
names_elus += "tour	nom	prénom	sexe	Date de naissance	code (profession)	libellé profession	nationalité"
def r_names(names_elus):
    l1 =[]
    l2 = names_elus.replace(' ','_')
    l3 = l2.replace("'",'_')
    l4 = l3.replace('.','_')
    l5 = l4.replace('é','e')
    l6 = l5.replace('è','e')
    l7 = l6.replace(',','')
    l8 = l7.replace('(','')
    l9 = l8.replace(')','')
    l10 = l9.split('	')
    for i in l10:
        l1.append(i)
    return l1
print(r_names(names_elus))


# In[150]:


Nuanceier_plolitique = "code	libellé	ordre	définition"
def r_names(Nuancier_plolitique):
    l1 =[]
    l2 = Nuanceier_plolitique.replace(' ','_')
    l3 = l2.replace("'",'_')
    l4 = l3.replace('.','_')
    l5 = l4.replace('é','e')
    l6 = l5.replace('è','e')
    l7 = l6.replace(',','')
    l8 = l7.replace('(','')
    l9 = l8.replace(')','')
    l10 = l9.split('	')
    for i in l10:
        l1.append(i)
    return l1
print(r_names(Nuancier_plolitique))


# In[149]:


Liste_des_villes = "id	departement_code	code_insee	zip_code	name"
def r_names(Liste_des_villes):
    l1 =[]
    l2 = Liste_des_villes.replace(' ','_')
    l3 = l2.replace("'",'_')
    l4 = l3.replace('.','_')
    l5 = l4.replace('é','e')
    l6 = l5.replace('è','e')
    l7 = l6.replace(',','')
    l8 = l7.replace('(','')
    l9 = l8.replace(')','')
    l10 = l9.split('	')
    for i in l10:
        l1.append(i)
    return l1
print(r_names(Liste_des_villes))


# In[151]:


Référentiel_géographique = "Code	Nb d'emplois	Artisans, commerçants, chefs d'entreprise	"
Référentiel_géographique += "Cadres et professions intellectuelles supérieures	Professions intermédaires	"
Référentiel_géographique += "Employés	Ouvriers"

def r_names(Référentiel_géographique):
    l1 =[]
    l2 = Référentiel_géographique.replace(' ','_')
    l3 = l2.replace("'",'_')
    l4 = l3.replace('.','_')
    l5 = l4.replace('é','e')
    l6 = l5.replace('è','e')
    l7 = l6.replace(',','')
    l8 = l7.replace('(','')
    l9 = l8.replace(')','')
    l10 = l9.split('	')
    for i in l10:
        l1.append(i)
    return l1
print(r_names(Référentiel_géographique))


# In[145]:


Population_France_par_commune = "Code insée	Population légale"
def r_names(Population_France_par_commune):
    l1 =[]
    l2 = Population_France_par_commune.replace(' ','_')
    l3 = l2.replace("'",'_')
    l4 = l3.replace('.','_')
    l5 = l4.replace('é','e')
    l6 = l5.replace('è','e')
    l7 = l6.replace(',','')
    l8 = l7.replace('(','')
    l9 = l8.replace(')','')
    l10 = l9.split('	')
    for i in l10:
        l1.append(i)
    return l1
print(r_names(Population_France_par_commune))


# In[146]:


Liste_départements = "id	region_code	code	name	nom normalisé"
def r_names(Liste_départements):
    l1 =[]
    l2 = Liste_départements.replace(' ','_')
    l3 = l2.replace("'",'_')
    l4 = l3.replace('.','_')
    l5 = l4.replace('é','e')
    l6 = l5.replace('è','e')
    l7 = l6.replace(',','')
    l8 = l7.replace('(','')
    l9 = l8.replace(')','')
    l10 = l9.split('	')
    for i in l10:
        l1.append(i)
    return l1
print(r_names(Liste_départements))


# In[130]:


"""2. Ecrire une fonction python parse_dates() qui admet pour entrer la liste renvoyer par r_names() 
et qui retourne une liste contenant seulement les noms de colonnes commençant par « Date»"""
l1 = ['code_insee', 'mode_de_scrutin', 'numliste', 'code_nuance_de_la_liste', 'numero_du_candidat_dans_la_listetour', 'nom', 'prenom', 'sexe', 'Date_de_naissance', 'code_profession', 'libelle_profession', 'nationalite']
from re import findall 

def parse_dates(l1):
    l2 = ' '.join(l1)
    l3 = findall('D[a-z]*(?:[\w]*[a-z]*)',l2)
    return l3
print(parse_dates(l1))


# In[194]:


"""6. Les fichiers ayant la même structure, écrire une fonction chargement() pour alimenter la base « RNE » avec
ces fichiers. Cette fonction utilisera les fonction r_names et parses_dates(). Elle aura pour entrer la chaîne de
caractère contenant le nom des colonnes, le chemin d’accès vers le fichier et le nom de la table dans la quel écrire.
Alimenter la base avec les fichiers"""

from sqlalchemy import create_engine
import pandas as pd
from re import findall

names_elus = ['code_insee', 'mode_de_scrutin', 'numliste', 'code_nuance_de_la_liste', 'numero_du_candidat_dans_la_liste', 'tour', 'nom', 'prenom', 'sexe', 'Date_de_naissance', 'code_profession', 'libelle_profession', 'nationalite']

engine = create_engine("mysql+pymysql://RNE_user:RNE_pasword@localhost/RNE")

def chargement(link, table, names_elus):
    print("Lecture des données")
    link = '/Users/mosbahhachem/Documents/git/Evaluation/Tables/elus_mun2014.xlsx'
    df = pd.read_excel(link , skiprows=0,header=1, set='\t', names = names_elus)
    df.to_sql('elus', con = engine, if_exists='append', index = False)
    return print("fin")

chargement('/Users/mosbahhachem/Documents/git/Evaluation/Tables/elus_mun2014.xlsx', 'elus', names_elus)


# In[199]:


Nuancier_plolitique = ['code', 'libelle', 'ordre', 'definition']

engine = create_engine("mysql+pymysql://RNE_user:RNE_pasword@localhost/RNE")

def chargement(link, table, Nuanceier_plolitique):
    print("Lecture des données")
    link = '/Users/mosbahhachem/Documents/git/Evaluation/Tables/codes_nuances.xlsx'
    df = pd.read_excel(link , skiprows=0,header=1, set='\t', names = Nuancier_plolitique)
    df.to_sql('nuancier', con = engine, if_exists='append', index = False)
    return print("fin")

chargement('/Users/mosbahhachem/Documents/git/Evaluation/Tables/codes_nuances.xlsx', 'nuancier', Nuancier_plolitique)


# In[205]:


Liste_des_villes = ['id', 'departement_code', 'code_insee', 'zip_code', 'name']

engine = create_engine("mysql+pymysql://RNE_user:RNE_pasword@localhost/RNE")

def chargement(link, table, Liste_des_villes):
    print("Lecture des données")
    link = '/Users/mosbahhachem/Documents/git/Evaluation/Tables/cities.xlsx'
    df = pd.read_excel(link , skiprows=0,header=1, set='\t', names = Liste_des_villes)
    df.to_sql('villes', con = engine, if_exists='append', index = False)
    return print("fin")

chargement('/Users/mosbahhachem/Documents/git/Evaluation/Tables/cities.xlsx', 'villes', Liste_des_villes)


# In[217]:


Référentiel_géographique = ['Code', 'Nb_d_emplois', 'Artisans_commerçants_chefs_d_entreprise', 'Cadres_et_professions_intellectuelles_superieures', 'Professions_intermedaires', 'Employes', 'Ouvriers']

engine = create_engine("mysql+pymysql://RNE_user:RNE_pasword@localhost/RNE")

def chargement(link, table, Référentiel_géographique):
    print("Lecture des données")
    link = '/Users/mosbahhachem/Documents/git/Evaluation/Tables/categorie_professionelle.xlsx'
    df = pd.read_excel(link , skiprows=0,header=1, set='\t', names = Référentiel_géographique)
    df.to_sql('categorie', con = engine, if_exists='append', index = False)
    return print("fin")

chargement('/Users/mosbahhachem/Documents/git/Evaluation/Tables/categorie_professionelle.xlsx', 'categorie', Référentiel_géographique)


# In[213]:


Population_France_par_commune = ['Code_insee', 'Population_legale']

engine = create_engine("mysql+pymysql://RNE_user:RNE_pasword@localhost/RNE")

def chargement(link, table, Population_France_par_commune):
    print("Lecture des données")
    link = '/Users/mosbahhachem/Documents/git/Evaluation/Tables/population2017.xlsx'
    df = pd.read_excel(link , skiprows=0,header=1, set='\t', names = Population_France_par_commune)
    df.to_sql('population', con = engine, if_exists='append', index = False)
    return print("fin")

chargement('/Users/mosbahhachem/Documents/git/Evaluation/Tables/population2017.xlsx', 'population', Population_France_par_commune)


# In[214]:


Liste_départements = ['id', 'region_code', 'code', 'name', 'nom_normalise']

engine = create_engine("mysql+pymysql://RNE_user:RNE_pasword@localhost/RNE")

def chargement(link, table, Liste_départements):
    print("Lecture des données")
    link = '/Users/mosbahhachem/Documents/git/Evaluation/Tables/departments.xlsx'
    df = pd.read_excel(link , skiprows=0,header=1, set='\t', names = Liste_départements)
    df.to_sql('departements', con = engine, if_exists='append', index = False)
    return print("fin")

chargement('/Users/mosbahhachem/Documents/git/Evaluation/Tables/departments.xlsx', 'departements', Liste_départements)


# In[ ]:




