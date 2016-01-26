import json, pymongo

data = open('data.json', 'r').read()
data = json.loads(data)

mongoURI = "mongodb://127.0.0.1:27017"
try:
	con = pymongo.MongoClient(host=mongoURI, port=27017)
	db = con['teacher']
	for teacher in data:
		db.main.insert({ 'name': teacher, 'data': data[teacher] })
except:
	print "[Error] Cannot connect with mongodb."
