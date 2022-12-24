#!/usr/bin/python3
# coding:UTF-8

# -------------------------------------------------------------------------------------
#          PYTHON SCRIPT FILE FOR THE PRELIMINARY ANALYSIS OF WEB APPLICATIONS
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
   print("Use the command python3 auto_run.py pentestpeople.co.uk...")
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
   
def stage1(host):
   print(colored("[+] Stage 1 - Obtaining the URL's...", colour1))
   os.system("python3 waymore.py -i " + host + " -mode U --no-subs") 
   return
   
def stage2(host):
   print(colored("[+] Stage 2 - Sorting the URL's...", colour1))
   os.system("sort -u ./results/" + host + "./results/sorted.txt")
   return
   
def stage3(host):
   print(colored("[+] Stage 3 - Checkign for CVE's...", colour1))
   os.system("nuclei --ut && nuclei -l ./results/sorted.txt --tags CVE --rate-limit 4 -header 'Authentication: Hackerone")
   return      
   
# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : MAIN PROGRAM.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
banner()
stage1(host)
stage2(host)
stage3(host)


