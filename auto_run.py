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

   
def parked(host):
   page = requests.get("https://" + host)
   os.system("echo " + str(page.headers) + " > securityheaders3.txt")
   return
   
def banner():
   print(colored("Pentest People - AUTORUN.", colour5))
   print("Target:", host)   
   print("- - - - - - - - - - - - - - - - - - - - - - -")   
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
print(colored("[+] Identifying " + host + " IP addresses...", colour1))
os.system("dig +short " + host + " > digshortip.txt")
print(colored("[*] Manually check the IP addresses shown below for direct IP access...", colour1))
os.system("cat digshortip.txt")
print(colored("[+] Performing DNS enumeration...", colour1))
targetIP = (linecache.getline("digshortip.txt", 1).rstrip("\n"))
parts = targetIP.split(".")
if len(parts) == 4:
   os.system("whois -I " + targetIP + " > whois.txt")
else:
   targetIP = (linecache.getline("digshortip.txt", 2).rstrip("\n"))
   os.system("whois -I " + targetIP + " > whois.txt")   
os.system("dig +short TXT " + host + " > digtxt.txt")
os.system("dig SOA " + host + " > digsoa.txt")
print(colored("[+] Performing TCP scan", colour1))
os.system("nmap -sVC -T4 -p- -oN tcp.txt " + host + " > null.txt")
print(colored("[+] Performing UDP scan...", colour1))
os.system("nmap -sUV --top-ports 200 -oN udp_top2000.txt " + host + " > null.txt")
print(colored("[+] Performing BIOS scan...", colour1))
os.system("nbtscan -rv " + targetIP + " > bios.txt")
print(colored("[+] Performing slow loris scan...", colour1))
os.system("nmap -p 80,443 --script=http-slowloris-check -oN slowloris.txt " + host + " > null.txt")
print(colored("[+] Performing load balancer scan...", colour1))
os.system("lbd https://" + host + " > lbd.txt")
print(colored("[+] Performing WAF scan...", colour1))
os.system("wafw00f -a https://" + host + " > wafw00f.txt")
print(colored("[+] Performing enumeration scan...", colour1))
os.system("nmap -sVC -p 80,443 --script=http-enum -oN enumeration.txt " + host + " > null.txt")
print(colored("[+] Performing sitemap scan...", colour1))
os.system("nmap -Pn --script=http-sitemap-generator -oN sitemap.txt " + host + " > null.txt")
print(colored("[+] Performing vuln #1 scan...", colour1))
os.system("nmap -p 80,443 --script=vuln -oN vuln1.txt " + host + " > null.txt")
print(colored("[+] Performing vuln #2 scan...", colour1))
os.system("nmap -p 80,443 --script=vulners -oN vuln2.txt " + host + " > null.txt")
print(colored("[+] Performing unsafe escaping scan...", colour1))
os.system("nmap -p 80,443 --script=http-unsafe-output-escaping -oN unsafe.txt " + host + " > null.txt")
print(colored("[+] Performing SQL injection scan...", colour1))
os.system("nmap -p 80,443 --script=http-sql-injection -oN sqlinject.txt " + host + " > null.txt")
print(colored("[+] Performing a crytographic scan...", colour1))
os.system("testssl --full https://" + host + " | tee testssl.txt > null.txt")
print(colored("[+] Performing client re-negotiation scan...", colour1))
os.system("testssl -R https://" + host + " | tee renegotiation.txt > null.txt")
print(colored("[+] Performing SSL scan...", colour1))
os.system("sslscan -v https://" + host + " | tee sslscan.txt > null.txt")
print("Scanning completed...")





