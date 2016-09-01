import csv
import collections

f = open('faculty.csv')
csv_f = csv.reader(f)

degree = []
title = []
email = []

for row in csv_f:
	degree.append(row[1])
	title.append(row[2])
	email.append(row[3])

#deleting the titles of the columns from the lists
degree = degree[1::]
title = title[1::]
email = email[1::]

#Noticed that there are several ways of spelling Ph.d. Made the spelling of Ph.d. uniform throughout the degree list. Also separated all the multiple degree elements and made them unique
unique_degree = []
for i in degree:
    new = i.replace('.', '')
    separate = new.split()
    for j in separate:
	unique_degree.append(j)

#Count the frequency of each degree
counter = collections.Counter(unique_degree)

#Noticed that there was a spelling error in the dataset. Replaced 'is' with 'of'.
fixed_title = []
for i in title:
	new = i.replace(' is ', ' of ')
	fixed_title.append(new)

#Count the frequency of each title
counter2 = collections.Counter(fixed_title)

#Question1
print "There are ", len(set(unique_degree))," different degrees. The frequences are given by this list "
print counter

#Question2
print "There are ", len( set(fixed_title))," different titles. The frequences are given by this list "
print counter2

#Question3
print email

#Question 4
email_domain = []
for i in email:
	j = i.index("@")
	email_domain.append(i[j::])

counter3 = collections.Counter(email_domain)

print "The amount of different email domains is ", len(set(email_domain)), "."
print "The unique email domains are: ", list(set(email_domain))
