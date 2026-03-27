import csv
import shapefile
import math

# Ne pas modifier cette fonction
# On utilisera forcément la distance de haversine en m
def distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371#*1000
    return R * c  # Distance en km




if __name__ == "__main__":
    # TODO générer le README
    # Nous allons récupérer et conserver les propositions de positions de capteurs au format WGS84/EPSG2154
    propositionsEmplacements = {}
    header = True
    numCapteur = 1
    propositionsEmplacementsFilepath = "propositionsEmplacementsCapteurs.csv"
    with open(propositionsEmplacementsFilepath, "r") as propositionsEmplacementsFile:
        lines = csv.reader(propositionsEmplacementsFile, delimiter=",", lineterminator="\n")
        for line in lines:
            if (header):
                header = False
                continue
            # TODO : modifier la ligne suivante
            propositionsEmplacements[numCapteur] = [float(line[]), float(line[])]
            numCapteur += 1


    # Nous allons enregistrer les coefficients dans un shapefile de "coeficient"
    # TODO : compléter la ligne suivante
    shapefileCoefficientsMrs = shapefile.Writer("", shapefile.POLYGON)
    # TODO : créer un champ "Id" de type texte
    # TODO : créer un champ "coefficient" de type numérique, avec au moins 6 décimales

    shapefileHexaCalanques = shapefile.Reader("maillageCalanques_50M_hexa_complet", shapefile.POLYGON)
    for hexagone in shapefileHexaCalanques.iterShapeRecords():

        # On récupère le centroide de la maille
        maille = hexagone.shape
        centreX = # TODO : completer
        centreY = # TODO : completer

        coefficient = 0.0 

        # README : on donne la boucle for suivante
        # elle peut être utilisée, completée, etc.
        for capteurId, capteurPos in propositionsEmplacements.items():
            distCapteur = distance(centreY, centreX, (capteurPos[1]), capteurPos[0])

        # README : on accède aux attributs de la maille via l'objet record
        # les attributs disponibles sont l'altitude, le dénivelé, l'id de la maille, la position, etc.
        listeDesAttributsDeLaMaille = hexagone.record
        
        coefficient = # TODO : completer

        
        # On ajoute une nouvelle shape
        shapefileCoefficientsMrs.shape(maille)
        # TODO : ajouter un nouvel enregistrement avec un id de carreau et un coefficient
        shapefileCoefficientsMrs.
        
    # TODO : fermer le shapefile à la fin de la boucle for