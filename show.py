import cherrypy
import json
import sqlite3
import jsonToDatabase as j


j.createDatabase()


class WebManager(object):
	"""
	Exposes web services
	"""
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		write = """<h2>Hi ! You can chose your section right here !</h2>
					<br />
					<a href='/index_activity/'><input type='button' value='Activities'></a>
					<a href='/index_equipment/'><input type='button' value='Equipments'></a>
					<a href='/index_installation/'><input type='button' value='Installations'></a>
					<br /><br />
					<p>If you want to have informations about a city, click here : <a href='/index_cities/'><input type='button' value='List of cities'></a>
					<br />
					If you want to search, click here : <a href='/search'><input type='button' value='search'></a></p>
				"""
		return write
	
	@cherrypy.expose
	def index_activity(self):
		"""
		Exposes the service at localhost:8080/index_activity/
		"""
		numberOfItems = 0
		conn = sqlite3.connect('allData.db')
		c = conn.cursor() 
		# We count the number of items
		for row in c.execute("SELECT * FROM activite"):
			numberOfItems = numberOfItems + 1
		# We commit data
		conn.commit()
		# We close the connection
		conn.close()
		write = """<h2>Hi ! You are here to check activities !</h2>
					<br />
					There are {0} activities !
					<br />
					If you want to go back to the index, click on the button : <a href='http://localhost:8080'><input type='button' value='Index'></a>
				""".format(numberOfItems)
		return write

	@cherrypy.expose
	def index_equipment(self):
		"""
		Exposes the service at localhost:8080/index_equipement/
		"""
		numberOfItems = 0
		conn = sqlite3.connect('allData.db')
		c = conn.cursor() 
		# We count the number of items
		for row in c.execute("SELECT * FROM equipement"):
			numberOfItems = numberOfItems + 1
		# We commit data
		conn.commit()
		# We close the connection
		conn.close()
		write = """<h2>Hi ! You are here to check equipements !</h2>
					<br />
					There are {0} equipements !
					<br />
					If you want to go back to the index, click on the button : <a href='http://localhost:8080'><input type='button' value='Index'></a>
				""".format(numberOfItems)
		return write

	@cherrypy.expose
	def index_installation(self):
		"""
		Exposes the service at localhost:8080/index_installation/
		"""
		numberOfItems = 0
		conn = sqlite3.connect('allData.db')
		c = conn.cursor() 
		# We count the number of items
		for row in c.execute("SELECT * FROM installation"):
			numberOfItems = numberOfItems + 1
		# We commit data
		conn.commit()
		# We close the connection
		conn.close()
		write = """<h2>Hi ! You are here to check installations !</h2>
					<br />
					There are {0} installations !<br />
					If you want to go back to the index, click on the button : <a href='http://localhost:8080'><input type='button' value='Index'></a>
				""".format(numberOfItems)
		return write

	@cherrypy.expose
	def index_cities(self):
		"""
		Exposes the service at localhost:8080/index_cities/
		"""
		write = "If you want to go back to the index, click on the button : <a href='http://localhost:8080'><input type='button' value='Index'></a><ul>"
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		liste = list()
		for row in c.execute("SELECT * FROM installation ORDER BY comLib"):
			if row[0] not in liste:
				write = write + "<li><a href='http://localhost:8080/show_city/" + str(row[0]) + "''>" + str(row[0]) + "</li>"
				liste.append(row[0])
		# On commit les données
		conn.commit()
		# On ferme la connexion
		conn.close()
		write = write + "</ul>"
		return write

	@cherrypy.expose
	def show_city(self, city):
		"""
		Exposes the service at localhost:8080/show_city/{city}
		"""
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		write = """<table border='1px solid black' cellspacing='0' cellpadding='0'>
						<tr>
							<th>Numéro d'activité</th>
							<th>Nom de l'activité</th>
						</tr>
				"""
		for row in c.execute("SELECT * FROM activite WHERE comLib='" + str(city) + "' ORDER BY actCode"):
			write = write + "<tr><td>" + row[0] + "</td><td>" + row[1] + "</td></tr>"
		write = write + "</table>"
		return write

	@cherrypy.expose
	def search(self):
		"""
		Exposes the service at localhost:8080/search
		"""
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		city = list()
		activity = list()
		write = """Select a city, then an activity and find where you can do it
					<form method='get' action='http://localhost:8080/result/'>
						<input type='text' id='city' name='city' />
						<input type='text' id='activity' name='activity' />
						<input type='submit' value='search' />
					</form>"""
		return write

	@cherrypy.expose
	def result(self, city, activity):
		"""
		Exposes the service at localhost:8080/result/city&activity
		"""
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		write = """<table border='1px solid black' cellspacing='0' cellpadding='0'>
						<tr>
							<th>Nom equipement</th>
						</tr>
				"""
		for row in c.execute("SELECT e.insNom FROM equipement e WHERE e.comLib like '%" + str(city) + "%' ORDER BY e.insNom"):
			write = write + "<tr><td>" + row[0] + "</td></tr>"
		write = write + "</table>"
		return write

	@cherrypy.expose
	def activity_select(self):
		"""
		Exposes the service at localhost:8080/activity_select/
		"""
		write = "<select><option selected='selected'>No activity selected</option>"
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		liste = list()
		for row in c.execute("SELECT * FROM activite ORDER BY actCode"):
			if row[1] not in liste:
				write = write + "<option>" + str(row[1]) + "</option>"
				liste.append(row[1])
		# On commit les données
		conn.commit()
		# On ferme la connexion
		conn.close()
		write = write + "<select>"
		return write

	@cherrypy.expose
	def activity_show_all(self):
		"""
		Exposes the service at localhost:8080/activity_show_all/
		"""
		res = ""
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		res = "<table border='1px solid black' cellspacing='0' cellpadding='0'><tr><th>Numero d'activite</th><th>Nom d'activite</th><th>Ville</th></tr>"
		for row in c.execute("SELECT * FROM activite ORDER BY comLib"):
			res = res + "</td><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2]) + "</tr>"
		res = res + "</table>"
		# On commit les données
		conn.commit()
		# On ferme la connexion
		conn.close()
		return res
	 
	@cherrypy.expose
	def activity_show(self, id):
		"""
		Exposes the service at localhost:8080/activity_show/[id]/
		"""
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		try:
			cmd = "SELECT * FROM activite ORDER BY actCode LIMIT " + format(id)
			for row in c.execute(cmd):
				res = str(row[0]) + "<br />" + str(row[1])
		except (IndexError, IOError):
			return "Invalid ID"
		 
		return res
	 
	@cherrypy.expose
	def installation_select(self):
		"""
		Exposes the service at localhost:8080/installation_select/
		"""
		write = "<select><option selected='selected'>No installation selected</option>"
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		liste = list()
		for row in c.execute("SELECT * FROM installation ORDER BY insNumeroInstall"):
			if row[0] not in liste:
				write = write + "<option id='" + str(row[0]) + "'>" + str(row[0]) + "</option>"
				liste.append(row[0])
		# On commit les données
		conn.commit()
		# On ferme la connexion
		conn.close()
		write = write + "</select>"
		return write

	@cherrypy.expose
	def installation_show_all(self):
		"""
		Exposes the service at localhost:8080/installation_show_all/
		"""
		res = ""
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		for row in c.execute("SELECT * FROM installation ORDER BY comLib"):
			res = res + str(row) + "<br />"
		# On commit les données
		conn.commit()
		# On ferme la connexion
		conn.close()
		return res
	 
	@cherrypy.expose
	def activity_show(self, id):
		"""
		Exposes the service at localhost:8080/activity_show/[id]/
		"""
		conn = sqlite3.connect('allData.db')
		c = conn.cursor()
		try:
			cmd = "SELECT * FROM activite ORDER BY actCode LIMIT " + format(id)
			for row in c.execute(cmd):
				res = str(row[0]) + "<br />" + str(row[1])
		except (IndexError, IOError):
			return "Invalid ID"
		 
		return res
cherrypy.quickstart(WebManager()) 