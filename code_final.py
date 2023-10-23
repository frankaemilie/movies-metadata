""" Exercice noté 1
Entrée: Fichier movie_metadata2.csv
Fonctionnement
**Veuillez entrer le nom d'un acteur ou d'une actrice :** Natalie Portman
Natalie Portman a joué avec les 17 personnes suivantes :
Chris Hemsworth
Christopher Lee
Eddie Marsan
Eva Amurri Martino
Greta Gerwig
Jake Gyllenhaal
James Frain
Joseph Gordon-Levitt
Julia Roberts
Liam Neeson
Martin Short
Mila Kunis
Noah Emmerich
Norah Jones
Philip Seymour Hoffman
Scarlett Johansson
Zooey Deschanel
**Veuillez entrer le nom d'un acteur ou d'une actrice :** Nataly Portman
Nom inconnu !
Contraintes :
La lecture du fichier devra se faire avant la demande du nom de l’acteur ou de l’actrice et l’ensemble des informations
du fichier devra être stocké dans une structure de données appropriée. Aucun accès au fichier ne devra se faire
après avoir récupéré le nom de l’acteur ou de l’actrice. Le programme devra fonctionner quel que soit le nom donné par
l’utilisateur. Le programme utilisera au moins un dictionnaire et un ensemble.
Les compréhensions devront être privilégiées pour remplacer les boucles “classiques” dès que possible."""

# D'abord on lit le fichier. La première ligne du fichier sera lu pour enlever les descriptions de chaque colonne.
# La liste nommé actors est établie pour l'utiliser plus tard.
# Ensuite on stocke toutes les informations sous formes des variables.
# Pour l'exercice, il n'est nécessaire de stocker que "cast".
# Les informations concernant les acteurs seront stockés sous forme de dictionnaire.

with open('input/movie_metadata2.csv', 'r', encoding='utf8') as f:
    data = f.readline()
    actors = []
    for line in f:
        column = line.strip().split(';')
        movie = column[1]
        director = column[2]
        critic = column[3]
        cast = {column[4]: column[5]}
        info1 = column[6:9]
        lang = column[9]
        country = column[10]
        info2 = column[11:]

        actors.append(cast)   # Ajout du dictionnaire dans une liste, ensuite on demande l'utilisateur d'entrer un nom.

    name_search = input("Veuillez un nom d'un acteur ou d'une actrice : ")
    # res = []
    # for line in actors:
    #     for (k, v) in line.items():
    #         if name_search in (k, v):
    #             res.append(v) if name_search == k else res.append(k)

    list_acteurs = [v if name_search == k else k for line in actors for (k, v) in line.items() if name_search in (k, v)]

    if len(list_acteurs) == 0:
        print("Nom inconnu !")
    else:
        other_actors = set(list_acteurs)
        print(f'{name_search} a joué avec les {len(other_actors)} personnes suivantes :')
        other_actors = sorted(other_actors)
        print('\n'.join(other_actors))

"""
La boucle for (55-59) est remplacée par une liste de compréhension. Elle cherche dans les lignes du dictionnaires si le nom
entré y est et s'il s'agit de la clé ou de la valeur. Elle ajoute le correspondant, qui est l'autre acteur.
Ensuite, on vérifie si la liste est vide. Si elle est vide, le nom saisi n'existe pas dans le dictionnaire et un message
d'erreur s'affiche.
Si la liste n'est pas vide, elle est transformée en ensemble afin de supprimer les doublons.
Enfin, la longueur d'ensemble est parcouru et les acteurs s'affichent en ordre alphabétique.
Pour un affichage plus agréable, l'acteur ligne par ligne, la fonction join() est employé.  

Sources supplémentaires:
# https://www.pythonpool.com/python-iteritems/
# https://betterdatascience.com/python-if-else-one-line/
# https://www.geeksforgeeks.org/python-difference-between-sorted-and-sort/
"""
