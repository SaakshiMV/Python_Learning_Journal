import smtplib

# Your email credentials (use app password for safety)
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

SUBJECT = "Test Email"
BODY = "Hello! This is an automated email from Python."

def send_emails():
    try:
        with open("contacts.txt", "r") as file:
            recipients = file.read().splitlines()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        for recipient in recipients:
            message = f"Subject: {SUBJECT}\n\n{BODY}"
            server.sendmail(EMAIL, recipient, message)
            print(f"Email sent to {recipient}")

        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    send_emails()
