from urllib import request
import csv

CSV_URL = 'http://finance.yahoo.com/d/quotes.csv?s='

stocks = []

with open('companylist.csv') as csvfile:
	read = csv.DictReader(csvfile)
	i = 0
	for row in read:
		if i < 200:
			stocks.append('' + row['Symbol'])
			i += 1
print(stocks)

for index in range(len(stocks)):
	CSV_URL += stocks[index]
	if index < len(stocks) - 1:
		CSV_URL += '+'
CSV_URL += '&f=nsophgved'

#print(CSV_URL)
response = request.urlopen(CSV_URL)
csv = response.read()

csvstr = str(csv).strip("b'")

lines = csvstr.split("\\n")
f = open("stocks.csv", "w")
for line in lines:
	f.write(line + "\n")
f.close()