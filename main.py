# Password Strength Checker

password = input("Enter your password: ")

length_ok = len(password) >= 8
has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

if length_ok and has_digit and has_upper:
    strength = "Strong"
elif length_ok and (has_digit or has_upper):
    strength = "Medium"
else:
    strength = "Weak"

print("Password Strength:", strength)
