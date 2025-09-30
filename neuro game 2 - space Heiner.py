# Programm zum Erstellen von PDF Datei Welche Eine bestimmte Anzahl Also sozusagen die sind Einfache Benutzbare Skin Zur Festhaltung des Scoreverlauf XP Punkte Themas Sozusagen wie in endokrines Level Lebensleistungssystem

## kann PDF dateien erstellen
## fragt den Benutzer nach den Basic 3 ab
### fragt den Benutzer nach seinem Held ab
### fragt den Benutzer nach den Skills ab
### fragt den Benutzer nach den Gesundheits Fluch

## sorgt dafür das PDf in jeweils 90 - 120 minuten bearbeitet wird

#######
## Version 2
#######

# hero erfahren
import time
hero = input("Wähle weise!! - >: ")
time.sleep(0.3)
print(f"Okay: {hero}" + " los gehts!!")
time.sleep(1)
# ende hero erfahren


# ticket 4
# textdartei soll erstellt werden

def create_log_file():
    with open("Aufrufe_2.txt", "w") as file:
        file.write("Log Datei für Aufrufe\n")
        file.write("=====================\n")

create_log_file()

'''

def counter():
    try:
        with open("Aufrufe_1.txt", "r") as file:
            count = int(file.read())
    except FileNotFoundError:
        print("Datei nicht gefunden")
        count = 0
    count += 1
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open("Aufrufe_1.txt", "a") as file:
        file.write(f"Aufruf #{count} - Uhrzeit: {current_time}\n")
    return count

counter()




















def counter_3():
    try:
        with open("Aufrufe_1.txt", "r") as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0
    count += 1
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open("Aufrufe_1.txt", "a") as file:
        file.write(str(count))
        file.write("\n")
        file.write("Uhrzeit des Aufrufes: ")
        file.write(current_time)
        file.write("\n")
    return count


'''

'''




'''

















######################################
# Ticket 1
########################################
# hero erfahren
import time
hero = input("Wähle weise!! - >: ")
time.sleep(0.3)
print(f"Okay: {hero}" + " los gehts!!")
time.sleep(1)
# ende hero erfahren
######################################

######################################
# Ticket 2
########################################
# funktion die mitschreibt wie oft das programm getestet/gestartet wurde
def counter():
    try:
        with open("counter.txt", "r") as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0
    count += 1
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open("counter.txt", "a") as file:
        file.write(f"Aufruf #{count} - Uhrzeit: {current_time}\n")
    return count
# ende funktion die mitschreibt wie oft das programm getestet/gestartet wurde
######################################
######################################



# Ticket 2
########################################
# counter um zeitpunkt des aufrufes erweitern
def counter_2():
    try:
        with open("counter_2.txt", "r") as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0
    count += 1
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Aktuelle Uhrzeit:", current_time)
    with open("counter_2.txt", "a") as file:
        file.write(str(count))
        file.write("\n")
        file.write("Uhrzeit des Aufrufes: ")
        file.write(current_time)
        file.write("\n")
    return count


# ticket 3 
# counter soll neue eintäge addieren

def counter_3():
    try:
        with open("counter_3.txt", "r") as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0
    count += 1
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open("counter_3.txt", "a") as file:
        file.write(str(count))
        file.write("\n")
        file.write("Uhrzeit des Aufrufes: ")
        file.write(current_time)
        file.write("\n")
    return count


counter()
counter_2()
counter_3()