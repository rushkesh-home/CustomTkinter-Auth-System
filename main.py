import sys
import subprocess
import customtkinter as ctk
from signin import signin  # Imports your existing signin function

app = ctk.CTk()
app.geometry("320x370")
app.title("Login")

# --- Login Logic ---
def handle_login():
    user_email = email_entry.get().strip()
    user_password = password_entry.get().strip()

    if not user_email or not user_password:
        status_label.configure(text="Please fill in all fields", text_color="orange")
        return

    # Call your signin function
    if signin(user_email, user_password):
        status_label.configure(text="Access granted! Opening dashboard...", text_color="green")
        # Optional: app.destroy() and open your dashboard window here
    else:
        status_label.configure(text="Access denied. Invalid credentials.", text_color="red")

# --- UI Layout ---
ctk.CTkLabel(app, text="Sign In", font=("Arial", 22, "bold")).pack(pady=(20, 15))

email_entry = ctk.CTkEntry(app, width=220, placeholder_text="Enter email")
email_entry.pack(pady=5)

password_entry = ctk.CTkEntry(app, width=220, placeholder_text="Enter password", show="*")
password_entry.pack(pady=5)

# Status message (Shows success/failure directly on the window)
status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=2)

# Forgot Password
ctk.CTkButton(
    app,
    text="Forgot password?",
    fg_color="transparent",
    font=("Arial", 11, "underline"),
    command=lambda: subprocess.Popen([sys.executable, "Forget_pass.py"])
).pack(pady=(0, 10))

# Login Button
ctk.CTkButton(
    app,
    text="Login",
    width=140,
    command=handle_login
).pack(pady=5)

# Sign Up Link
ctk.CTkButton(
    app,
    text="Don't have an account? Sign up",
    fg_color="transparent",
    font=("Arial", 11, "underline"),
    command=lambda: subprocess.Popen([sys.executable, "Signup.py"])
).pack(pady=(5, 10))

app.mainloop()