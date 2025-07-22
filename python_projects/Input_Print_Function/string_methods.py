# name = input("What's your name ? ")

name = input("What's your name ? ").strip().title()

name = name.strip() #remove extra space or characters if any

name = name.upper()  #upper case

name = name.lower()   #lower case

name = name.capitalize()   #capitalize the first character of the whole string

name = name.title()    #title format for each word of the string will be capital

name = name.strip().title()  #here we are doing applying two methods on single variable

print(f"Hello {name}")

#split user's name in to first name and last name

first, last = name.split(" ")

print(f"Hello {first}")


