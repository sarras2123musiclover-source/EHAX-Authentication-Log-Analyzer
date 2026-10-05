from parser import read_log_file 
from parser import parse_log_line
from analyser import analyse_logs
from detector import detect_repeated_failures
from exporter import create_report
from exporter import save_report

try: 
    lines = read_log_file("logs/sample.txt") 
except FileNotFoundError: 
     print("Error: Log file not found.")
     exit()


records = []
for line in lines:
    result = parse_log_line(line)
    records.append(result)
success_count, failure_count = analyse_logs(records)
print("Successful attempts:", success_count)
print("Failed attempts:", failure_count)

repeated_failures, suspicious_ips = detect_repeated_failures(records)

if repeated_failures:
    print("ALERT: Repeated authentication failures detected")
    for failure in repeated_failures:
        key = failure[0]
        count = failure[1]


        username = key[0]
        ip_address = key[1]
        print("User:", username)
        print("IP Address:", ip_address)
        print("Failed Attempts:", count)
if suspicious_ips:
        print("ALERT: Suspicious IP addresses detected")
        for ip_addresses, count in suspicious_ips:
             print("Suspicious IP:", ip_address)
             print("Failed Attempts:", count)
        report = create_report(success_count, failure_count, repeated_failures, suspicious_ips)
        save_report(report, "reports/report.txt")
print("Report generated successfully.")





    