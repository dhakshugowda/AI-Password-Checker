import re

def check_password(password):

    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Check special characters
    if re.search(r"[@#$%&*!]", password):
        score += 1

    # Check common passwords
    common = ["password", "12345678", "admin",
              "qwerty", "123456"]

    if password.lower() in common:
        return "Very Weak"

    # Display result
    if score <= 1:
        return "Very Weak"

    elif score == 2:
        return "Weak"

    elif score == 3:
        return "Medium"

    elif score == 4:
        return "Strong"

    else:
        return "Very Strong"


# Main program

print("================================")
print(" AI PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter your password: ")

result = check_password(password)

print("Password Strength:", result)

print("================================")