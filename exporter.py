def create_report(success_count, failure_count, repeated_failures, suspicious_ips):
    report = "Authentication Log Analysis\n"
    report +="=============================\n"
    report += f"Successful attempts: {success_count}\n"
    report += f"Failed attempts: {failure_count}\n"
    if repeated_failures:
        report += "\nRepeated authentication failures:\n"
        for failure in repeated_failures:
            key = failure[0]
            count = failure[1]
            username = key[0]
            ip_address = key[1]
            report += f"User:{username}, IP: {ip_address}, Failed Attempts: {count}\n"
    if suspicious_ips:
        report += "\nSuspicious IP addresses:\n"
        for ip_addresses, count in suspicious_ips:
            report += f"IP: {ip_address}, Failed Attempts: {count}\n"
    return report
def save_report(report, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)
        