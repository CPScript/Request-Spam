# Request-Spam
Easily flood a Ip-tracker or URL with real-looking requests to throw off an attacker and make it harder for them to track you!

---

## How to Use:
* Type the link (This can be any link, so be responsible)
* Enter the number of requests (How many requests to send)
* Time delay (seconds) (Recommended to use '0.5', anything below will get blocked)

## Features:
* Rotates through a list of user agents and IP addresses to simulate real requests
* Sends GET requests to the specified link with the chosen user agent and IP address
* Waits for the specified delay between requests
* Handles errors and retries if necessary

## Requirements:
* GIT (must clone the repo)
* Python 3.x (language)
`requests` library (install with `pip install requests`)

## Usage:
* Install the `python` programming language
* Install `git` - `pkg install git` or `apt install git`, if these dont work try to install it using python `pip install git`
* Clone this repo - `git clone https://github.com/CPScript/Request-Spam`
* Get into the repo's folder - `cd Request-Spam` or if you saved it somewhere type `cd <dir where its stored>/Request-Spam`
* Execute the script - `python spam.py`
* Follow the prompts to enter the link, number of requests, and time delay


> Note: This script is for educational purposes only. Use responsibly and do not use to harm or track others without their consent.
> Author: CPScript
> License: MIT License (see LICENSE file for details)
