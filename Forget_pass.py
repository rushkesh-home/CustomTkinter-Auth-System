import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Reset Password")
app.geometry("340x360")
app.resizable(False, False)

# Title
ctk.CTkLabel(app, text="Reset Password", font=("Arial", 22, "bold")).pack(pady=(25, 15))

# Input Fields
email_entry = ctk.CTkEntry(app, width=220, placeholder_text="Enter your email")
email_entry.pack(pady=6)

new_password_entry = ctk.CTkEntry(app, width=220, placeholder_text="Enter new password", show="*")
new_password_entry.pack(pady=6)

status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=4)

def handle_reset():
    email = email_entry.get().strip()
    new_pass = new_password_entry.get().strip()

    if not email or not new_pass:
        status_label.configure(text="Please fill in all fields", text_color="orange")
        return

    # TODO: Connect with your database.py update query here
    status_label.configure(text="Password reset successfully!", text_color="green")

# Update Button
ctk.CTkButton(app, text="Update Password", width=140, command=handle_reset).pack(pady=15)

# Back / Close Button
ctk.CTkButton(
    app,
    text="Close",
    fg_color="transparent",
    font=("Arial", 11, "underline"),
    command=app.destroy
).pack()

app.mainloop()