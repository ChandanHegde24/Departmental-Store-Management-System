🏬 Department Store Management System (DSMS)
A Department Store Management System (DSMS) in Python is a command-line software tool used to manage the inventory and sales of items in a department store.

This simple system provides store admins the ability to:

Add Items

View Items

Update Items

Delete Items

All data is stored in a file (book.txt) for persistence.

🔹 Features
➕ Add Item
Prompts the user for:

Item Code

Item Name

Company Name

Quantity (No. of items)

Stores this data in book.txt.

After adding, asks:
"Do you want to Add Another Item (y/n)?"

👀 View Items
Displays information of all items in the store in tabular format.

✏️ Update Item
Requests the Item Code from the user.

If found, allows editing:

Item Code

Item Name

Company Name

Quantity

Updates changes inside book.txt.

❌ Delete Item
Requests the Item Code from the user.

If found, deletes the item from the file.

If the entered code is invalid, an error message is displayed.

🚪 Exit
Program exits when the user selects the Exit option from the control panel.

🔹 Approach
The DepartmentStore class is created to perform add, view, update, and delete operations.

A Control Panel displays a menu with options for admin operations.

All data is handled with file operations (book.txt).

Update works by locating the item and rewriting updated info into the file.

Delete works by rewriting the file without the deleted item entry.

🛠️ Installation & Usage
1. Clone the Repository
bash
git clone https://github.com/your-username/Department-Store-Management-System.git
cd Department-Store-Management-System

3. Run the Program
bash
python dsms.py

📂 File Structure
text
Department-Store-Management-System/
│
├── dsms.py       # Main Python source code
├── book.txt      # File to store all items (auto-created if absent)
└── README.md     # Documentation

💻 Sample Control Panel
text
==== Department Store Management System ====
1. Add Item
2. View Items
3. Update Item
4. Delete Item
5. Exit
   
⚡ Future Improvements
Add GUI using Tkinter / PyQt.

Implement search and filter options.

Add login authentication for admin.

Replace text file with SQLite/SQL database for scalability.

📜 License
This project is open source and available under the MIT License.
