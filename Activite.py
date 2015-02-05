class Activite:
	actCode
	actLib
	actNivLib
	comInsee
	comLib
	equActivitePraticable
	equActivitePratique
	equActiviteSalleSpe
	equNbEquIdentique
	equipementId

	def __init__(self, actCode, actLib,	actNivLib, comInsee, comLib, equActivitePraticable, equActivitePratique, equActiviteSalleSpe, equNbEquIdentique, equipementId):
		self.actCode = actCode
		self.actLib = actLib
		self.actNivLib = actNivLib
		self.comInsee = comInsee
		self.comLib = comLib
		self.equActivitePraticable = equActivitePraticable
		self.equActivitePratique = equActivitePratique
		self.equActiviteSalleSpe = equActiviteSalleSpe
		self.equNbEquIdentique = equNbEquIdentique
		self.equipementId = equipementId

	def getActCode(self):
		return self.actCode

	def setActCode(self, actCode):
		self.actCode = actCode

	def getActLib(self):
		return self.actLib

	def setActLib(self, actLib):
		self.actLib = actLib

	def getActNivLib(self):
		return self.actNivLib

	def setActNivLib(self, actNivLib):
		self.actNivLib = actNivLib

	def getComInsee(self):
		return self.comInsee

	def setComInsee(self, comInsee):
		self.comInsee = comInsee

	def getComLib(self):
		return self.comLib

	def setComLib(self, comLib):
		self.comLib = comLib

	def getEquActivitePraticable(self):
		return self.equActivitePraticable

	def setEquActivitePraticable(self, equActivitePraticable):
		self.equActivitePraticable = equActivitePraticable

	def getEquActivitePratique(self):
		return self.equActivitePratique

	def setEquActivitePratique(self, equActivitePratique):
		self.equActivitePratique = equActivitePratique

	def getEquActiviteSalleSpe(self):
		return self.equActiviteSalleSpe

	def setEquActiviteSalleSpe(self, equActiviteSalleSpe):
		self.equActiviteSalleSpe = equActiviteSalleSpe

	def getEquNbEquIdentique(self):
		return self.equNbEquIdentique

	def setEquNbEquIdentique(self, equNbEquIdentique):
		self.equNbEquIdentique = equNbEquIdentique

	def getEquipementId(self):
		return self.equipementId

	def setEquipementId(self, equipementId):
		self.equipementId = equipementId

	def toString(self):
		ret = "[\n{0},\n{1},\n{2},\n{3},\n{4},\n{5},\n{6},\n{7},\n{8},\n{9}\n]".format(self.actCode, self.actLib, self.actNivLib, self.comInsee, self.comLib, self.equActivitePraticable, self.equActivitePratique, self.equActiviteSalleSpe, self.equNbEquIdentique, self.equipementId)
		print(ret);