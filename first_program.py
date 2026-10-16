from datetime import datetime
with open("security_logs.txt","r") as file:
    log_lines = file.readlines()

successful_logins = {}

for line in log_lines:
    if "Accepted password" in line:
        parts = line.split()
        ip = parts[-1]

        if ip in successful_logins:
            successful_logins[ip] = successful_logins[ip] + 1
        else:
            successful_logins[ip] = 1    

print("\nSuccessful logins:", successful_logins)

failed_logins = {}

for line in log_lines:
    if "Failed password" in line:
        parts = line.split()
        ip = parts[-1]

        if ip in failed_logins:
            failed_logins[ip] = failed_logins[ip] + 1
        else:
            failed_logins[ip] = 1

total_attempts = sum(failed_logins.values())
total_ips = len(failed_logins)

print("Total Failed Login Attempts:", total_attempts)
print("Total Unique IP Addresses:", total_ips)

print("\nSecurity Warning: Failed Attempts Followed by Successful Login")

for ip in failed_logins:
    if ip in successful_logins:
        print(
            "WARNING:", 
            ip,
            "| Failed Attempts:", failed_logins[ip],
            "| Successful Logins:", successful_logins[ip])

print("Failed Login Summary:")

sorted_logins = sorted(
    failed_logins.items(),
    key=lambda item: item[1],
    reverse=True
)
for ip, attempts in sorted_logins:
    print(ip, ":", attempts)

threshold = 3

print("\nSecurity Alerts:")

for ip, attempts in failed_logins.items():
    if attempts >= threshold:
        if attempts >= 5:
            severity = "HIGH"
        else:
            severity = "MEDIUM"

        print("SECURITY ALERT:", ip, "| Attempts:", attempts, "| Severity:", severity)

with open("security_report.txt","a") as file:
    file.write("\n===== Security Report =====\n")
    report_time = datetime.now().strftime("%d-%m-%Y | %I:%M %p")
    file.write("Report Generated At : " + report_time + "\n")
    file.write("Total Failed Login Attempts: " + str(total_attempts) + "\n")
    file.write("Total Unique IP Addresses: " + str(total_ips) + "\n")
    file.write("\nFailed Login Summary:\n")

    for ip, attempts in sorted_logins:
        file.write(ip + " : " + str(attempts) + "\n")
        
    file.write("\nSuccessful Login Summary:\n")

    for ip, attempts in successful_logins.items():
        file.write(ip + " : " + str(attempts) + "\n")    

    file.write("\nSecurity Alerts:\n")

    for ip, attempts in failed_logins.items():
        if attempts >= threshold:
            if attempts >= 5:
                severity = "HIGH"
            else:
                severity = "MEDIUM"

            file.write(
                "SECURITY ALERT: " + ip
                + " | Attempts: " + str(attempts)
                + " | Severity: " + severity + "\n"
            )        
     

