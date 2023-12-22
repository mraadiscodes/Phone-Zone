# Coded By mraadiscodes
# github: https://github.com/mraadiscodes
# this is a simple phone number detais finder tool written in python.

# To create a typing effect I have used time mode.
# To find phone number details, I have used the PhoneNumbers model and imported the timezone, geocoder, carrier functions from it.
# I used the pyfiglet model to create a simple banner for the tool.


import time
import phonenumbers as pn
from phonenumbers import timezone, geocoder, carrier
import pyfiglet

# colors class
class colors():
    red = '\033[0;31m'
    green = '\033[0;34m'
    cyan = '\033[0;36m'
    yellow = '\033[0;33m'
    magenta = '\033[0;35m'
    
# pyfiglet banner
bn = pyfiglet.figlet_format("PHONE-Zone")
print(colors.green + bn)
    
# typing effect function
def print_typing(text):
    for type in text:
        print(type, end='', flush=True)
        time.sleep(0.04)      
    print()
    
# about tool
print_typing(colors.cyan + "About this tool:")
print_typing(colors.green + f"Introducing {colors.magenta}PhoneZone {colors.green}your go-to solution for effortlessly uncovering {colors.red}phone number details!\n")

# inputs form user in a infinity while loop
while True:
    while True:
        phon = input(colors.cyan + "[+] Enter Your Target Phone Number (eg. 9988665544): ")
        if len(phon) != 10 or not phon.isdigit():
            print_typing(colors.red + "\n[!] Invalid Phone Number!!! Please enter a valid 10-digit numeric phone number.\n")
        else:
            break
        
    c_code = input(colors.green + "[+] Enter Country Code (eg. +91, +1): ")
    ful_phon = f"{c_code}{phon}"
        
    # back-end codes 
    phone_n = pn.parse(ful_phon)
    tz = timezone.time_zones_for_number(phone_n)
    crr = carrier.name_for_number(phone_n, 'en')
    geo = geocoder.description_for_number(phone_n, 'en')
    
    # printing the details of phone number
        
    print(f"\n{colors.yellow}[✓] Phone Number: {ful_phon}\n[✓] Timezone: {tz}\n[✓] Carrier: {crr}\n{colors.cyan}[✓] Geographical Area: {geo}\n")
    user_b = input("[+] Press Enter to run again or q to exit: ")
    if user_b == "":
        continue
    elif user_b == "q":
        print_typing("\nThanks for using :)")
        break
        
# ended!!!