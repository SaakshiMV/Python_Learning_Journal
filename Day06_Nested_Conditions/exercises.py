# Exercise 1
# Check student eligibility for exam
print("======================================================")
print("\nCheck student eligibility for exam: ")
attendance = 80
fees_paid = True

if attendance >= 75:
    if fees_paid:
        print("Eligible for exam")
    else:
        print("Fees not paid")
else:
    print("Attendance too low")

#=======================================================
# Exercise 2
# ATM withdrawal simulation
print("======================================================")
print("\nATM withdrawal simulation: ")
balance = 1000
withdraw = 500

if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")


#=======================================================
# Exercise 3
# Login system
print("======================================================")
print("\nLogin system: ")
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")


#=======================================================
# Exercise 4
# Age and citizenship check
print("======================================================")
print("\nAge and citizenship check: ")
age = int(input("Enter your age: "))
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Underage")
