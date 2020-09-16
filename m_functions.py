# determine what kind of input -> handle it accordingly
def getInput(kind,values):
	values = values.replace('"','\'').replace('\n', '').replace('\t', '')
	if kind == 'genre':
		return getGenre(values)
	elif kind == 'description':
		return getDescription(values)
	else:
		return '"'+ kind + '": "' + values + '",\n'

#skip input
def skipInput(kind):
	return '"'+ kind + '": "",\n'

# function to split genre string and return the correct form
def getGenre(values):
	values = values.split(', ')
	genre = '['
	for x in values:
		genre += '"' + x + '",'
	genre ='"genre": ' + genre[:-1] + "],\n"
	return genre

# handle description with "quote" sign that break the details.json
def getDescription(values):
	values = values.replace('"','\'').replace('\n', ' ').replace('\t', ' ')
	return '"description": "' + values + '",\n'

# ## Main Program ##
# details = open('details.json','w')
# result = '{\n'
# result += getInput('title')
# result += skipInput('author')
# result += skipInput('artist')
# result += getInput('description')
# result += getInput('genre')
# print('\nstatus values": ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed"]')
# result += skipInput('status')
# result += '"_status values": ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed"]\n}'
# details.write(result)
# details.close()


