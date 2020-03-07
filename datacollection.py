import coronavirus
import time

#Get current file count:
fileCount = 17
try:
	with open('data/fileCount.txt', 'r') as f:
			fileCount = int(f.read())
except:
	print(f'fileCount.txt not found, using default count ({fileCount}).')


#Data Collection
while True:
	fileCount+=1

	terms = ['coronavirus', 'wuhanvirus', 'covid19',
			 'COVID2019', 'CoronaVirusOutbreak', 'CoronaVirusUpdate']

	print(f'Set #{fileCount}:')

	#generate a dataset for each term
	for term in terms:
		print(f'Collecting data for {term}... ', end='', flush=True)
		coronavirus.generateData(f'{term}', fileCount)
		if term != terms[-1]:
			print('Done.\nSleeping for 15 minutes... ', end='', flush=True)
			time.sleep(15*60)
		print('Done.', flush=True)
	
	#Record latest fileCount
	with open('data/fileCount.txt', 'w') as f:
		f.write(str(fileCount))

	print('Done.\nBegin cooldown period: 6 hours', flush=True)

	#Six hour cooldown period
	for i in range(6):
		n = 6 - i
		if n > 1:
			print(f'{n} hours remaining... ')
		else:
			print(f'{n} hour remaining... ', end = '', flush=True)
		time.sleep(1*60*60)

	print('Done.\n', flush=True)


#Every 6 hours, this program generates a tweet dataset
