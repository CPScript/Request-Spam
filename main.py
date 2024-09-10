import requests
import random
import time
import os
from os import system
import platform 

def clear(): # clear function for clearing the terminal if you reuse the tool or after you install dependacys, for a nice sleek design
    system = platform.system().lower()

    if system == 'windows':
        _ = os.system('cls')
    elif system == 'linux' or system == 'darwin':
        _ = os.system('clear')
    elif system == 'android':
        _ = subprocess.run(['termux-exec', 'sh', '-c', 'clear'], check=False)
    else:
        print(f"{system} Is an Unsupported platform, skipping")

# Call
print("Checking if Your Platform is Supported!")
print(f"You are using '{system}'")
clear() # clear

def main():

    # banner
    print("""
=======> Anti-Grabify <========
Description:
Easily flood a Grabify tracker
or link with real looking requests
to throw off an attacker and make
it harder or them to track you!
(undetectable bot)

How to use:
1. Type the link
(This can be any link so be responsible)

2. Enter number of requests
(How many requests to send.)

3. Time delay (seconds)
(Recommended to use '0.5', anything below will get blocked)
=======> By: CPScript <========

┌─[Anti-Grabify] - [User-Input]""")

    # user input
    grabify_link = input("|─[link]──> ")
    num_requests = int(input("|─[requests]──> "))
    delay_between_requests = float(input("└─[delay]──> "))

    # user agents
    user_agents = [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 11; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0",
        "Mozilla/5.0 (Android 11; Mobile; LG-M255) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36"
    ]

    # IP addresses | This can be changes to the users liking
    ip_addresses = [
        "192.168.1.1",
        "172.16.254.1",
        "10.0.0.1",
        "8.8.8.8",
        "4.4.4.4",
        "1.1.1.1",
        "2.2.2.2",
        "3.3.3.3",
        "5.5.5.5",
        "6.6.6.6",
        "7.7.7.7",
        "8.8.4.4",
        "9.9.9.9",
        "10.10.10.10",
        "11.11.11.11",
        "12.12.12.12",
        "13.13.13.13",
        "14.14.14.14",
        "15.15.15.15",
        "16.16.16.16",
        "17.17.17.17",
        "18.18.18.18",
        "19.19.19.19",
    ]

    # rotate IP addresses and user agents
    def rotate_ip_and_ua():
        ip_address = random.choice(ip_addresses)
        user_agent = random.choice(user_agents)
        return ip_address, user_agent

    for i in range(num_requests):
        # Rotate through IP addresses and user agents
        ip_address, user_agent = rotate_ip_and_ua()
        # Set headers
        headers = {
            "User-Agent": user_agent,
            "X-Forwarded-For": ip_address
        }
        # Send request(s)
        try:
            response = requests.get(grabify_link, headers=headers)
            print(f"Request '{i+1}': User-Agent '{user_agent}' and from '{ip_address}'")
            # delay
            time.sleep(delay_between_requests)
        except requests.exceptions.RequestException as e:
            print(f"Error message: {e}")
            # Wait before retrying if error
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
