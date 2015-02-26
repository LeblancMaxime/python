#On importe
import json
from Activite import Activite

#On ouvre le fichier json
jsonfile = open('json/activite.json')
data = json.load(jsonfile)

#Pour toutes les activités dans data
for i in data["data"]:
	#on crée un activité puis on lui ajoute tous ses attributs
 	activity = Activite(i["ActCode"])
 	activity.setActLib(i["ActLib"])
 	activity.setActNivLib(i["ActNivLib"])
 	activity.setComInsee(i["ComInsee"])
 	activity.setComLib(i["ComLib"])
 	activity.setEquActivitePraticable(i["EquActivitePraticable"])
 	activity.setEquActivitePratique(i["EquActivitePratique"])
 	activity.setEquActiviteSalleSpe(i["EquActiviteSalleSpe"])
 	activity.setEquNbEquIdentique(i["EquNbEquIdentique"])
 	activity.setEquipementId(i["EquipementId"])
 	#on affiche tous les attributs de l'activite
 	activity.toString()