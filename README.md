# 🏬 Department Store Management System (DSMS)

A **Department Store Management System (DSMS)** in Python — simple, fast, and efficient command-line software to manage the inventory and sales of your department store!

---

## ✨ Overview

DSMS lets store admins easily:
- **Add**, **View**, **Update**, and **Delete** items
- All data is securely stored in a file (`book.txt`) for persistence

---

## 🚀 Features

| Feature        | Description                                                                 |
|:--------------:|:---------------------------------------------------------------------------:|
| ➕ **Add Item**    | Enter Item Code, Name, Company, & Quantity — stored in `book.txt`           |
| 👀 **View Items**  | See all items in a neatly formatted table                                  |
| ✏️ **Update Item** | Modify any item’s details using the Item Code                              |
| ❌ **Delete Item** | Remove any item by Item Code — error shown if code not found               |
| 🚪 **Exit**        | Exit the program securely                                                  |

---

## 🧑‍💻 How It Works

- The `DepartmentStore` class manages all operations: add, view, update, delete.
- **Control Panel:** Easy menu for quick admin actions
- **File Operations:** All data handled in `book.txt` for easy access and reliability

---

## 🛠️ Installation & Usage

```bash
# 1. Clone the Repository
git clone https://github.com/your-username/Department-Store-Management-System.git
cd Department-Store-Management-System

# 2. Run the Program
python dsms.py
```

---

## 📂 File Structure

```
Department-Store-Management-System/
│
├── dsms.py       # Main Python source code
├── book.txt      # Stores all items (auto-created if absent)
└── README.md     # Documentation
```

---

## 📋 Sample Control Panel

```
==== Department Store Management System ====
1. Add Item
2. View Items
3. Update Item
4. Delete Item
5. Exit
```

---

## ⚡ Future Improvements

- Add a GUI (Tkinter / PyQt)
- Implement search & filter options
- Add login authentication for admin
- Replace text file with SQLite/SQL database for scalability

---

## 📜 License

This project is **open source** and available under the [MIT License](LICENSE).

---

> 🚩 **Contributions Welcome!**  
> Feel free to fork, open issues, or submit pull requests to improve DSMS 😊
