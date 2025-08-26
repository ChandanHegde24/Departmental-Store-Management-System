import os

class DepartmentStore:
    def __init__(self, filename="book.txt"):
        self.filename = filename

    def add_item(self):
        with open(self.filename, "a") as f:
            while True:
                code = input("Enter Item Code: ")
                name = input("Enter Item Name: ")
                company = input("Enter Company Name: ")
                qty = input("Enter No. of items: ")

                f.write(f"{code},{name},{company},{qty}\n")
                print("Item added successfully!")

                ch = input("Do you want to Add Another Item (y/n)? ")
                if ch.lower() != "y":
                    break

    def view_items(self):
        if not os.path.exists(self.filename):
            print("No items found!")
            return
        with open(self.filename, "r") as f:
            data = f.readlines()
            if not data:
                print("No items available in store.")
                return
            print("\n--- Store Inventory ---")
            print("Code\tName\tCompany\tQuantity")
            print("-------------------------------")
            for line in data:
                code, name, company, qty = line.strip().split(",")
                print(f"{code}\t{name}\t{company}\t{qty}")

    def update_item(self):
        code_to_update = input("Enter Item Code to update: ")
        found = False
        updated_data = []

        with open(self.filename, "r") as f:
            for line in f:
                code, name, company, qty = line.strip().split(",")
                if code == code_to_update:
                    found = True
                    print(f"Current -> {code}, {name}, {company}, {qty}")
                    code = input("Enter new Item Code: ")
                    name = input("Enter new Item Name: ")
                    company = input("Enter new Company Name: ")
                    qty = input("Enter new No. of Items: ")
                    updated_data.append(f"{code},{name},{company},{qty}\n")
                else:
                    updated_data.append(line)

        if found:
            with open(self.filename, "w") as f:
                f.writelines(updated_data)
            print("Item updated successfully!")
        else:
            print("Item not found!")

    def delete_item(self):
        code_to_delete = input("Enter Item Code to delete: ")
        found = False
        updated_data = []

        with open(self.filename, "r") as f:
            for line in f:
                code, name, company, qty = line.strip().split(",")
                if code == code_to_delete:
                    found = True
                    print(f"Deleting -> {code}, {name}, {company}, {qty}")
                else:
                    updated_data.append(line)

        if found:
            with open(self.filename, "w") as f:
                f.writelines(updated_data)
            print("Item deleted successfully!")
        else:
            print("Item not found!")

    def control_panel(self):
        while True:
            print("\n==== Department Store Management System ====")
            print("1. Add Item")
            print("2. View Items")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.view_items()
            elif choice == "3":
                self.update_item()
            elif choice == "4":
                self.delete_item()
            elif choice == "5":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


# Run the DSMS
if __name__ == "__main__":
    ds = DepartmentStore()
    ds.control_panel()