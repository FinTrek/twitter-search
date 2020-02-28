import coronavirus
import time

fileCount = 3
while True:
	fileCount+=1
	print('Collecting data for coronavirus... ', end='', flush=True)
	coronavirus.generateData('coronavirus', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)
	print('Done.')

	print('Collecting data for wuhanvirus... ', end='', flush=True)
	coronavirus.generateData('wuhanvirus', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)
	print('Done.')

	print('Collecting data for covid19... ', end='', flush=True)
	coronavirus.generateData('covid19', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)
	print('Done.')
	
	print('Collecting data for COVID2019... ', end='', flush=True)
	coronavirus.generateData('COVID2019', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)
	print('Done.')
	
	print('Collecting data for CoronaVirusOutbreak... ', end='', flush=True)
	coronavirus.generateData('CoronaVirusOutbreak', fileCount)
	print('Done.\nSleeping for 15 minutes... ')
	time.sleep(15*60)
	print('Done.')
	
	print('Collecting data for CoronaVirusUpdate... ', end='', flush=True)
	coronavirus.generateData('CoronaVirusUpdate', fileCount)
	print('Done.\nWaiting for 6 hours before collecting again... ', end='', flush=True)
	time.sleep(6*60*60)
	print('Done.')

#Every 6 hours, this program generates a tweet dataset
