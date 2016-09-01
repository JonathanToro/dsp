import csv

f = open('faculty.csv')
csv_f = csv.reader(f)

email = []
email = email[1::]

for row in csv_f:
    email.append(row[3])

with open('emails.csv', 'wb') as f:
        writer = csv.writer(f)
        for val in email:
                writer.writerow([val])

