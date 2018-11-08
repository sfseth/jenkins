import csv


# TODO: parameterize filename, turn file operations into function, handle response strings that are in diff position
rspStrings = []
with open('test.log') as file:
	data = csv.reader(file, delimiter=' ')
	for line in data:
		rspStrings.append(line[2])
		print(line[2])

def test_responses():
	assert rspStrings.count('INFO') == 50
	assert rspStrings.count('WARNING') == 11
	assert rspStrings.count('ERROR') == 3
