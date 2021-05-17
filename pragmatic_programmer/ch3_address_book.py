"""
    CHAPTER 3 - The Basic Tools
    Page 78
    Design a small address book database (name, phone number, etc)
    using a straightforward binary representation.
"""
import sqlite3

DB_NAME = "address_book.db"

class Entry:
    name: str
    def __init__(self, name: str) -> None:
        self.name = name

class AddressBook:

    def __init__(self) -> None:
        self.connection = sqlite3.connect(DB_NAME)

    def save(self, entry: Entry):
        print("Saving...")

    def get(self, name: str):
        print(f"Getting name {name}")

    def list(self):
        print("List of names")


if __name__ == "__main__":
    #TODO: Need to test and get it working with docker
    ab = AddressBook()
    ab.save(Entry(
        name="David"
    ))
    ab.get("David")
    ab.list()
