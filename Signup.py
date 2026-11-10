import os
import sys
import subprocess
import customtkinter as ctk
from auth import signup  # Backend signup function

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIGNIN_SCRIPT = os.path.join(BASE_DIR, "signin.py")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sign Up")
app.geometry("340x430")
app.resizable(False, False)

# --- Functions ---
def open_signin():
    app.destroy()  # Closes Sign Up window
    subprocess.Popen([sys.executable, SIGNIN_SCRIPT])  # Re-opens Sign In

def handle_signup():
    user = username_entry.get().strip()
    email = email_entry.get().strip()
    pwd = password_entry.get().strip()

    if not user or not email or not pwd:
        status_label.configure(text="Please fill in all fields", text_color="orange")
        return

    try:
        signup(user, email, pwd)
        status_label.configure(text="Account created successfully!", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Error: {e}", text_color="red")

# --- UI Elements ---

# Title
ctk.CTkLabel(app, text="Sign Up", font=("Arial", 22, "bold")).pack(pady=(25, 15))

# Input Fields
username_entry = ctk.CTkEntry(app, width=220, placeholder_text="Username")
username_entry.pack(pady=6)

email_entry = ctk.CTkEntry(app, width=220, placeholder_text="Email")
email_entry.pack(pady=6)

password_entry = ctk.CTkEntry(app, width=220, placeholder_text="Password", show="*")
password_entry.pack(pady=6)

# Status message
status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=4)

# Sign Up Button
ctk.CTkButton(app, text="Sign Up", width=140, command=handle_signup).pack(pady=10)

# Back to Sign In Link
ctk.CTkButton(
    app,
    text="Already have an account? Sign in",
    fg_color="transparent",
    hover=False,
    cursor="hand2",
    font=("Arial", 11, "underline"),
    command=open_signin
).pack(pady=(5, 10))

app.mainloop()