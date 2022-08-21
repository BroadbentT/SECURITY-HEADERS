#!/usr/bin/python3
# coding:UTF-8

# -------------------------------------------------------------------------------------
#          PYTHON SCRIPT FILE FOR THE PRELIMINARY ANALYSIS OF JWT TOKENS
#                       BY TERENCE BROADBENT BSc CYBER SECURITY
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                               
# Details : Load required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import requests
import linecache
import ipaddress 

from termcolor import colored # pip3 install termcolor  

colour1 = 'green'
colour2 = 'yellow'
colour3 = 'blue'
colour4 = 'red'
colour5 = 'cyan'

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                               
# Details : Conduct simple and routine tests on any user supplied arguements.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if os.geteuid() != 0:
   print("\nPlease run this python script as root...")
   exit(True)

if len(sys.argv) < 2:
   print("Use the command python3 jwt_token.py host")
   exit()
host = sys.argv[1]

os.system("xdotool key Alt+Shift+S; xdotool type 'AUTORUN'; xdotool key Return")
    
# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Create functional subroutine calls from main.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

def banner():
   print(colored("Pentest People - JWT TOKEN ANALYZER.", colour5))
   print("Domain:", host)   
   print("- - - - - - - - - - - - - - - - - - - - - - -")   
   return
   
def next(message):
   if message != "":
      key_data = input(message + " Y/N :")
   else:
      key_data = input("Y/N :")
   key_data = key_data[:1]
   key_data = key_data.upper()
   if key_data== "Y":
      return 1
   else:
      return 0
   
# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : MAIN PROGRAM.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
banner()
print("[i] Instructions: Identify a test page where a clear difference in response can be seen if the JWT token is tampered with, such as an account page or an authenticated page that user/organisation specific data is displayed...")
next("Completed")
print("[i] Instructions: Now check the the identified request is replayable within your burp console...")
next("Completed")

print(colored("\n\nREQUIRED TEST", colour2))
print("[*] Now remove the token and replay the request, did it still work?...")

quickCheck = 0
quickCheck = next("")
if quickCheck == 1:
   print(colored("[-] This means the JWT token is unlikely to facilitate authentication...",colour4))
else:
   print(colored("[+] This means the JWT token is likely to faciliate authentiction...", colour1))

print(colored("\n\nCHECKED TEST", colour2))
print("[*] Lets see if the token is checked, delete the last few bytes of the token and replay the request. Did it still work?")

quickCheck = 0
quickCheck = next("")
if quickCheck == 1:
   print(colored("[-] Same result? this means that the token is not checked! If this is the case tamper with the parameter and see what results can be obtained...", colour4))
else:
   print(colored("[+] If the page returned an error message, or displayed a different result to the orginal result then this means that the signature is checked...", colour1))

print("\n[i] Instructions: Resend the token, multiple times, intermittently with no token, or a token with a invalid signature...")

quickCheck = 0
quickCheck = next("Completed ")

print(colored("\n\nPERSISTENT TEST", colour2))
print("[*] Now replay the orginal token, is the token invalidated?...")
   
quickCheck = 0
quickCheck = next("")
if quickCheck == 1:
   print(colored("[+] If the token is invalidated, this is normal behavour and means that token refreshing is required..", colour1))
else:
   print(colored("[-] Mmm looks like the token is static...", colour4))
   print("[*] How long is the token expiry set to? check the 'exp' claim...")

print("\n[*] Grab a new token if required. Now logout of the application and replay the token, did the token still work?...")

quickCheck = 0
quickCheck = next("")
if quickCheck == 1:
    print(colored("[-] It looks like the JWT token is persistent...", colour4))
else:
    print(colored("[+] Good, that's correct the token should not work...", colour1))
        
print(colored("\n\nORIGIN TEST", colour2))
print("[*] Now log back in, did the JWT token first appear on the server side?...")
quickCheck = 0
quickCheck = next("")
if quickCheck == 0:
   print(colored("[-] Tokens should always appear on server side first, check the code for secret signature...", colour4))
else:
   print(colored("[+] Great tokens should always apprear server side first...", colour1))
   
print(colored("\n\nCLAIMS TEST", colour2))


   
   




#os.system
