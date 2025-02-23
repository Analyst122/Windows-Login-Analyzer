# Windows Login Analyzer

A simple Python script to detect failed login attempts (Event ID 4625) in Windows Security logs, perfect for beginner blue team practice in cybersecurity.

## Overview
This project parses Windows Security logs exported as text, identifies failed login attempts, and generates a report with timestamps, account names, and event IDs. It’s a beginner-friendly way to learn log analysis and Python scripting for cybersecurity.

## How to Use
1. Export your Windows Security logs from Event Viewer (`Windows Logs > Security`) as `security_log.txt` (Text, Tab Delimited format).
2. Place `security_log.txt` in this folder.
3. Run the script:

# python login_analyzer.py

4. Check `failed_logins_report.txt` for results.

## Screenshot
Here’s a screenshot of the project running in VS Code, showing the script, report, and terminal output (private details blurred for security):

![Screenshot 1](screenshot1.png)
![Screenshot 2](screenshot2.png)


## Sample Output
Here’s a sanitized version of the report (as seen in the screenshot):
Failed Login Attempts Detected:
Time: Audit Failure 2/22/2025 11:29:XX PM Account: TestAccount Event ID: 4625
## Files
- `login_analyzer.py`: The Python script with playful, beginner-friendly comments.
- `failed_logins_report.txt`: Generated report (sanitized version included for reference).
- `security_log.txt`: Sample input log (optional, sanitized or not included for privacy).

## Prerequisites
- Python 3.x (tested with Python 3.13.2)
- Windows PC with Event Viewer access

## License
MIT License (or choose your preferred open-source license).

#Cybersecurity #BlueTeam #Python #LogAnalysis
