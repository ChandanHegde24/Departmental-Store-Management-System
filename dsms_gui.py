import customtkinter as ctk
import os

ctk.set_appearance_mode("system")  # Use system theme (can be 'dark' or 'light')
ctk.set_default_color_theme("green")  # Available themes: "blue", "dark-blue", "green"


class ModernDSMS(ctk.CTk):
    def __init__(self, filename="book.txt"):
        super().__init__()
        self.filename = filename
        self.title("Department Store Management System")
        self.geometry("750x550")
        self.create_widgets()
        self.load_items()

    def create_widgets(self):
        # Header
        header = ctk.CTkLabel(self, text="Department Store Management System", font=ctk.CTkFont(size=24, weight="bold"))
        header.pack(pady=16)

        # Controls frame with buttons
        controls = ctk.CTkFrame(self)
        controls.pack(pady=10)

        ctk.CTkButton(controls, text="Add Item", command=self.add_item_dialog, width=120).pack(side="left", padx=10)
        ctk.CTkButton(controls, text="Update Item", command=self.update_item_dialog, width=120).pack(side="left", padx=10)
        ctk.CTkButton(controls, text="Delete Item", command=self.delete_item_dialog, width=120).pack(side="left", padx=10)

        # Search frame
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=5)
        self.search_var = ctk.StringVar()
        ctk.CTkLabel(search_frame, text="Search:").pack(side="left", padx=5)
        ctk.CTkEntry(search_frame, textvariable=self.search_var, width=250).pack(side="left", padx=5)
        ctk.CTkButton(search_frame, text="Go", command=self.search_item).pack(side="left", padx=5)
        ctk.CTkButton(search_frame, text="Clear", command=self.load_items).pack(side="left", padx=5)

        # Table frame to show items using Treeview for better appearance
        from tkinter import ttk
        self.tree = ttk.Treeview(self, columns=("code", "name", "company", "qty"), show="headings", height=15)
        self.tree.heading("code", text="Item Code")
        self.tree.heading("name", text="Item Name")
        self.tree.heading("company", text="Company Name")
        self.tree.heading("qty", text="Quantity")
        self.tree.column("code", width=120, anchor="center")
        self.tree.column("name", width=220, anchor="center")
        self.tree.column("company", width=220, anchor="center")
        self.tree.column("qty", width=100, anchor="center")
        self.tree.pack(padx=10, pady=20, fill="both", expand=True)

    def load_items(self, filter_func=None):
        for row in self.tree.get_children():
            self.tree.delete(row)
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        items = [line.split(",") for line in lines]
        if filter_func:
            items = [item for item in items if filter_func(item)]
        for itm in items:
            self.tree.insert("", "end", values=(itm[0], itm[1], itm[2], itm[3]))

    def add_item_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add Item")
        dialog.geometry("350x300")
        entries = {}

        fields = ["Item Code", "Item Name", "Company Name", "Quantity"]
        for i, field in enumerate(fields):
            ctk.CTkLabel(dialog, text=field).pack(pady=(15 if i == 0 else 5, 0))
            ent = ctk.CTkEntry(dialog, width=250)
            ent.pack()
            entries[field] = ent

        def save():
            values = [entries[field].get().strip() for field in fields]
            if any(not v for v in values):
                ctk.CTkMessagebox(dialog, title="Error", message="All fields must be filled!", icon="warning")
                return
            try:
                int(values[3])  # Validate quantity as int
            except:
                ctk.CTkMessagebox(dialog, title="Error", message="Quantity must be an integer!", icon="warning")
                return
            with open(self.filename, "a") as f:
                f.write(",".join(values) + "\n")
            self.load_items()
            dialog.destroy()

        ctk.CTkButton(dialog, text="Save", command=save).pack(pady=20)

    def update_item_dialog(self):
        selected = self.tree.selection()
        if not selected:
            ctk.CTkMessagebox(self, title="Error", message="Select one item to update", icon="warning")
            return
        cur_values = self.tree.item(selected[0])["values"]

        dialog = ctk.CTkToplevel(self)
        dialog.title("Update Item")
        dialog.geometry("350x300")
        entries = {}

        fields = ["Item Code", "Item Name", "Company Name", "Quantity"]
        for i, field in enumerate(fields):
            ctk.CTkLabel(dialog, text=field).pack(pady=(15 if i == 0 else 5, 0))
            ent = ctk.CTkEntry(dialog, width=250)
            ent.insert(0, cur_values[i])
            ent.pack()
            entries[field] = ent

        def save():
            values = [entries[field].get().strip() for field in fields]
            if any(not v for v in values):
                ctk.CTkMessagebox(dialog, title="Error", message="All fields must be filled!", icon="warning")
                return
            try:
                int(values[3])
            except:
                ctk.CTkMessagebox(dialog, title="Error", message="Quantity must be an integer!", icon="warning")
                return

            updated_data = []
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == cur_values[0]:
                        updated_data.append(",".join(values) + "\n")
                    else:
                        updated_data.append(line)
            with open(self.filename, "w") as f:
                f.writelines(updated_data)
            self.load_items()
            dialog.destroy()

        ctk.CTkButton(dialog, text="Update", command=save).pack(pady=20)

    def delete_item_dialog(self):
        selected = self.tree.selection()
        if not selected:
            ctk.CTkMessagebox(self, title="Error", message="Select one item to delete", icon="warning")
            return
        item = self.tree.item(selected[0])["values"]
        confirmed = ctk.CTkMessagebox(self, title="Confirm Delete",
                                     message=f"Are you sure you want to delete item '{item[1]}'?",
                                     icon="question", option_1="Yes", option_2="No")
        if confirmed == "Yes":
            updated_data = []
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] != item[0]:
                        updated_data.append(line)
            with open(self.filename, "w") as f:
                f.writelines(updated_data)
            self.load_items()

    def search_item(self):
        query = self.search_var.get().lower().strip()
        if not query:
            self.load_items()
            return
        def filter_func(item):
            return (query in item[0].lower() or
                    query in item[1].lower() or
                    query in item[2].lower())
        self.load_items(filter_func)


if __name__ == "__main__":
    app = ModernDSMS()
    app.mainloop()