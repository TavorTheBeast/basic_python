import datetime

# Accept user input
date_str = input("Enter a date in dd/mm/yyyy format: ")

# Convert string to datetime object
date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')

# Get day of the week as a string
day_of_week = date_obj.strftime("%A")

# Print result
print("The day of the week for", date_str, "is", day_of_week)
