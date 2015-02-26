#On importe
import json
from Equipement import Equipement

#On ouvre le fichier json
jsonfile = open('json/equipement.json')
data = json.load(jsonfile)

print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')))

# #Pour toutes les activités dans data
# for i in data["data"]:
# 	#on crée un activité puis on lui ajoute tous ses attributs

#  	#on affiche tous les attributs de l'activite