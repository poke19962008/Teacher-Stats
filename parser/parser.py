import pymongo, json

'''
	DATA STRUCTURE
		data = {
			subjectCode: {
				ct1: {
					'0-10': [INT],
					'10-20': [INT],
					.........
				},
				ct2: {
					'0-10': [INT],
					'10-20': [INT],
					.........
				},
				mt: {
					'0-10': [INT],
					'10-20': [INT],
					.........
				},
				internal: {
					'0-10': [INT],
					'10-20': [INT],
					.........
				},
				attendance: {
					'0-10': [INT],
					'10-20': [INT],
					.........
				}
				students: [INT]frequency
			}
		}
'''

data = json.loads(open('test.json', 'r').read())

mongoURI = "mongodb://127.0.0.1:27017"
try:
	con = pymongo.MongoClient(host=mongoURI, port=27017)
	db = con['zoho_swe']
	connected = True
except:
	print "[Error] Cannot connect with mongodb."

def rangeParser(student, data, sub, key, factor):
	if student[sub][key]*factor < 10:
		data[faculty][sub][key]['0-10'] = data[faculty][sub][key]['0-10'] + 1

	elif  student[sub][key]*factor >= 10 and student[sub][key]*factor < 20:
		data[faculty][sub][key]['10-20'] = data[faculty][sub][key]['10-20'] + 1

	elif  student[sub][key]*factor >= 20 and student[sub][key]*factor < 30:
		data[faculty][sub][key]['20-30'] = data[faculty][sub][key]['20-30'] + 1

	elif  student[sub][key]*factor >= 30 and student[sub][key]*factor < 40:
		data[faculty][sub][key]['30-40'] = data[faculty][sub][key]['30-40'] + 1

	elif  student[sub][key]*factor >= 40 and student[sub][key]*factor < 50:
		data[faculty][sub][key]['40-50'] = data[faculty][sub][key]['40-50'] + 1

	elif  student[sub][key]*factor >= 50 and student[sub][key]*factor < 60:
		data[faculty][sub][key]['50-60'] = data[faculty][sub][key]['50-60'] + 1

	elif  student[sub][key]*factor >= 60 and student[sub][key]*factor < 70:
		data[faculty][sub][key]['60-70'] = data[faculty][sub][key]['60-70'] + 1

	elif  student[sub][key]*factor >= 70 and student[sub][key]*factor < 80:
		data[faculty][sub][key]['70-80'] = data[faculty][sub][key]['70-80'] + 1

	elif  student[sub][key]*factor >= 80 and student[sub][key]*factor < 90:
		data[faculty][sub][key]['80-90'] = data[faculty][sub][key]['80-90'] + 1

	elif  student[sub][key]*factor >= 90 and student[sub][key]*factor < 100:
		data[faculty][sub][key]['90-100'] = data[faculty][sub][key]['90-100'] + 1

	return data

def compute(student, sub, data):
	if student[sub]['pt'] != '-':
		keys = ['pt', 'internal']
		multiplier = {
			'pt': 2,
			'internal': 1.66,
		}
	else:
		keys = ['ct1', 'ct2', 'mt', 'internal']
		multiplier = {
			'ct1': 10,
			'ct2': 10,
			'mt': 5,
			'internal': 2,
		}

	for key in keys:
		data = rangeParser(student, data, sub, key, multiplier[key])
	data = rangeParser(student, data, sub, 'attendance', 1)
	data[faculty][sub]['student'] = data[faculty][sub]['student'] + 1

	return data
	
def setZero(data, faculty, sub, key):
	data[faculty][sub][key] = {}
	data[faculty][sub][key]['0-10'] = 0
	data[faculty][sub][key]['10-20'] = 0
	data[faculty][sub][key]['20-30'] = 0
	data[faculty][sub][key]['30-40'] = 0
	data[faculty][sub][key]['40-50'] = 0
	data[faculty][sub][key]['50-60'] = 0
	data[faculty][sub][key]['60-70'] = 0
	data[faculty][sub][key]['70-80'] = 0
	data[faculty][sub][key]['80-90'] = 0
	data[faculty][sub][key]['90-100'] = 0

	return data


def init(data, faculty, sub, isPrac):
	data[faculty][sub] = {}
	data[faculty][sub]['attendance'] = {}
	if isPrac:
		keys = ['pt', 'internal']
	else:
		keys = ['ct1', 'ct2', 'mt', 'internal']

	for key in keys:
		data = setZero(data, faculty, sub, key)

	data[faculty][sub]['student'] = 0 
	data = setZero(data, faculty, sub, 'attendance')
	return data			

counter = 50
for student in db.main.find():
	student = student['course']
	for sub in  student:
		faculty =  student[sub]['faculty']
		if not data.has_key(faculty):
			data[faculty] = {}
			if not data[faculty].has_key(sub):
				isPrac = False
				if student[sub]['pt'] != '-':
					isPrac = True
				data = init(data, faculty, sub, isPrac)
				data = compute(student, sub, data)
		else:
			if not data[faculty].has_key(sub):
				isPrac = False
				if student[sub]['pt'] != '-':
					isPrac = True
				data = init(data, faculty, sub, isPrac)
				data = compute(student, sub, data)
			data = compute(student, sub, data)
			
file = open('test.json', "w")
file.write(json.dumps(data, indent=2))

