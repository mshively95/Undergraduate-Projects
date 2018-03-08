import xml.etree.ElementTree as ET

#print(root)
root = ET.parse(source="library.xml")

elements = root.iter("book")


# 1
# just making a list of all the books in the xml
# individually seeing if the book id matches the arugment
# we do this by checking the attrib id
# if there is a match we print the given info about the book


def display_book(book_id):
    #books = root.findall("catalog")
    books = root.iter("book")
    #print(books)
    for book in books:
        if book_id == book.attrib["id"]:
            print("This book was written by", book.find("author").text, "\n" "the book is called", book.find("title").text, "\n", "the genre of this book is",
                  book.find("genre").text," this book is worth",
                  book.find("price").text, "this book was published on",
                  book.find("publish_date").text, "a brief description of this book:", book.find("description").text)


#2

# was able to find the books printed in december
# had trouble also finding the genres
# this prints out all the dates of the books


books = root.findall("book")
dates = [(date.find("publish_date").text).split("-") for date in books]
##genres = [(genre.find("genre").text) for genre in books]
##print(genres)


for date in dates:
    if int(date[1]) == 12:
        

#3
# here just did a list comprehension for the genres
# then used set to get rid of duplicates

genres = [(genre.find("genre").text) for genre in books]
print (set(genres))








# main

display_book("bk101")
                  
    
