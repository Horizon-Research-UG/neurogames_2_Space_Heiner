
# create_log_file

dateiname = "Aufrufe_8.txt"

def create_log_file():
    try:
        with open(dateiname, "x") as file:
            file.write("Log Datei\n")
            file.write("=====================\n")
    except FileExistsError:
        pass

create_log_file()

# prepend new entries (newest at top)
import datetime
import time
def count_calls():
    try:
        with open(dateiname, "r") as file:
            lines = file.readlines()
            count = len(lines) - 2  # Subtract header lines
    except FileNotFoundError:
        print("Datei nicht gefunden")
        time.sleep(2)  # Kurze Pause, um sicherzustellen, dass die Datei erstellt wird
        count = 0
        lines = []
    
    count += 1
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = f"Aufruf: {count} - Datum: {date}\n"
    
    # Neue Einträge OBEN einfügen (nach Header)
    if len(lines) >= 2:
        # Header behalten, neuen Eintrag nach Header einfügen
        header = lines[:2]  # "Log Datei" und "============="
        old_entries = lines[2:]  # Alte Einträge
        new_content = header + [new_entry] + old_entries
    else:
        # Falls keine Header da sind
        new_content = [new_entry]
    
    # Datei komplett neu schreiben
    with open(dateiname, "w") as file:
        file.writelines(new_content)
    
    return count
    
count_calls()