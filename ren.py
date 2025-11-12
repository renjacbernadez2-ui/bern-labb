# Simple Login System in Python

# Step 1: Store username and password
USERNAME = "admin"
PASSWORD = "12345"

# Step 2: Ask user for input
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

# Step 3: Check credentials
if entered_username == USERNAME and entered_password == PASSWORD:
    print(" Login successful! Welcome,", USERNAME) 
else:
    print(" Invalid username or password. Try again.") 
