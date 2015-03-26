# We import
import json
import sqlite3
from model.Installation import Installation
from model.Activite import Activite
from model.Equipement import Equipement


def createDatabase():
	"""
	Create the database and the three tables: installation, activity and equipment; and set the data into them
	"""
	# We open the json file for installation
	jsonfile = open('json/installation.json')
	data = json.load(jsonfile)

	# We create the connection
	conn = sqlite3.connect('allData.db')
	c = conn.cursor()

	# We delete installation's table if it exists and then we create it again
	c.execute("DROP TABLE IF EXISTS installation")
	c.execute("CREATE TABLE installation(comLib text, insCodePostal text, insLibelleVoie text, insNumeroInstall text, insLatitude text, insLongitude text, geo text)")

	# We create each installations
	for i in data["data"]:
		# We put installations' attributes
		installation = Installation(i["ComLib"])
		installation.setComLib(i["ComLib"])
		installation.setInsCodePostal(i["InsCodePostal"])
		installation.setInsLibelleVoie(i["InsLibelleVoie"])
		installation.setInsNumeroInstall(i["InsNumeroInstall"])
		installation.setLatitude(i["Latitude"])
		installation.setLongitude(i["Longitude"])
		installation.setGeo(i["geo"])
		# We insert data into database
		c.execute("INSERT INTO installation VALUES (?, ?, ?, ?, ?, ?, ?)",
			[installation.getComLib(),
			installation.getInsCodePostal(),
			installation.getInsLibelleVoie(),
			installation.getInsNumeroInstall(),
			installation.getLatitude(),
			installation.getLongitude(),
			installation.getGeo()])

	# We open the json file for activity
	jsonfile = open('json/activite.json')
	data = json.load(jsonfile)

	# We delete activity's table if it exists and then we create it again
	c.execute("DROP TABLE IF EXISTS activite")
	c.execute("CREATE TABLE activite(actCode text, actLib text, comLib text)")

	# We create each activities
	for i in data["data"]:
		# We put activities' attributes
		activity = Activite(i["ActCode"])
		activity.setActCode(i["ActCode"])
		activity.setActLib(i["ActLib"])
		activity.setComLib(i["ComLib"])
		# We insert data into database
		c.execute("INSERT INTO activite VALUES (?, ?, ?)",
			[activity.getActCode(),
			activity.getActLib(),
			activity.getComLib()])

	# We open the json file for equipement
	jsonfile = open('json/equipement.json')
	data = json.load(jsonfile)

	# We delete equipement's table if it exists and then we create it again
	c.execute("DROP TABLE IF EXISTS equipement")
	c.execute("CREATE TABLE equipement(equipementId text, insNom text, insNumeroInstall text, comLib text)")

	# We create each equipements
	for i in data["data"]:
		# We put equipements' attributes
		equipement = Equipement(i["EquipementId"])
		equipement.setEquipementId(i["EquipementId"])
		equipement.setInsNom(i["InsNom"])
		equipement.setInsNumeroInstall(i["InsNumeroInstall"])
		equipement.setComLib(i["ComLib"])
		# We insert data into database
		c.execute("INSERT INTO equipement VALUES (?, ?, ?, ?)",
			[equipement.getEquipementId(),
			equipement.getInsNom(),
			equipement.getInsNumeroInstall(),
			equipement.getComLib()])

	# We commit data
	conn.commit()

	# We close the connection
	conn.close()