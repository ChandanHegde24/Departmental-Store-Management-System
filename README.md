# Department Store Management System (ModernDSMS)

A simple desktop application built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for managing items in a department store. You can add, update, delete, and search items stored in a plain text file (`book.txt`).

## Features

- **Modern UI:** Uses CustomTkinter for a modern, themed interface.
- **CRUD Operations:** Add, update, and delete items.
- **Search:** Find items by code, name, or company.
- **Persistent Storage:** Items stored in a file (`book.txt`).
- **Easy Setup:** No database required; just Python and CustomTkinter.

## Requirements

- Python 3.7+
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Tkinter (bundled with Python)

Install CustomTkinter via pip:

```bash
pip install customtkinter
```

## Usage

1. **Clone this repository** or copy the code into a file named `modern_dsms.py`.
2. Make sure a `book.txt` file exists in the same directory (it will be created automatically if missing).
3. Run the application:

```bash
python modern_dsms.py
```

## File Format

Items are stored in `book.txt` as comma-separated lines:

```
item_code,item_name,company_name,quantity
```

Example:

```
101,Detergent,ACME,50
102,Soap,GoodCare,30
```

## Main Components

- **Add Item:** Enter item details in a pop-up and save.
- **Update Item:** Select an item in the table, edit details in a pop-up, and update.
- **Delete Item:** Select an item and confirm deletion.
- **Search:** Enter a query to find items by code, name, or company. Hit "Clear" to reset.

## Screenshots

*(Add your own screenshots here)*

## Notes

- The UI uses the system theme by default; you can change between "dark" or "light" in the code.
- All data is stored locally in `book.txt`. No cloud or database integration.

## License

MIT License (or specify your own)

---

**Author:** Chandan Hegde  
**Contact:** [Your GitHub Profile](https://github.com/ChandanHegde24)
