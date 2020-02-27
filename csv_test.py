import csv

with open('data/1_022520.csv', 'w') as f:
	writer = csv.writer(f)

	columns = ["col1", "col2", "col3", "col4", "col5"]
	writer.writerow(columns)

	for i in range(10):
		writer.writerow([i, i+1, i+2, i+3, i+4])

	