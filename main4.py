# Leap year or common year calculator

year = int(input("Enter the year: "))
if year % 4 == 0 and year % 100 != 0:
    print(f"The year {year} is a leap year.")
elif year % 400 == 0:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is a common year.")
