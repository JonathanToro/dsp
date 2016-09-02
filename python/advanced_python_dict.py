import csv

f = open('faculty.csv')
csv_f = csv.reader(f)

name = []
degree = []
title = []
email = []

for row in csv_f:
        name.append(row[0])
        degree.append(row[1])
        title.append(row[2])
        email.append(row[3])

#Getting rid of the title of each column from the lists
name = name [1::]
degree = degree[1::]
title = title[1::]
email = email[1::]

#Get the last names of the professors
last_name = []
for i in name:
        n = i.rfind(" ")
        last_name.append(i[n+1::])

#fixing the title names to the desired format
fixed_title = []
for i in title:
        n = i.index("Professor")
        fixed_title.append(i[:n+9])

#Question 6
faculty_dict = {z[0]:list(z[1:]) for z in zip(last_name,degree, title, email)}
print faculty_dict

#getting the first names of the professors
first_name = []
for i in name:
        n = i.rfind(" ")
        first_name.append(i[:n])

##put the first name and last name into a set and into a list
full_name = []
for a,b in zip(first_name,last_name):
        full_name.append((a,b))

#Question 7
professor_dict = {z[0]:list(z[1:]) for z in zip(full_name, degree,fixed_title, email)}
print professor_dict

# Question 8
for x in sorted(professor_dict.keys(), key =lambda x: x[1]):
        print x, professor_dict[x]
