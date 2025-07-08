# IP Toggler

A Python script to rotate your IP address by switching between multiple proxy servers every set interval. Designed to enhance privacy by masking your IP during scripted requests.

## Features

- Supports HTTP, HTTPS, and SOCKS5 proxies
- Rotates proxies automatically every 10 minutes (configurable)
- Fetches and displays your current IP address and geolocation info after each switch
- Handles SSL certificate verification issues with proxy servers
- Logs useful connection info to the console

## Requirements

- Python 3.6 or higher
- `requests` package with SOCKS support

Install dependencies with:

```bash
pip install requests[socks]
