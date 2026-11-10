import os
import sys
import subprocess
import customtkinter as ctk
from database import verify_user  # Connects to your MySQL verification function

# Resolve paths to open Signup and Forgot Password windows
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIGNUP_SCRIPT = os.path.join(BASE_DIR, "Signup.py")
FORGOT_PASS_SCRIPT = os.path.join(BASE_DIR, "Forget_pass.py")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sign In")
app.geometry("340x390")
app.resizable(False, False)

# --- Functions ---
def open_signup():
    subprocess.Popen([sys.executable, SIGNUP_SCRIPT])

def open_forgot_password():
    subprocess.Popen([sys.executable, FORGOT_PASS_SCRIPT])

def handle_signin():
    email = email_entry.get().strip()
    pwd = password_entry.get().strip()

    if not email or not pwd:
        status_label.configure(text="Please fill in all fields", text_color="orange")
        return

    # Verify against MySQL database
    if verify_user(email, pwd):
        status_label.configure(text="Login successful!", text_color="green")
        # Optional: app.destroy() and open your main dashboard here
    else:
        status_label.configure(text="Invalid email or password", text_color="red")

# --- UI Elements ---

# Title
ctk.CTkLabel(app, text="Sign In", font=("Arial", 22, "bold")).pack(pady=(25, 15))

# Email Input
email_entry = ctk.CTkEntry(app, width=220, placeholder_text="Email")
email_entry.pack(pady=6)

# Password Input
password_entry = ctk.CTkEntry(app, width=220, placeholder_text="Password", show="*")
password_entry.pack(pady=6)

# Forgot Password Link
ctk.CTkButton(
    app,
    text="Forgot password?",
    fg_color="transparent",
    hover=False,
    cursor="hand2",
    font=("Arial", 11, "underline"),
    command=open_forgot_password
).pack(pady=(2, 5))

# Status / Error Message
status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=2)

# Sign In Button
ctk.CTkButton(app, text="Sign In", width=140, command=handle_signin).pack(pady=10)

# Sign Up Link
ctk.CTkButton(
    app,
    text="Don't have an account? Sign up",
    fg_color="transparent",
    hover=False,
    cursor="hand2",
    font=("Arial", 11, "underline"),
    command=open_signup
).pack(pady=(5, 10))

app.mainloop()