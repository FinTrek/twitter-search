import coronavirus
import time

fileCount = 1
while True:
	fileCount+=1
	print('Collecting data for coronavirus... ', end='')
	coronavirus.generateData('coronavirus', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)

	print('Collecting data for wuhanvirus... ', end='')
	coronavirus.generateData('wuhanvirus', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)

	print('Collecting data for covid19... ', end='')
	coronavirus.generateData('covid19', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)
	print('Collecting data for COVID2019... ', end='')
	coronavirus.generateData('COVID2019', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)
	print('Collecting data for CoronaVirusOutbreak... ', end='')
	coronavirus.generateData('CoronaVirusOutbreak', fileCount)
	print('Done.\nSleeping for 15 minutes...')
	time.sleep(15*60)
	print('Collecting data for CoronaVirusUpdate... ', end='')
	coronavirus.generateData('CoronaVirusUpdate', fileCount)
	print('Done.\nWaiting for 6 hours before collecting again...')
	time.sleep(15*60)
	time.sleep(6*60*60)


#Every 6 hours, this program generates a tweet dataset