# Ticket 1
# create log file if not exists
# Aufrufe zählen
# angeben wie oft das spiel gestartet wurde
# zeit neben den die aufruf nummer schreiben

# Ticket 1a
# create log file if not exists

def create_log_file():
    try:
        with open("Aufrufe_3.txt", "x") as file:
            file.write("Log Datei\n")
            file.write("=====================\n")
    except FileExistsError:
        pass

create_log_file()

def counter():
    try:
        with open("Aufrufe_3.txt", "r") as file:
            lines = file.readlines()
            count = len(lines) - 2  # Subtract header lines
    except FileNotFoundError:
        print("Datei nicht gefunden")
    try:
        count += 1
        open("Aufrufe_3.txt", "a").write(f"Aufruf #{count}\n")

    