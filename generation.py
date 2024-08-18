#input year function
birth_year = int(input("What is your year of birth? "))

#determine their year of birth
if 1946 <= birth_year <= 1964:
    print("You are a baby boomer")
elif 1965 <= birth_year <= 1980:
    print("You are a member of Generation X")
elif 1981 <= birth_year <= 1996:
    print("You are a millenial")
elif 1997<= birth_year <= 2012:
    print("You are a member of Generation Z")
elif 2013 <= birth_year:
    print("You are a member of Generation Alpha")
else:
    print("Error. Please enter a four-digit year, 1946 or later.")