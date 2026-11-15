import customtkinter as ctk
import random
import smtplib #library to send email
from email.message import EmailMessage #library to create email message

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Reset Password")
app.geometry("340x440")
app.resizable(False, False)

# Store the generated OTP globally so both functions can access it
generated_otp = None

# Title
ctk.CTkLabel(app, text="Reset Password", font=("Arial", 22, "bold")).pack(pady=(25, 15))

# Input Fields
email_entry = ctk.CTkEntry(app, width=220, placeholder_text="Enter your email")
email_entry.pack(pady=6)

new_password_entry = ctk.CTkEntry(app, width=220, placeholder_text="Enter new password", show="*")
new_password_entry.pack(pady=6)

otp_entry = ctk.CTkEntry(app, width=220, placeholder_text="Enter 6-digit OTP")
otp_entry.pack(pady=6)

status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=6)


def send_otp():
    global generated_otp
    to_email = email_entry.get().strip()

    if not to_email:
        status_label.configure(text="Please enter your email first", text_color="orange")
        return

    # Generate 6-digit OTP
    generated_otp = "".join(str(random.randint(0, 9)) for _ in range(6))

    sender_email = "**************"
    app_password = "**********"  # Replace with your Gmail App Password

    msg = EmailMessage()
    msg["Subject"] = "OTP for Password Reset"
    msg["From"] = sender_email
    msg["To"] = to_email
    msg.set_content(f"Your OTP is: {generated_otp}")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        status_label.configure(text="OTP sent to your email!", text_color="skyblue")
    except Exception as e:
        status_label.configure(text="Failed to send OTP. Check email/settings.", text_color="red")
        print("SMTP Error:", e)


def handle_reset():
    email = email_entry.get().strip()
    new_pass = new_password_entry.get().strip()
    entered_otp = otp_entry.get().strip()

    if not email or not new_pass or not entered_otp:
        status_label.configure(text="Please fill in all fields", text_color="orange")
        return

    if generated_otp is None:
        status_label.configure(text="Please click 'Send OTP' first", text_color="orange")
        return

    if entered_otp != generated_otp:
        status_label.configure(text="Invalid OTP. Please try again.", text_color="red")
        return

    # TODO: Connect with your database.py update query here
    status_label.configure(text="Password reset successfully!", text_color="green")


# Buttons
ctk.CTkButton(app, text="Send OTP", width=140, command=send_otp).pack(pady=(10, 6))
ctk.CTkButton(app, text="Update Password", width=140, command=handle_reset).pack(pady=6)
ctk.CTkButton(
    app,
    text="Close",
    fg_color="transparent",
    font=("Arial", 11, "underline"),
    command=app.destroy,
).pack(pady=(6, 0))

app.mainloop()
