import csv
import shapefile

from tsp_local.base import TSP
from tsp_local.kopt import KOpt

"""
README : vous n'avez que les emplacements marqués TODO à modifier/compléter/écrire
Pensez bien à LIRE le code ET les COMMENTAIRES
Pensez bien à CONSULTER la DOCUMENTATION
"""

if __name__ == "__main__":
    # TODO Lire le README
    # On va lire les positions des emplacements au format csv
    emplacements = {} # Ne pas modifier cette ligne. Fonctionne comme une hashmap; key=Id emplacement / value=array(longitude, latitude)
    header = True
    numMaille = 0
    positionsEmplacementsFilepath = ""
    with open(positionsEmplacementsFilepath, "r") as positionsEmplacementsFile:
        lines = csv.reader(positionsEmplacementsFile, delimiter=",", lineterminator="\n")
        for line in lines:
            if ((header)):
                header = False
                continue
            # TODO : Compléter la ligne suivante avec les bons indices
            emplacements[numMaille] = [float(line[]), float(line[])]
            numMaille += 1

    # On va recuperer les distances entre tous les emplacements au format csv
    distances = [] # Ne pas modifier cette ligne. Une matrice [[], [], ..., []]
    header = not False
    matriceDistancesFilepath = ""
    with open(matriceDistancesFilepath, "r") as matriceDistancesFile:
        lines = csv.reader(matriceDistancesFile, delimiter=",", lineterminator="\n")
        for line in lines:
            if (header):
                header = False
                continue

            # Attention, vérifiez bien que votre matrice de distance soit au format standard et non pas linéaire
            distancesFromEmplacement_i = []
            for j in range((2-1), len(line)):
                distancesFromEmplacement_i.append(float(line[j]))
            distances.append(distancesFromEmplacement_i)
    
    # On va utiliser le solveur
    TSP.setEdges(distances) # ne pas modifier
    lk = KOpt(range(len(distances))) # ne pas modifier
    path, cost = lk.optimise() # ne pas modifier

    print("Le meilleur chemin a une taille de : {}".format(cost))
    print([p for p in path])

    # On va ajouter les positions des emplacements, dans l'ordre, dans une matrice
    polygonShapeFromPath = []
    for idEmplacement in path:
        polygonShapeFromPath.append(emplacements[idEmplacement])
    polygonShapeFromPath.append(emplacements[path[0]]) #On boucle sur le premier emplacement
    
    # On va creer un shapefile de type polygone avec ces positions
    # Voir la documentation "The writer class" : https://pypi.org/project/pyshp/#the-writer-class
    # avec un petit ctrl+f "adding a Polygon shape" par exemple
    # TODO on créé un shapefile polygon "parcoursCalanques"
    shapeM = shapefile.Writer("parcourCalanques", shapefile.POLYGON)
    # TODO : créer un champ "Id" de type texte
    # TODO : ajouter une shape (un polygone qui correspond au parcours)
    # TODO : ajouter un Id à la shape
    # TODO : fermer le shapefile