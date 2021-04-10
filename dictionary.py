# Dictionay is key value pair, Just Like JSON
monthConversions = {
        0 : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "July" : "July",
    "Aug" : "Auguest",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}
# All Keys Must Be Unique

print(monthConversions)

# get specific value
print(monthConversions['Dec'])

# get
print(monthConversions.get("Dec"))

# if key not found, we can specify default value
print(monthConversions.get("LOB", "Not A Valid Key"))
