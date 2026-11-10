# CustomTkinter Authentication System

A clean, modern desktop authentication GUI built with Python and [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). Features a dark-themed interface for Sign In, Account Registration, and Password Reset, hooked to a modular backend and database.

---

## Features

- **Modern Dark UI:** Responsive and modern dark mode styling powered by CustomTkinter.
- **Sign In & Sign Up:** Multi-window authentication workflow with field validation.
- **Password Reset:** Dedicated window for account recovery / password updates.
- **Modular Architecture:** UI forms separated cleanly from authentication logic (`auth.py`) and database management (`database.py`).
- **SQL Integration:** Uses structured queries with `Databse.sql` for user record storage.

---

## Project Structure

```text
Login_Page/
├── main.py            # Entry point / CLI & app launcher
├── signin.py          # Sign In GUI window
├── Signup.py          # Registration GUI window
├── Forget_pass.py     # Password recovery GUI window
├── auth.py            # Core authentication logic (hashing / validation)
├── database.py        # Database connection & query handling
├── Databse.sql        # Database schema / table setup
└── README.md          # Project documentation
