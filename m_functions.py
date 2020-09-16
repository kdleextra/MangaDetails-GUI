# determine what kind of input -> handle it accordingly
def getInput(kind):
	if kind == 'genre':
		return getGenre()
	elif kind == 'description':
		return getDescription(kind)
	else:
		print('>>' + kind +':')
		string = input()
		return '"'+ kind + '": "' + string + '",\n'

#skip input
def skipInput(kind):
	print('>>' + kind +':')
	return '"'+ kind + '": "",\n'

# function to split genre string and return the correct form
def getGenre():
	print('>> genre:')
	s = input()
	s = s.split(', ')
	genre = '['
	for x in s:
		genre += '"' + x + '",'
	genre ='"genre": ' + genre[:-1] + "],\n"
	return genre

# handle description with "quote" sign that break the details.json
def getDescription(kind):
	print('>> description:')
	s = input()
	s = s.replace('"','\'')
	return '"'+ kind + '": "' + s + '",\n'

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


