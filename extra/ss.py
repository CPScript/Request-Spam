import requests
import random
import time
import os
import platform

def clear():
    platform_name = platform.system().lower()
    if platform_name == 'windows':
        os.system('cls')
    elif platform_name == 'linux' or platform_name == 'darwin':
        os.system('clear')
    elif platform_name == 'android':
        os.system('termux-exec sh -c clear')
    else:
        print(f"{platform_name} is an unsupported platform, skipping")

def print_banner():
    print("""
=======> Request-Flood <========
Description:

(This is a updated version with a more comlex way of generating IP addresses, this generation proccess can make it slow so i introduced extra workers)

Easily flood a IP tracker
or URL with real looking requests
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

┌─[Request-Flood] - [User-Input]""")

def get_user_input():
    grabify_link = input("|─[link]──> ")
    while not grabify_link.startswith('http'):
        print("Invalid URL. Please enter a valid URL.")
        print("""
        ┌─[Anti-Grabify] - [User-Input]""")
        grabify_link = input("|─[link]──> ")
    
    num_requests = int(input("|─[requests]──> "))
    while num_requests <= 0:
        print("Invalid number of requests. Please enter a positive integer.")
        num_requests = int(input("|─[requests]──> "))
    
    delay_between_requests = float(input("└─[delay]──> "))
    while delay_between_requests < 0:
        print("Invalid delay. Please enter a non-negative float.")
        delay_between_requests = float(input("└─[delay]──> "))
    
    return grabify_link, num_requests, delay_between_requests

def generate_random_ip():
    octet1 = random.randint(1, 254)
    octet2 = random.randint(1, 254)
    octet3 = random.randint(1, 254)
    octet4 = random.randint(1, 254)
    return f"{octet1}.{octet2}.{octet3}.{octet4}"

def send_requests(grabify_link, num_requests, delay_between_requests, user_agents):
    for i in range(num_requests):
        ip_address = generate_random_ip()
        user_agent = random.choice(user_agents)
        headers = {
            "User-Agent": user_agent,
            "X-Forwarded-For": ip_address,
            "Referer": f"https://{generate_random_ip()}"
        }
        try:
            response = requests.get(grabify_link, headers=headers)
            print(f"Request '{i+1}': User-Agent '{user_agent}' and from '{ip_address}'")
            time.sleep(delay_between_requests)
        except requests.exceptions.RequestException as e:
            print(f"Error message: {e}")
            time.sleep(delay_between_requests)
            continue

def print_done_message():
    print("""
======> Done <======
You are able to see the requests sent.
If there are no errors then they should all appear

Have a good day!
""")

def main():
    print("Checking if Your Platform is Supported!")
    print(f"You are using '{platform.system()}'")
    clear()
    
    print_banner()
    grabify_link, num_requests, delay_between_requests = get_user_input()
    
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
    
    send_requests(grabify_link, num_requests, delay_between_requests, user_agents)
    
    print_done_message()

if __name__ == "__main__":
    main()
