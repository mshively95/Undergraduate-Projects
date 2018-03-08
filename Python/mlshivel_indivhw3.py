# morgan shively
# homework 3
# i211

# 1
# here you can find all the python documentation
# at least, this is the one I use
# https://docs.python.org/3/library/index.html



#2
# I did a list comprehension for the problem
# get the input from the user for the directory
# make a list of the contents inside the directory
# us os.replace to change the string "draft" to "final" for all the instances of files that containt the string "draft"
# then append those files to the list called files




# 3

import os

def word_change():
    user_input = input("Please enter a directory.")
    contents = os.listdir(user_input)

    files = [file.replace("draft", "final") for file in contents if "draft" in file]

    print(files)



# main
word_change()




