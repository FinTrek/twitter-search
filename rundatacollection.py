import coronavirus
import time

fileCount = 1
while True:
	fileCount+=1
	coronavirus.generateData('coronavirus', fileCount)
	time.sleep(15*60)
	coronavirus.generateData('wuhanvirus', fileCount)
	time.sleep(15*60)
	coronavirus.generateData('covid19', fileCount)
	time.sleep(15*60)
	coronavirus.generateData('COVID2019', fileCount)
	time.sleep(15*60)
	coronavirus.generateData('CoronaVirusOutbreak', fileCount)
	time.sleep(15*60)
	coronavirus.generateData('CoronaVirusUpdate', fileCount)
	time.sleep(15*60)
	time.sleep(6*60*60)


#Every 6 hours, this program generates a tweet dataset