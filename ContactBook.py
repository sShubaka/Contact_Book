import os.path
import time

print("If you don't have a answer for the question asked, just type in none.")

def fileExistence():
    if os.path.exists("/Users/shubsharma/Desktop/Contact.txt"):
        pass
    else:
        file = open("/Users/shubsharma/Desktop/Contact.txt", "w")
        file.close()
fileExistence()

def mainfuc():
    Actual_DT = time.strftime("%Y-%m-%d %H:%M:%S")
    appendin = open("/Users/shubsharma/Desktop/Contact.txt", "a+")
    first_name = input("Type in the first name: ")
    last_name = input("Type in the last name: ")
    phone_number = input("Type in the phone number: ")
    email_address = input("Type in the email address: ")
    address = input("Please put the entire address: ")
    birthday = input("Type in the birthday: ")
    appendin.write("\n\n---------------------------\n\n" + "Contact Saved at- " + Actual_DT + "\nName: " + first_name + " " + last_name +
                   "\nPhone number- " + phone_number + "\nEmail address- " + email_address + "\nAddress- " + address + "\nBirthday- " + birthday)
    appendin.close()
    print("Contact saved!")
mainfuc()