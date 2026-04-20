import sqlite3
import csv
import re
from connect import connect_db

PHONE_PATTERN = re.compile(r"^[0-9]{10,15}$")


def createtable():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Phonebook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE
        )
        """)
        conn.commit()


def is_valid(phone):
    return bool(PHONE_PATTERN.fullmatch(phone))


def print_contacts(results):
    if not results:
        print("No contacts found")
        return

    print("\n---Contacts---")
    for contact in results:
        print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}")


def search_records(pattern_value):
    like_pattern = f"%{pattern_value}%"
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM Phonebook
            WHERE name LIKE ? OR phone LIKE ?
            ORDER BY name
        """, (like_pattern, like_pattern))
        return cursor.fetchall()


def searchcontacts():
    pattern_value = input("Enter pattern (part of name or phone): ").strip()
    results = search_records(pattern_value)
    print_contacts(results)


def upsert_user(name, phone):
    name = name.strip()
    phone = phone.strip()

    if not name:
        return False, "Name cannot be empty"

    if not is_valid(phone):
        return False, "Invalid phone number"

    try:
        with connect_db() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM Phonebook WHERE name = ?", (name,))
            existing = cursor.fetchone()

            if existing:
                cursor.execute(
                    "UPDATE Phonebook SET phone = ? WHERE id = ?",
                    (phone, existing[0])
                )
                conn.commit()
                return True, "Existing user updated"

            cursor.execute(
                "INSERT INTO Phonebook (name, phone) VALUES (?, ?)",
                (name, phone)
            )
            conn.commit()
            return True, "New user added"

    except sqlite3.IntegrityError:
        return False, "This phone already exists for another contact"
    except Exception as e:
        return False, f"Error: {e}"


def upsertcontacts():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    success, message = upsert_user(name, phone)
    print(message)


def insert_many_users(users):
    incorrect_data = []

    with connect_db() as conn:
        cursor = conn.cursor()

        for row in users:
            if len(row) != 2:
                incorrect_data.append((row, "Row must contain exactly name and phone"))
                continue

            name = str(row[0]).strip()
            phone = str(row[1]).strip()

            if not name:
                incorrect_data.append((name, phone, "Empty name"))
                continue

            if not is_valid(phone):
                incorrect_data.append((name, phone, "Invalid phone"))
                continue

            cursor.execute("SELECT id FROM Phonebook WHERE name = ?", (name,))
            existing = cursor.fetchone()

            try:
                if existing:
                    cursor.execute(
                        "UPDATE Phonebook SET phone = ? WHERE id = ?",
                        (phone, existing[0])
                    )
                else:
                    cursor.execute(
                        "INSERT INTO Phonebook (name, phone) VALUES (?, ?)",
                        (name, phone)
                    )
            except sqlite3.IntegrityError:
                incorrect_data.append((name, phone, "Phone already exists for another contact"))

        conn.commit()

    return incorrect_data


def insertmanyfromconsole():
    try:
        count = int(input("How many users do you want to enter? ").strip())
    except ValueError:
        print("Invalid number")
        return

    users = []
    for i in range(count):
        print(f"\nUser {i + 1}")
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        users.append((name, phone))

    incorrect_data = insert_many_users(users)

    if not incorrect_data:
        print("All users processed successfully")
    else:
        print("\nIncorrect data:")
        for item in incorrect_data:
            print(item)


def get_contacts_paginated(limit, offset):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM Phonebook
            ORDER BY name
            LIMIT ? OFFSET ?
        """, (limit, offset))
        return cursor.fetchall()


def query_with_pagination():
    try:
        limit = int(input("Enter LIMIT: ").strip())
        offset = int(input("Enter OFFSET: ").strip())
    except ValueError:
        print("LIMIT and OFFSET must be integers")
        return

    if limit <= 0 or offset < 0:
        print("LIMIT must be > 0 and OFFSET must be >= 0")
        return

    results = get_contacts_paginated(limit, offset)
    print_contacts(results)


def querycontacts():
    print("1. All contacts")
    print("2. Filter by name")
    print("3. Filter by phone")
    print("4. Pagination")

    choice = input("Choose filter option: ").strip()

    with connect_db() as conn:
        cursor = conn.cursor()

        if choice == "1":
            cursor.execute("SELECT * FROM Phonebook ORDER BY name")

        elif choice == "2":
            name = input("Enter name to search: ").strip()
            cursor.execute(
                "SELECT * FROM Phonebook WHERE name LIKE ? ORDER BY name",
                ('%' + name + '%',)
            )

        elif choice == "3":
            phone = input("Enter phone to search: ").strip()
            cursor.execute(
                "SELECT * FROM Phonebook WHERE phone LIKE ? ORDER BY name",
                ('%' + phone + '%',)
            )

        elif choice == "4":
            try:
                limit = int(input("Enter LIMIT: ").strip())
                offset = int(input("Enter OFFSET: ").strip())
            except ValueError:
                print("LIMIT and OFFSET must be integers")
                return

            if limit <= 0 or offset < 0:
                print("LIMIT must be > 0 and OFFSET must be >= 0")
                return

            cursor.execute("""
                SELECT * FROM Phonebook
                ORDER BY name
                LIMIT ? OFFSET ?
            """, (limit, offset))

        else:
            print("Invalid choice")
            return

        results = cursor.fetchall()
        print_contacts(results)


def insertfromcsv(filename="contacts.csv"):
    try:
        users = []

        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                users.append(row)

        incorrect_data = insert_many_users(users)

        print("CSV import finished!")
        if incorrect_data:
            print("\nIncorrect data:")
            for item in incorrect_data:
                print(item)

    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(f"Error opening CSV file: {e}")


def insertfromconsole():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    success, message = upsert_user(name, phone)
    print(message)


def updating():
    oldphone = input("Enter the current phone number of the contact: ").strip()
    newname = input("Enter new name (leave blank to skip): ").strip()
    newphone = input("Enter new phone (leave blank to skip): ").strip()

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
                WHERE phone = ?
            """, (updatedname, updatedphone, oldphone))

            conn.commit()
            print("Contact updated")

    except sqlite3.IntegrityError:
        print("Failed update: name or phone already exists")
    except Exception as e:
        print(f"Error: {e}")


def delete_by_username_or_phone(identifier):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Phonebook WHERE name = ? OR phone = ?",
            (identifier, identifier)
        )
        deleted_count = cursor.rowcount
        conn.commit()
        return deleted_count


def deletecontacts():
    identifier = input("Enter name or phone to delete: ").strip()
    deleted_count = delete_by_username_or_phone(identifier)

    if deleted_count == 0:
        print("No contact found")
    else:
        print(f"Deleted {deleted_count} contact(s)")


def menu():
    createtable()

    while True:
        print("\n---Phonebook Menu---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete by name or phone")
        print("6. Search by pattern")
        print("7. Upsert user by name")
        print("8. Insert many users")
        print("9. Paginated query")
        print("10. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            insertfromcsv()
        elif choice == "2":
            insertfromconsole()
        elif choice == "3":
            updating()
        elif choice == "4":
            querycontacts()
        elif choice == "5":
            deletecontacts()
        elif choice == "6":
            searchcontacts()
        elif choice == "7":
            upsertcontacts()
        elif choice == "8":
            insertmanyfromconsole()
        elif choice == "9":
            query_with_pagination()
        elif choice == "10":
            print("Bye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()