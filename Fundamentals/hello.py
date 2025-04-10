# Ask User for their name
name = input("Whats your name?").strip().title()

#Split users name into first and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}") 
