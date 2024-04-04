# Hello! welcome to Day 2 of my 30-day Python challenge taught to me by ChatGPT!
# Today's focus is on reinforcing Python programming concepts, understanding Python's role in cybersecurity, and exploring relevant tools and libraries. 


# Review Python Functions:
# Functions in Python allow you to encapsulate reusable code blocks.
# Review function syntax, parameters, return statements, and how to call functions.

# Here's an example
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print(result)  # Output: 15


# Learn about Modules and Packages:
# Modules are Python files containing functions, classes, and variables that can be imported into other Python scripts.
# Packages are directories containing multiple modules and an __init__.py file.

# Example of using a module:
# ex: Create a module named my_module.py
# Contents of my_module.py
def greet(name):
    print(f"Hello, {name}!")

# In another script, import the module
import my_module
my_module.greet("Alice")


# Cybersecurity Tools with Python:
# Scapy: Scapy is a powerful Python library that allows you to create, manipulate, and analyze network packets. It's commonly used for tasks like packet sniffing, network scanning, and crafting custom network tools.
# Example of sending a custom ICMP packet using Scapy
from scapy.all import *

packet = IP(dst="www.example.com")/ICMP()
response = sr1(packet)
response.show()

# Nmap: Nmap is a popular network scanning tool that can be used via Python's python-nmap library. It allows you to discover hosts, scan open ports, and gather information about network services.
# Example of using python-nmap to scan for open ports
import nmap

nm = nmap.PortScanner()
nm.scan('192.168.1.1', '22-443')
for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        ports = nm[host][proto].keys()
        for port in ports:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

# Requests: The Requests library simplifies HTTP requests in Python, making it useful for web interactions in cybersecurity tasks such as web scraping, API calls, and web vulnerability testing.
# Example of making a GET request using Requests
import requests

response = requests.get('https://www.example.com')
print(response.status_code)
print(response.text)

