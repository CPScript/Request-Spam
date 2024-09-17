import requests
import random
import time
import os
from os import system
import platform 

def clear(): 
    system = platform.system().lower()

    if system == 'windows':
        _ = os.system('cls')
    elif system == 'linux' or system == 'darwin':
        _ = os.system('clear')
    elif system == 'android':
        _ = subprocess.run(['termux-exec', 'sh', '-c', 'clear'], check=False)
    else:
        print(f"{system} Is an Unsupported platform, skipping")

print("Checking if Your Platform is Supported!")
print(f"You are using '{system}'")
clear() 

def main():

    print("""
=======> Request-Flood <========
Description:
Easily flood a IP-tracker
or URL with real looking requests
to throw off an attacker and make
it harder or them to track your 
original host ip. (undetectable bot)

How to use:
1. Type the link
(This can be any link so be responsible)

2. Enter number of requests
(How many requests to send.)

3. Time delay (seconds)
(Recommended to use '0.5', anything below will get blocked)
=======> By: CPScript <========

┌─[Request-Flood] - [User-Input]""")

    grabify_link = input("|─[link]──> ")
    num_requests = int(input("|─[requests]──> "))
    delay_between_requests = float(input("└─[delay]──> "))

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 11; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0",
        "Mozilla/5.0 (Android 11; Mobile; LG-M255) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36"
    ]

    ip_addresses = [
        "24.48.128.53",
        "50.116.1.121",
        "71.179.23.134",
        "98.210.174.122",
        "104.223.51.189",
        "108.61.122.131",
        "142.93.137.145",
        "157.245.73.123",
        "172.96.189.153",
        "192.241.143.123"
        "192.168.1.1",
        "172.16.254.1",
        "10.0.0.1",
        "8.8.8.8",
        "4.4.4.4",
        "1.1.1.1",
        "2.2.2.2",
        "3.3.3.3",
        "10.10.10.10",
    ]

    def rotate_ip_and_ua():
        ip_address = random.choice(ip_addresses)
        user_agent = random.choice(user_agents)
        return ip_address, user_agent

    for i in range(num_requests):
        ip_address, user_agent = rotate_ip_and_ua()
        headers = {
            "User-Agent": user_agent,
            "X-Forwarded-For": ip_address
        }
        try:
            response = requests.get(grabify_link, headers=headers)
            print(f"Request '{i+1}': User-Agent '{user_agent}' and from '{ip_address}'")
            time.sleep(delay_between_requests)
        except requests.exceptions.RequestException as e:
            print(f"Error message: {e}")
            time.sleep(delay_between_requests)
            continue

    print("""
======> Done <======
You are able to see the requests sent.
If there are no errors then they should all appear

Have a good day!
""")

clear()
main()
