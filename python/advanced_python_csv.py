import csv

f = open('faculty.csv')
csv_f = csv.reader(f)

email = []
email = email[1::]

for row in csv_f:
    email.append(row[3])

resultFile = open("emails.csv",'wb')
wr = csv.writer(resultFile, quoting = csv.QUOTE_ALL)
wr.writerow(email)
