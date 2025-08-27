import customtkinter as ctk  
import os

ctk.set_appearance_mode("system")  # "dark" or "light"
ctk.set_default_color_theme("blue")  # Try "dark-blue", "green", etc.

class ModernDSMS(ctk.CTk):
    def __init__(self, filename="book.txt"):
        super().__init__()
        self.filename = filename
        self.title("Department Store Management System")
        self.geometry("700x500")
        self.create_widgets()
        self.load_items()

    def create_widgets(self):
        # Header
        header = ctk.CTkLabel(self, text="Department Store", font=ctk.CTkFont(size=28, weight="bold"))
        header.pack(pady=16)

        # Control Buttons
        controls = ctk.CTkFrame(self)
        controls.pack(pady=10)
        ctk.CTkButton(controls, text="Add Item", command=self.add_item, width=120).pack(side="left", padx=5)
        ctk.CTkButton(controls, text="Update Item", command=self.update_item, width=120).pack(side="left", padx=5)
        ctk.CTkButton(controls, text="Delete Item", command=self.delete_item, width=120).pack(side="left", padx=5)

        # Search Bar
        search_frame = ctk.CTkFrame(self)
        search_frame.pack()
        self.search_var = ctk.StringVar()
        ctk.CTkLabel(search_frame, text="Search:").pack(side="left", padx=5)
        ctk.CTkEntry(search_frame, textvariable=self.search_var, width=200).pack(side="left")
        ctk.CTkButton(search_frame, text="Go", command=self.search_item).pack(side="left", padx=5)

        # Items Table
        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill="both", expand=True, pady=12)
        self.table = ctk.CTkTextbox(table_frame, width=580, height=300, font=("Segoe UI", 12))
        self.table.pack(padx=10, pady=10)

    def load_items(self, filter_func=None):
        self.table.delete("1.0", ctk.END)
        if not os.path.exists(self.filename):
            self.table.insert(ctk.END, "No items found!\n")
            return
        with open(self.filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        items = [line.split(",") for line in lines]
        if filter_func:
            items = [i for i in items if filter_func(i)]
        self.table.insert(ctk.END, f"{'Code':<12}{'Name':<18}{'Company':<20}{'Qty':<6}\n")
        self.table.insert(ctk.END, "-"*60 + "\n")
        for itm in items:
            self.table.insert(ctk.END, f"{itm:<12}{itm[9]:<18}{itm[10]:<20}{itm[11]:<6}\n")

    def add_item(self):
        # Modern dialog using CustomTkinter
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add Item")
        dialog.geometry("300x280")
        fields = ["Item Code", "Item Name", "Company", "No. of Items"]
        entries = {}
        for i, label in enumerate(fields):
            ctk.CTkLabel(dialog, text=label).pack(pady=4)
            entry = ctk.CTkEntry(dialog)
            entry.pack()
            entries[label] = entry
        def save():
            values = [entries[f].get() for f in fields]
            if not all(values):
                ctk.CTkMessagebox(dialog, message="All fields must be filled!", icon="warning")
                return
            with open(self.filename, "a") as f:
                f.write(",".join(values) + "\n")
            self.load_items()
            dialog.destroy()
        ctk.CTkButton(dialog, text="Save", command=save).pack(pady=8)

    def update_item(self):
        # For simplicity, updates by code (prompt and modal)
        code = ctk.CTkInputDialog(text="Enter Item Code to update:", title="Update")
        code_val = code.get_input()
        if not code_val: return
        updated_data = []
        found = False
        with open(self.filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts == code_val:
                    found = True
                    # Pop dialog for editing
                    dialog = ctk.CTkToplevel(self)
                    dialog.title("Update Item")
                    dialog.geometry("300x280")
                    fields = ["Item Code", "Item Name", "Company", "No. of Items"]
                    entries = {}
                    for i, label in enumerate(fields):
                        ctk.CTkLabel(dialog, text=label).pack(pady=4)
                        entry = ctk.CTkEntry(dialog)
                        entry.insert(0, parts[i] if i < len(parts) else "")
                        entry.pack()
                        entries[label] = entry
                    def save():
                        values = [entries[f].get() for f in fields]
                        updated_data.append(",".join(values) + "\n")
                        with open(self.filename, "r") as f:
                            for line in f:
                                ps = line.strip().split(",")
                                if ps != code_val:
                                    updated_data.append(line)
                        with open(self.filename, "w") as wf:
                            wf.writelines(updated_data)
                        self.load_items()
                        dialog.destroy()
                    ctk.CTkButton(dialog, text="Update", command=save).pack(pady=8)
                    return
                else:
                    updated_data.append(line)
        if not found:
            ctk.CTkMessagebox(self, message="Item not found!", icon="warning")

    def delete_item(self):
        code = ctk.CTkInputDialog(text="Enter Item Code to delete:", title="Delete")
        code_val = code.get_input()
        updated_data = []
        found = False
        with open(self.filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts == code_val:
                    found = True
                else:
                    updated_data.append(line)
        if found:
            with open(self.filename, "w") as f:
                f.writelines(updated_data)
            self.load_items()
            ctk.CTkMessagebox(self, message="Item deleted!", icon="info")
        else:
            ctk.CTkMessagebox(self, message="Item not found!", icon="warning")

    def search_item(self):
        query = self.search_var.get().lower()
        def filter_func(item):
            return any(query in s.lower() for s in item)
        self.load_items(filter_func if query else None)

if __name__ == "__main__":
    ModernDSMS()