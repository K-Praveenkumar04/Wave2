#MonthToDays
month = input("Enter a month: ")
numofdays = 31
if month == "April" or month == "June" or month == "September" or month == "November":
    numofdays = 30
elif month == "February":
    numofdays = "28 or 29"
else:
    numofdays = 31
print (str(month) + " has " + str(numofdays) + " days")