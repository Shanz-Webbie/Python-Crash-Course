import csv
from datetime import datetime 

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get dates, and high an low temperatures from this file.
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[2],'%Y-%m-%d')
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)


# Plot the high and low temperatures.
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates, highs, c ='red')
	ax.plot(dates, lows, c='blue')

	#Format plot.
	title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
	ax.set_title(title, fontsize= 20)
	ax.set_xlabel('', fontsize = 16)
	fig.autofmt_xdate()
	ax.set_ylabel("Temperature (F)", fontsize= 16)
	ax.tick_params(axis= 'both', which='major', labelsize= 16)

	plt.show()