# Example 1: Access control
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("You are underage")

#==========================================================
# Example 2: Movie eligibility
age = 16
with_parent = True
if age >= 18:
    print("Allowed to watch")
else:
    if with_parent:
        print("Allowed with parental guidance")
    else:
        print("Not allowed")

#==========================================================
# Example 3: Login simulation
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")
