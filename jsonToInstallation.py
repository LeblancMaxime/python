#On importe
import json
from Installation import Installation

#On ouvre le fichier json
jsonfile = open('json/installation.json')
data = json.load(jsonfile)

#Pour toutes les activités dans data
for i in data["data"]:
	#on crée un installation puis on lui ajoute tous ses attributs
 	installation = Installation(i["ComInsee"])
 	installation.setComLib(i["ComLib"])
 	installation.setInsAccessibiliteAucun(i["InsAccessibiliteAucun"])
 	installation.setInsAccessibiliteHandiMoteur(i["InsAccessibiliteHandiMoteur"])
 	installation.setInsAccessibiliteHandiSens(i["InsAccessibiliteHandiSens"])
 	installation.setInsCodePostal(i["InsCodePostal"])
 	installation.setInsDateMaj(i["InsDateMaj"])
 	installation.setInsEmpriseFonciere(i["InsEmpriseFonciere"])
 	installation.setInsGardiennee(i["InsGardiennee"])
 	installation.setInsLibelleVoie(i["InsLibelleVoie"])
 	installation.setInsLieuDit(i["InsLieuDit"])
 	installation.setInsMultiCommune(i["InsMultiCommune"])
 	installation.setInsNbPlaceParking(i["InsNbPlaceParking"])
 	installation.setInsNbPlaceParkingHandi(i["InsNbPlaceParkingHandi"])
 	installation.setInsNoVoie(i["InsNoVoie"])
 	installation.setInsNumeroInstall(i["InsNumeroInstall"])
 	installation.setInsPartLibelle(i["InsPartLibelle"])
 	installation.setInsTransportAutre(i["InsTransportAutre"])
 	installation.setInsTransportBateau(i["InsTransportBateau"])
 	installation.setInsTransportBus(i["InsTransportBus"])
 	installation.setInsTransportMetro(i["InsTransportMetro"])
 	installation.setInsTransportTrain(i["InsTransportTrain"])
 	installation.setInsTransportTram(i["InsTransportTram"])
 	installation.setLatitude(i["Latitude"])
 	installation.setLongitude(i["Longitude"])
 	installation.setNb_Equipements(i["Nb_Equipements"])
 	installation.setNb_FicheEquipement(i["Nb_FicheEquipement"])
 	installation.set_l(i["_l"])
 	installation.setGeo(i["geo"])
 	#on affiche tous les attributs de l'activite
 	installation.toString()