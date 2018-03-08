# Morgan shively
# Practical 1


import urllib.request

import re


# part 1
# just getting the contents from the web page

web_page = urllib.request.urlopen("http://www.soic.indiana.edu/undergraduate/courses/index.html")
contents = web_page.read().decode(errors="replace")
web_page.close()

#print(contents)

# part 2

print()

# a normale expression to gather the correct data


courses_data = re.findall('<a href=".+?(?=</a>)', contents, re.DOTALL)
data = ""

# here i was getting a string error when passing the data to the lists
# i assume its because course data is a list not a string
# so i just did a small for loop to make it into one long string

for i in courses_data:
    data += i

# I read ahead before startin this so I went ahead and did individual lists of the classes
# this made it easier for the last part of the problem
# these are all just normal expressions


#print(data)
csi_list = re.findall('(?<=CSCI">).+?(?=<a)', data, re.DOTALL)


#print(csi_list)

info_list = re.findall('(?<=INFO">).+?(?=<a)', data, re.DOTALL)
#print(info_list)


library_list = re.findall('(?<=ILS">).+?(?=<a)', data, re.DOTALL)

#print(library_list)

print("Computer Science Classes: ")
for course in csi_list:
    print(course)

print("Informatics Classes: ")
for course in info_list:
    print(course)

print("Libary Science Classes: ")
for course in library_list:
    print(course)

# here is the search function
# i wasnt sure what to use for the formatting
# i went ahead and used .title()

# these are just for loop and conditionals to print out the classes

user_class = input("Please enter a word to search for.")
print()

print("CSCI Undergraduate courses that match.")

for i in csi_list:
    if user_class.title() in i:
        print(i)
print()

print("INFO Undergraduate courses that match.")

for i in info_list:
    if user_class.title() in i:
        print(i)
print()

print("Library Science undergraduate courses that match.")
for i in library_list:
    if user_class.title() in i:
        print(i)
print()




