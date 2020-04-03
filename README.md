# TER

Je télécharge dans un  premier temps la base de données open library data dumps authors.
Je stock ces données dans un fichier json.txt
J'execute mon programme "json" (la premiere ligne en commentaire) pour supprimer les différentes lignes inutiles (devant le json).
Ensuite je prend mon fichier texte que je copie dans "http://jsonviewer.stack.hu/" pour avoir une syntaxe json. 
Je stocke le json dans newjson.txt.
J'execute mon programme "json" pour ne selectionner que les informations qui m'interesse ( name, revision, etc).
Le resultat de ce programme est stocké dans json2.txt.
J'execute ensuite le programme "propresql" qui permet de rajouter des virgules et des guillements pour pouvoir les intégrer dans mysql.
Le résultat est stocké dans json3.txt.

### BDD ####

Je créé une base de donnée authors sur mysql phpmyadmin avec les valeurs de name, personal_name, last_modified et revision.
Pour cela je fais un INSERT INTO authors (name,personal_name,last_modifed,revision) values (contenu de json3.txt).
Et cela integre les données dans les bonnes colonnes correspondantes.
(juste petite optimisation ), au lieu de ); )


### Version json integrer directement

Je cree une nouvelle table avec une colonne information qui est de type json.
Ensuite je fais INSERT INTO table (information) VALUES (contenu de newjson.txt).
Et je peux ensuite accéder aux données json via cette commande (exemple de name):
SELECT information->'$.name' information
FROM table;

J'ai ajouté différentes captures d'écran pour montrer le resultat des tables de mysql.
