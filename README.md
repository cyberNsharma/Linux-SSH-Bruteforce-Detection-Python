#  Linux SSH Brute-Force Detection using Python Automation

##  Project Overview
This project demonstrates host-based log monitoring and brute-force attack detection by analyzing Linux authentication logs (`/var/log/auth.log`) using Python automation.  
The objective is to replicate SIEM-style detection logic at the operating system level without relying on a full SIEM platform, focusing on how detection and correlation work internally.

---

## Objectives
- Simulate SSH brute-force attacks against a Linux system
- Generate and analyze authentication failure logs
- Identify attacker IP addresses through log correlation
- Apply threshold-based detection logic
- Automate analysis using Python scripting
- Produce SOC-style investigative findings

---

## Detection Approach
The detection logic follows a structured SOC workflow:

1. Monitor Linux authentication logs (`auth.log`)
2. Extract failed SSH login attempts
3. Correlate events based on source IP address
4. Count repeated failures within a session/log file
5. Flag IPs exceeding a defined failure threshold as potential brute-force attacks

This approach mirrors how SIEM correlation rules work under the hood.

---

##  Architecture

Attacker (Kali Linux)
        ↓
Linux SSH Server
        ↓
/var/log/auth.log
        ↓
Python Detection Script
        ↓
Brute-Force Alert Output



---

##  Tools & Technologies
- **Operating System:** Ubuntu Linux
- **Attack Simulation:** OpenSSH (manual & automated attempts)
- **Log Source:** `/var/log/auth.log`
- **Scripting Language:** Python 3
- **Attacker Machine:** Kali Linux

---

##  Attack Simulation
- **Attack Type:** SSH Brute Force
- **Method:** Repeated failed authentication attempts
- **Execution:** Manual SSH attempts and loop-based SSH execution
- **Result:** Multiple `Failed password` entries generated in `auth.log`

---

##  Log Analysis
- **Log File:** `/var/log/auth.log`
- **Event Type:** Failed SSH authentication
- **Key Fields Extracted:**
  - Source IP address
  - Username
  - Timestamp

Filtered logs were exported into a separate file and used as input for automated analysis.

---

##  Python-Based Detection Logic
The Python script performs the following actions:
- Reads filtered SSH failure logs
- Extracts attacker IP addresses
- Counts failed attempts per IP
- IPs based on number of failures
- Flags IPs exceeding a defined threshold as brute-force attackers

This simulates alert generation performed by SIEM tools.

---

##  Findings
- Identified attacker IP(s) with highest failed authentication attempts
- Observed repeated login failures in a short time window
- Confirmed brute-force behavior based on threshold logic

---

##  Limitations
- Host-based analysis only (single system)
- No real-time alerting or dashboard visualization
- No centralized log ingestion

---

##  Future Improvements
- Integrate detection logic with a SIEM platform (Wazuh / Splunk)
- Add real-time monitoring and alerting
- Extend detection to Windows event logs
- Implement time-based correlation windows
- Automate response actions (IP blocking)

---

##  SOC Relevance
This project demonstrates practical SOC analyst skills including:
- Authentication log analysis
- Brute-force attack detection
- Event correlation and threshold logic
- Python automation for security monitoring
- Understanding SIEM detection principles beyond tool usage

---

##  Report
A detailed investigation report with screenshots, analysis, and findings is available in the `Report/` directory.

---

##  Author
**Nitin Kumar Sharma**  
Aspiring Security Analyst

