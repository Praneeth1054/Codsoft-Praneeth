import csv
import re

class ContactBook:
    def __init__(self):  # Corrected __init__ method
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        if not re.match(r"^\d{10}$", phone):
            print("Invalid phone number. Must be 10 digits.")
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            return
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def export_contacts(self, filename="contacts.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])
            writer.writeheader()
            writer.writerows(self.contacts)
        print("Contacts exported successfully.")

# Example Usage
book = ContactBook()
book.add_contact("Sivamani (Nagarjuna)", "9848022338", "NakuKonchamMental@gmail.com", "1 town ps, purna market, Visakhapatnam")
book.view_contacts()
book.export_contacts()
