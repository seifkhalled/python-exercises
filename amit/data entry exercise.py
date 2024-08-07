import re

def check_email(email):
    # Regular expression pattern for validating an email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    return re.match(pattern, email)  is not None

def check_name(name):
    return all(part.isalpha() for part in name.split()) and len(name.split()) <= 2

def check_phone(phone):
  
    valid_prefixes = ('010', '011', '012')
    return phone.isnumeric() and len(phone) == 11 and phone[:3] in valid_prefixes

# def check_phone(phone):
#     # Check if phone number is numeric, has exactly 11 digits, and starts with '010', '011', or '012'
#     return phone.isnumeric() and len(phone) == 11 and (phone.startswith('010') or phone.startswith('011') or phone.startswith('012'))

# def check_email(email):
#     return email.endswith('@gmail.com')

def check_age(age):
    if(not age.isnumeric() and (age > 18) and (age < 130)):
        return False
    return True

def check_gender(gender):
    return gender in ["m", "f"]

first_name = "seif khaled"


phone = '01259197056'
email = 'sefifj@gmail.com'
gender = 'm'
age = "20"

# print(check_name(first_name))  
# print(check_name(last_name))   
# print(check_age(age))          
# print(check_email(email))      
# print(check_gender(gender))   
# Perform all checks
name_check_first_name = check_name(first_name)

phone_check = check_phone(phone)
email_check = check_email(email)
age_check = check_age(age)
gender_check = check_gender(gender)

if not name_check_first_name:
    print("Invalid first name. Please try again.")

elif not phone_check:
    print("Invalid phone number. Please try again.")
elif not email_check:
    print("Invalid email address. Please try again.")
elif not age_check:
    print("Invalid age. Please try again.")
elif not gender_check:
    print("Invalid gender. Please try again.")
else:
    with open('dataentry.txt', 'w') as f:
        f.write(f"First Name: {first_name}\n")
        
        f.write(f"Phone: {phone}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Gender: {gender}\n")

    print("All data is valid. Results have been written to 'dataentry.txt'.")
