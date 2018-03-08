import xml.etree.ElementTree as ET

#print(root)
root = ET.parse(source="library.xml")

elements = root.iter("book")




def display_book(book_id):
    #books = root.findall("catalog")
    books = root.iter("book")
    print(books)
    for book in books:
        if book_id == book.attrib["id"]:
            print("This book was written by", book.find("author").text, "\n" "the book is called", book.find("title").text, "\n", book.find("genre").text, book.find("price").text, book.find("publish_date").text, book.find("description").text)


#2

books = root.findall("book")
##for date in books:
##    print(date.find("publish_date").text)
dates = [(date.find("publish_date").text).split("-") for date in books]
print(dates)




for date in elements:
    if int(date[1]) == 10 and date.find("genre").text == "Computer":
        print(date.find("title").text)
        








# main

display_book("bk101")
                  
    

