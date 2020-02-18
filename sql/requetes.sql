use RNE;

# 8. Quel sont les parties politiques qui dans leur libellé comporte le terme « Union »

SELECT LIBELLE
, DEFINITION FROM NUANCIER
WHERE LIBELLE LIKE "%Union%";

# 9. Quels élus du département du « var » sont nais entre le mois de juin et aout

SELECT NOM, DATE_DE_NAISSANCE, NOM_NORMALISE FROM DEPARTEMENTS D
JOIN VILLES V ON D.CODE = V.DEPARTEMENT_CODE
JOIN ELUS E ON E.CODE_INSEE = V.CODE_INSEE
WHERE D.NAME LIKE "VAR" AND DATE_DE_NAISSANCE BETWEEN '1900-06-01' AND '2019-08-31';

# 10. Quel est l’âge moyen des élus homme au 01/01/2014 ? Celui des élus femme

SELECT Date_de_naissance
, SEXE
, NOM
, AVG(timestampdiff(YEAR, Date_de_naissance, "2014-01-01")) AS MOYENNE
 FROM ELUS
 GROUP BY NOM, SEXE, DATE_DE_NAISSANCE
 ORDER BY SEXE; 

# 11. Afficher la population totale du département des « Bouches-du-Rhône »

SELECT nom_normalise AS NOM_DEPARTEMENT, SUM(POPULATION_LEGALE) TOTALE_POPULATION
FROM POPULATION P
JOIN ELUS E ON E.CODE_INSEE = P.CODE_INSEE
JOIN VILLES V ON E.CODE_INSEE = V.CODE_INSEE
JOIN DEPARTEMENTS D ON D.CODE = V.DEPARTEMENT_CODE
WHERE D.NAME LIKE "BOUCHES_DU_RHÔNE"
GROUP BY nom_normalise;

# 12. Quel sont les 10 départements comptant le plus d’ouvriers

SELECT  Ouvriers
, NOM_NORMALISE
FROM DEPARTEMENTS D 
JOIN VILLES V ON D.CODE = V.departement_code
JOIN CATEGORIE C ON V.CODE_INSEE = C.CODE
GROUP BY NOM_NORMALISE, Ouvriers
ORDER BY  Ouvriers DESC LIMIT 10;

# 13. Afficher le nombre d’élus regrouper par nuance politique et par département

SELECT LIBELLE
, NOM_NORMALISE  
, COUNT(NOM)
FROM NUANCIER N
JOIN ELUS E ON N.CODE = E.CODE_NUANCE_DE_LA_LISTE
JOIN VILLES V ON E.CODE_INSEE = V.CODE_INSEE
JOIN DEPARTEMENTS D ON V.DEPARTEMENT_CODE = D.CODE
GROUP BY LIBELLE, NOM_NORMALISE
ORDER BY LIBELLE ;

# 14. Afficher le nombre d’élus regroupé par nuance politique et par villes pour le département des « Bouches-du-Rhône »

SELECT LIBELLE
, V.name
, COUNT(NOM) NOM
FROM NUANCIER N
JOIN ELUS E ON N.CODE = E.CODE_NUANCE_DE_LA_LISTE
JOIN VILLES V ON E.CODE_INSEE = V.CODE_INSEE
JOIN DEPARTEMENTS D ON V.DEPARTEMENT_CODE = D.CODE
WHERE V.DEPARTEMENT_CODE LIKE "13"
GROUP BY LIBELLE, V.name
ORDER BY LIBELLE ;

# 15. Afficher les 10 départements dans lesquelles il y a le plus d’élus femme, ainsi que le nombre d’élus femme correspondant

SELECT V.NAME
, SEXE
, COUNT(NOM) NOM
FROM ELUS E
JOIN VILLES V ON E.CODE_INSEE = V.CODE_INSEE
JOIN DEPARTEMENTS D ON V.DEPARTEMENT_CODE = D.CODE
WHERE SEXE LIKE "F"
GROUP BY SEXE,V.NAME
ORDER BY NOM DESC LIMIT 10;

# 16. Donner l’âge moyen des élus par départements au 01/01/2014. Les afficher par ordre décroissant

SELECT V.NAME
, AVG(timestampdiff(YEAR, Date_de_naissance, "2014-01-01")) AS AGE_MOYEN
FROM ELUS E
JOIN VILLES V ON E.CODE_INSEE = V.CODE_INSEE
JOIN DEPARTEMENTS D ON V.DEPARTEMENT_CODE = D.CODE
GROUP BY V.NAME
ORDER BY AGE_MOYEN DESC;

# 17. Afficher les départements où l’âge moyen des élus est strictement inférieur à 54 ans.

SELECT V.NAME
, AVG(timestampdiff(YEAR, Date_de_naissance, "2014-01-01")) AS AGE_MOYEN
FROM ELUS E
JOIN VILLES V ON E.CODE_INSEE = V.CODE_INSEE
JOIN DEPARTEMENTS D ON V.DEPARTEMENT_CODE = D.CODE
GROUP BY V.NAME  
HAVING AGE_MOYEN < 54
ORDER BY AGE_MOYEN 
;