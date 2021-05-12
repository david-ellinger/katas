"""
    CHAPTER 3 - The Basic Tools
    Page 78
    Design a small address book database (name, phone number, etc)
    using a straightforward binary representation.
"""

class Entry:
    name: str
    def __init__(self, name: str) -> None:
        self.name = name

class AddressBook:

    def save(entry: Entry):
        print("Saving...")

    def get(name: str):
        print(f"Getting name {name}")

    def list():
        print("List of names")


if __name__ == "__main__":
    #TODO: Need to test and get it working with docker
    ab = AddressBook()
    ab.save()
    ab.get("David")
    ab.list()
