def read_log_file(file_path):
   with open(file_path, "r",encoding="utf-8") as file :
    lines = file.readlines() 
    return lines 
def parse_log_line(line):
     parts = line.split()
     username = parts[8]
     ip_address = parts[10]
     status = parts[5]
     return username, ip_address, status 
   