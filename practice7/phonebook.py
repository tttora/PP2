import sqlite3
import csv
import re
from connect import connect_db

pattern = re.compile(r"^[0-9]{10,15}$")

def createtable():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Phonebook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE 
        )
        """)
        conn.commit()


def is_valid(phone):
    return bool(pattern.fullmatch(phone))

def print_contacts(results):
    if not results:
        print ("No contacts found")
        return
    print ("\n---Contacts---")
    for contact in results:
        print(f"ID:{contact[0]}, Name: {contact[1]}, Phone: {contact[2]}")


def insertfromcsv(filename = "contacts.csv"):
    try:
        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)

            with connect_db() as conn:
                cursor = conn.cursor()

                for row in reader:
                    try:
                        if len(row) != 2:
                            print(f"Skipped invalid row: {row}")
                            continue

                        name = row[0].strip()
                        phone = row[1].strip()
                        if not name:
                            print(f"Skipped row with empty name: {row}")
                            continue
                        if not is_valid(phone):
                            print(f"Invalid phone: {row}")
                            continue
                        cursor.execute(
                            "INSERT INTO Phonebook (name, phone) VALUES (?, ?)",
                            (name, phone)
                        )
                    except sqlite3.IntegrityError:
                        print(f"Phone already exists, skipped: {row}")
                    except Exception as e:
                        print(f"Error inserting {row}: {e}")

                conn.commit()
            print("CSV import finished!")
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(f"Error opening CSV file: {e}")

def insertfromconsole():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    if not name:
        print("Name cannot be empty")
        return
    
    if not is_valid(phone):
        print("Invalid phone number")
        return
    
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Phonebook (name, phone) VALUES (?, ?)",
                (name, phone)
            )
            conn.commit()
            print("Contact added")
    except sqlite3.IntegrityError:
        print("This phone already exists")
    except Exception as e:
        print(f"Error: {e}")

def updating():
    oldphone = input("Enter the current phone number of the contact: ").strip()
    newname = input("Enter new name(leave blank to skip: )").strip()
    newphone = input("Enter new phone(leave blank to skip): ").strip()

    if not newname and not newphone:
        print("Nothing to update")
        return
    
    if newphone and not is_valid(newphone):
        print("Invalid new phone number")
        return
    
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Phonebook WHERE phone = ?", 
                (oldphone,)
            )   
            contact = cursor.fetchone()

            if not contact:
                print("Contact not found")
                return
            
            updatedname = newname if newname else contact[1]
            updatedphone = newphone if newphone else contact[2]
            cursor.execute("""
                UPDATE Phonebook
                SET name = ?, phone = ?
                WHERE phone = ?""",
            (updatedname, updatedphone, oldphone)
            )
            conn.commit()
            print("Contact updated")
    except sqlite3.IntegrityError:
        print("Failed update: phone number already exists")
    except Exception as e:
        print(f"Error: {e}")

def querycontacts():
    print("1. All contacts")
    print("2. Filter by name")
    print("3. Filter by phone")

    choice = input("Choose filter option: ").strip()
    with connect_db() as conn:
        cursor = conn.cursor()

        if choice == "1":
            cursor.execute("SELECT * FROM Phonebook ORDER BY name")
        elif choice == "2":
            name = input("Enter name to search: ").strip()
            cursor.execute("SELECT * FROM Phonebook WHERE name LIKE ? ORDER BY name",
            ('%' + name + '%'))
        elif choice == "3":
            phone = input("Enter phone to search: ").strip()
            cursor.execute("SELECT * FROM Phonebook WHERE phone LIKE ? ORDER BY name",
            ('%' + phone + '%'))
        else:
            print("Invalid choice")
            return
        
        results = cursor.fetchall()
        print_contacts(results)
def searchcontacts():
    pattern = input("Enter pattern(name or phone): ").strip()
    with connect_db() as conn:
        cursor = conn.cursor()
        likepattern = f"%{pattern}%"
        cursor.execute("""
            SELECT * FROM Phonebook
            WHERE name LIKE ? OR phone LIKE ?
            ORDER BY name""",
            (likepattern, likepattern))
        results = cursor.fetchall()
        print_contacts(results)
def upsertcontacts():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    if not name:
        print("Enter name")
        return
    if not is_valid(phone):
        print("Invalid phone number")
        return
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Phonebook WHERE phone = ?", (phone,))
            existing = cursor.fetchone()

            if existing:
                cursor.execute("UPDATE Phonebook SET name = ? WHERE phone = ?", (name,phone))
                print("Existing contact updated")
            else:
                cursor.execute("INSERT INTO Phonebook (name,phone) VALUES(?, ?)", (name, phone))
                print("New contact added")

            conn.commit()
    except Exception as e:
        print(f"Error: {e}")

def deletecontacts():
    print("Delete by:")
    print("1. Name")
    print("2. Phone")
    print("3. Name or phone(single input)")

    choice = input("Choose option: ").strip()

    with connect_db() as conn:
        cursor = conn.cursor()
        if choice == "1":
            name = input("Enter name to delete: ").strip()
            cursor.execute("DELETE FROM Phonebook WHERE name = ?", (name,))
        elif choice == "2":
            phone = input("Enter phone: ").strip()
            cursor.execute("DELETE FROM Phonebook WHERE phone = ?", (phone,))
        elif choice == "3":
            identifier = input("Enter name or phone: ").strip()
            cursor.execute("DELETE FROM Phonebook WHERE phone = ?", (identifier,))
            if cursor.rowcount == 0:
                cursor.execute("DELETE FROM Phonebook WHERE name = ?", (identifier,))
        else:
            print("Invalid choice")


def menu():
    createtable()

    while True:
        print("\n---Phonebook Menu---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Search by pattern")
        print("7. Upsert contact")
        print("8. Exit")

        choice = input("Enter choice: ").strip()
        if choice == '1':
            insertfromcsv()
        elif choice == '2':
            insertfromconsole()
        elif choice == '3':
            updating()
        elif choice == '4':
            querycontacts()
        elif choice == '5':
            deletecontacts()
        elif choice == '6':
            searchcontacts()
        elif choice == '7':
            upsertcontacts()
        elif choice == '8':
            print("Bye!")
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    menu()