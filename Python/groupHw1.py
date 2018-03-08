import csv, datetime

data = open("Indiana_Storms.csv", "r")
storms = csv.DictReader(data)

def storm_by_event(event):   
    
    for entry in storms:
        if entry["EVENT_TYPE"] == event:
            year = entry["BEGIN_YEARMONTH"]
            year = year[0:4]
            month = entry["BEGIN_YEARMONTH"]
            month = month[4:6]
            day = entry["BEGIN_DAY"]
            if len(day) != 2:
                day = "0" + day
                
            date = datetime.date(int(year), int(month), int(day))
            date = date.strftime("%m/%d/%y")

            print("A", event, "happened on", date, "and happened in", entry["CZ_NAME"])
            
def storm_by_date(user_date):
    year, month, day = str(user_date).split("-")
    for entry in storms:
        if year == entry["YEAR"] and day == entry["BEGIN_DAY"] and month == entry["BEGIN_YEARMONTH"][4:6]:
            print(entry["EVENT_TYPE"], "happened on", user_date, "and happened in", entry["CZ_NAME"], "county.")

            

user_choice = input("would you like to search by event or date?")
if user_choice == "event":
    event_choice = input("What event would you like to search for?")
    storm_by_event(event_choice)
    
    
elif user_choice == "date":
    date_choice = input("Please input a date. ex (YYYY-MM-DD)")date
    storm_by_date(date_choice)
    
else:
    print("That wasn't a valid choice.")

          
#main
#user_date = datetime.date(2015, 5, 15)
