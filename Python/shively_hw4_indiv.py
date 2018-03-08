# Morgan Shively
# Homework 4


# 1

#%b is the placeholder that will display the month as a three letter abbreviation


# 2
# use dictreader to get the file conetents
# split the dates at the slashes
# type cast them into integers
# format the numbers into dates by the corresponding index
# use stfrtime to see if they are fridays
# print the item name

# tried getting this into a list comprehension but couldn't figure it out

# this compiles all the same



import csv

import datetime
data = open("ShopRecords.csv", "r")

sales = list(csv.DictReader(data))

for entry in sales:
    sold = entry["Date"].split("/")
    date = datetime.date(int(sold[2]), int(sold[0]), int(sold[1]))
    if date.strftime("%A") == "Friday":
        print (entry["Item"])

    
       
                
       
