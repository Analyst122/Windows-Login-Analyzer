# Welcome to the Sneaky Login Detector 3000! Let’s catch those password fumblers!

def analyze_failed_logins(log_file, report_file):
    failed_logins = []  # Our treasure chest for sneaky clues
    
    # Time to crack open the log file and hunt for baddies!
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    
    # Let’s snoop through the lines like detectives on a mission
    current_event = {}
    for line in lines:
        if "4625" in line:  # Spotted a "wrong password" villain!
            parts = line.split("\t")
            if len(parts) >= 5:  # Make sure we’ve got enough loot
                current_event["timestamp"] = f"{parts[0]} {parts[1]}"  # When the crime happened
                current_event["event_id"] = parts[3].strip()  # The villain’s secret code
        elif "Account Name" in line and "Source" not in line and current_event:
            # Found the sneaky suspect’s name—busted!
            name_part = line.split("Account Name:")[1].strip()
            current_event["account"] = name_part.split("\t")[0]
            failed_logins.append(current_event)
            current_event = {}  # Reset our detective notepad for the next crook
    
    # Time to spill the beans in our super-secret report!
    with open(report_file, 'w') as report:
        if failed_logins:
            report.write("Failed Login Attempts Detected:\n")
            report.write("-" * 40 + "\n")
            for event in failed_logins:
                report.write(f"Time: {event['timestamp']}\n")
                report.write(f"Account: {event['account']}\n")
                report.write(f"Event ID: {event['event_id']}\n")
                report.write("-" * 40 + "\n")
        else:
            report.write("No failed login attempts detected—everyone’s behaving today!\n")

# Let’s kick off the detective party!
if __name__ == "__main__":
    input_log = "security_log.txt"
    output_report = "failed_logins_report.txt"
    analyze_failed_logins(input_log, output_report)
    print(f"Analysis complete. Report saved to {output_report}. Woohoo!")