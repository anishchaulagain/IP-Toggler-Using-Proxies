#!/usr/bin/python3
"""
This script rotates your IP address every 10 minutes using proxies
from different regions of the USA to enhance privacy.
"""

import requests
import time
import random

# List of high-anonymity USA-based proxies
PROXIES = [
    {"http": "socks5h://192.252.215.2:4145", "https": "socks5h://192.252.215.2:4145"},  # Atlanta, GA
    {"http": "http://4.156.78.45:80", "https": "http://4.156.78.45:80"},  # Virginia
    {"http": "http://152.26.229.52:9443", "https": "http://152.26.229.52:9443"},  # North Carolina
    {"http": "http://96.70.186.221:80", "https": "http://96.70.186.221:80"},  # Maryland
    {"http": "http://154.16.146.45:80", "https": "http://154.16.146.45:80"},  # New York
]

ROTATION_INTERVAL = 600  # 600 seconds = 10 minutes

def get_random_proxy():
    return random.choice(PROXIES)

def fetch_ip_and_location(proxy):
    try:
        # Get external IP
        ip_response = requests.get('https://api.ipify.org?format=json', proxies=proxy, timeout=10, verify=False)
        ip = ip_response.json().get("ip", "N/A")

        # Get location from IP (using ipinfo.io)
        location_response = requests.get(f'https://ipinfo.io/{ip}/json', timeout=10, verify=False)
        location_data = location_response.json()

        print(f"✅ IP: {ip}")
        print(f"🌍 Location: {location_data.get('city')}, {location_data.get('region')} ({location_data.get('country')})")
        print(f"🏢 ISP: {location_data.get('org')}")
        print("-" * 40)

    except Exception as e:
        print(f"❌ Failed to fetch IP/location: {e}")
        print("-" * 40)

def rotate_proxy():
    proxy = get_random_proxy()
    print(f"🔁 Switching to proxy: {proxy}")
    fetch_ip_and_location(proxy)

def main():
    print("🗺️ Starting IP rotation across the USA...")
    while True:
        rotate_proxy()
        time.sleep(ROTATION_INTERVAL)

if __name__ == "__main__":
    main()
