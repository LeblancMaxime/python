class Installation(object):

	def __init__(self, comLib):
		self.comLib = comLib
		
	# def getComInsee(self):
	# 	return self.comInsee

	# def setComInsee(self, comInsee):
	# 	self.comInsee = comInsee

	def getComLib(self):
		return self.comLib

	def setComLib(self, comLib):
		self.comLib = comLib

	# def getInsAccessibiliteAucun(self):
	# 	return self.insAccessibiliteAucun

	# def setInsAccessibiliteAucun(self, insAccessibiliteAucun):
	# 	self.insAccessibiliteAucun = insAccessibiliteAucun

	# def getInsAccessibiliteHandiMoteur(self):
	# 	return self.insAccessibiliteHandiMoteur

	# def setInsAccessibiliteHandiMoteur(self, insAccessibiliteHandiMoteur):
	# 	self.insAccessibiliteHandiMoteur = insAccessibiliteHandiMoteur

	# def getInsAccessibiliteHandiSens(self):
	# 	return self.insAccessibiliteHandiSens

	# def setInsAccessibiliteHandiSens(self, insAccessibiliteHandiSens):
	# 	self.insAccessibiliteHandiSens = insAccessibiliteHandiSens

	def getInsCodePostal(self):
		return self.insCodePostal

	def setInsCodePostal(self, insCodePostal):
		self.insCodePostal = insCodePostal

	# def getInsDateMaj(self):
	# 	return self.insDateMaj

	# def setInsDateMaj(self, insDateMaj):
	# 	self.insDateMaj = insDateMaj

	# def getInsEmpriseFonciere(self):
	# 	return self.insEmpriseFonciere 

	# def setInsEmpriseFonciere(self, insEmpriseFonciere):
	# 	self.insEmpriseFonciere = insEmpriseFonciere

	# def getInsGardiennee(self):
	# 	return self.insGardiennee

	# def setInsGardiennee(self, insGardiennee):
	# 	self.insGardiennee = insGardiennee

	def getInsLibelleVoie(self):
		return self.insLibelleVoie

	def setInsLibelleVoie(self, insLibelleVoie):
		self.insLibelleVoie = insLibelleVoie

	# def getInsLieuDit(self):
	# 	return self.insLieuDit

	# def setInsLieuDit(self, insLieuDit):
	# 	self.insLieuDit = insLieuDit

	# def getInsMultiCommune(self):
	# 	return self.insMultiCommune

	# def setInsMultiCommune(self, insMultiCommune):
	# 	self.insMultiCommune = insMultiCommune

	# def getInsNbPlaceParking(self):
	# 	return self.insNbPlaceParking

	# def setInsNbPlaceParking(self, insNbPlaceParking):
	# 	self.insNbPlaceParking = insNbPlaceParking

	# def getInsNbPlaceParkingHandi(self):
	# 	return self.insNbPlaceParkingHandi

	# def setInsNbPlaceParkingHandi(self, insNbPlaceParkingHandi):
	# 	self.insNbPlaceParkingHandi = insNbPlaceParkingHandi

	# def getInsNoVoie(self):
	# 	return self.insNoVoie

	# def setInsNoVoie(self, insNoVoie):
	# 	self.insNoVoie = insNoVoie

	def getInsNumeroInstall(self):
		return self.insNumeroInstall

	def setInsNumeroInstall(self, insNumeroInstall):
		self.insNumeroInstall = insNumeroInstall

	# def getInsPartLibelle(self):
	# 	return self.insPartLibelle

	# def setInsPartLibelle(self, insPartLibelle):
	# 	self.insPartLibelle = insPartLibelle

	# def getInsTransportAutre(self):
	# 	return self.insTransportAutre

	# def setInsTransportAutre(self, insTransportAutre):
	# 	self.insTransportAutre = insTransportAutre

	# def getInsTransportBateau(self):
	# 	return self.insTransportBateau

	# def setInsTransportBateau(self, insTransportBateau):
	# 	self.insTransportBateau = insTransportBateau

	# def getInsTransportBus(self):
	# 	return self.insTransportBus

	# def setInsTransportBus(self, insTransportBus):
	# 	self.insTransportBus = insTransportBus

	# def getInsTransportMetro(self):
	# 	return self.insTransportMetro

	# def setInsTransportMetro(self, insTransportMetro):
	# 	self.insTransportMetro = insTransportMetro

	# def getInsTransportTrain(self):
	# 	return self.insTransportTrain

	# def setInsTransportTrain(self, insTransportTrain):
	# 	self.insTransportTrain = insTransportTrain

	# def getInsTransportTram(self):
	# 	return self.insTransportTram

	# def setInsTransportTram(self, insTransportTram):
	# 	self.insTransportTram = insTransportTram

	def getLatitude(self):
		return self.latitude

	def setLatitude(self, latitude):
		self.latitude = latitude

	def getLongitude(self):
		return self.longitude

	def setLongitude(self, longitude):
		self.longitude = longitude

	# def getNb_Equipements(self):
	# 	return self.nb_Equipements

	# def setNb_Equipements(self, nb_Equipements):
	# 	self.nb_Equipements = nb_Equipements

	# def getNb_FicheEquipement(self):
	# 	return self.nb_FicheEquipement

	# def setNb_FicheEquipement(self, nb_FicheEquipement):
	# 	self.nb_FicheEquipement = nb_FicheEquipement

	# def get_l(self):
	# 	return self._l

	# def set_l(self, _l):
	# 	self._l = _l

	def getGeo(self):
		return self.geo["name"]

	def setGeo(self, geo):
		self.geo = geo

	# def toString(self):
	# 	ret = "[\n\tComInsee: {0},\n\tComLib {1},\n\tInsAccessibiliteAucun: {2},\n\tInsAccessibiliteHandiMoteur: {3},\n\tInsAccessibiliteHandiSens: {4},\n\tInsCodePostal: {5},\n\tInsDateMaj: {6},\n\tInsEmpriseFonciere: {7},\n\tInsGardiennee: {8},\n\tInsLibelleVoie: {9}, \n\tInsLieuDit: {10}, \n\tInsMultiCommune: {11}, \n\tInsNbPlaceParking: {12}, \n\tInsNbPlaceParkingHandi: {13}, \n\tInsNoVoie: {14}, \n\tInsNumeroInstall: {15}, \n\tInsPartLibelle: {16}, \n\tInsTransportAutre: {17}, \n\tInsTransportBateau: {18}, \n\tInsTransportBus: {19}, \n\tInsTransportMetro: {20}, \n\tInsTransportTrain: {21}, \n\tInsTransportTram: {22}, \n\tLatitude: {23}, \n\tLongitude: {24}, \n\tNb_Equipements: {25}, \n\tNb_FicheEquipement: {26}, \n\t_l: {27}, \n\tgeo: {28}\n]".format(self.comInsee, self.comLib, self.insAccessibiliteAucun, self.insAccessibiliteHandiMoteur, self.insAccessibiliteHandiSens, self.insCodePostal, self.insDateMaj, self.insEmpriseFonciere, self.insGardiennee, self.insLibelleVoie, self.insLieuDit, self.insMultiCommune, self.insNbPlaceParking, self.insNbPlaceParkingHandi, self.insNoVoie, self.insNumeroInstall, self.insPartLibelle, self.insTransportAutre, self.insTransportBateau, self.insTransportBus, self.insTransportMetro, self.insTransportTrain, self.insTransportTram, self.latitude, self.longitude, self.nb_Equipements, self.nb_FicheEquipement, self._l, self.geo)
	# 	print(ret);