import re
from collections import Counter

def analyze_ssh_logs(file_path, threshold=5):
                                                                                   # Regex to find an IP address (simplified for standard IPv4)
    ip_pattern = r'Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                                                                                         # here  .* means anything in between , cover username like invalid user test


    
    failed_ips = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                                                                                   # Check if the line indicates a failed login
                match = re.search(ip_pattern, line)
                if match:
                    # Extract the IP from the capture group
                    failed_ips.append(match.group(1))
        
                                                                            # Count the occurrences of each IP
        counts = Counter(failed_ips)
        
        print(f"{'IP Address':<20} | {'Failed Attempts':<15} | Status")
        print("-" * 50)
        
        for ip, count in counts.items():
            status = "⚠️  BRUTE FORCE DETECTED" if count >= threshold else "Normal"
            print(f"{ip:<20} | {count:<15} | {status}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

                                                                                       # Run the script
if __name__ == "__main__":
    analyze_ssh_logs('ssh_logs.txt')
