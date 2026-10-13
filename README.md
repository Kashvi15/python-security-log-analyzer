# Python Security Log Analyzer

## About the Project
This is a beginner-friendly cybersecurity project built using Python. It analyzes sample security logs to identify failed login attempts, successful logins, and potentially suspicious login activity.

## Features
- Reads log entries from a text file.
- Counts successful logins by IP address.
- Counts failed login attempts by IP address.
- Calculates total failed attempts and unique IP addresses.
- Sorts failed login attempts from highest to lowest.
- Generates security alerts based on configurable thresholds.
- Identifies IP addresses with both failed and successful logins.
- Warns when failed login attempts are followed by a successful login from the same IP.

## Technologies Used
- Python
- File Handling
- Dictionaries and Loops
- Conditional Statements
- Basic Log Analysis

## Project Files
- `first_program.py` — Main Python program.
- `security_logs.txt` — Sample security log data.
- `README.md` — Project documentation.

## How to Run
1. Install Python.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run the following command in the terminal:

   `python first_program.py`

## Disclaimer
This project uses sample log data for educational purposes. Security alerts indicate activity that may require investigation; they do not prove that an account has been compromised.

## Learning Goals
This project helped me practise Python programming, file handling, dictionaries, loops, sorting, and basic cybersecurity log analysis.
