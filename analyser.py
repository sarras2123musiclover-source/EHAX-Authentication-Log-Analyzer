def analyse_logs(records):
    success_count = 0
    failure_count = 0
    for record in records: 
        status = record[2]
        if status == "Accepted":
            success_count += 1
        elif status == "Failed":
            failure_count += 1
    return success_count, failure_count 