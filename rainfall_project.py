total_rainfall = 0

list_of_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Set", "Oct", "Nov", "Dec"]

year = int(input("Enter the number of years: "))

for years in range(year):
    print(f"Year {years + 1}")
    for month in range(12):
        month_data = (float(input(f"Enter the rainfall amount for {list_of_months[month]}: ")))
        total_rainfall += month_data

average_rainfall = total_rainfall / (int(year)*12)

print("For 12 Months: ")
print(f"Total rainfall: {total_rainfall} inches")
print(f"Average monthly rainfall: {average_rainfall}")