# erstelle log datei wenn nicht vorhanden

def create_log_file():
    try:
        with open("Aufrufe_4.txt", "x") as file:
            file.write("Log Datei\n")
            file.write("=====================\n")
    except FileExistsError:
        pass

import datetime
# zähle aufrufe
def count_calls():
    try:
        with open("Aufrufe_4.txt", "r") as file:
            lines = file.readlines()
            count = len(lines) - 2  # Subtract header lines
    except FileNotFoundError:
        print("Datei nicht gefunden")
    try:
        count += 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        open("Aufrufe_4.txt", "a").write(f"Aufruf: {count} - Datum: {date}\n")
    finally:
        return count
    

create_log_file()
count_calls()