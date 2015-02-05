#import parse
import json

jsonfile = open('json/activite.json')
data = json.load(jsonfile)

#print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
print(data["nb_results"][0])
# dataBis = json.dumps(data)

# for i in range(0, 10):
# 	print(jsonfile[i][1])
# 	print("\n")


# liste = list()
# position = 0
# mot = False

# for value in dataBis:	
# 	if value == "\"":
# 		if mot:
# 			mot = False
# 			position = position + 1
# 		elif not mot:
# 			mot = True
# 	if mot:
# 		print(position)
# 		liste[position] = str(liste[position]) + str(value)

# for word in liste:
# 	print(word)
