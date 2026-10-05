def detect_repeated_failures(records):
    print("DETECTOR RUNNING")
    failed_attempts = {}
    ip_failures = {}
    suspicious_ips = []

    for record in records:
        username = record[0]
        ip_address = record[1]
        status = record[2]

        if status == "Failed":
            key = (username, ip_address)
            failed_attempts[key] = failed_attempts.get(key, 0) + 1
            ip_failures[ip_address] = ip_failures.get(ip_address, 0) + 1 
    repeated_failures = []

    for key, count in failed_attempts.items():
            

            if count > 1: repeated_failures.append((key,count))
    for ip_address, count in ip_failures.items():
            if count > 2: suspicious_ips.append((ip_address, count))   
    return repeated_failures, suspicious_ips 
            

                
