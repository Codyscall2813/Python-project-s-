import csv
from email.message import EmailMessage
import smtplib

def get_credentials(filepath):
    """Read email credentials from a file."""
    try:
        with open(filepath, "r") as f:
            email_address = f.readline().strip()
            email_pass = f.readline().strip()
        return email_address, email_pass
    except FileNotFoundError:
        print("Credentials file not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading credentials: {e}")
        raise

def login(email_address, email_pass, s):
    """Log in to the SMTP server."""
    try:
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(email_address, email_pass)
        print("Logged in successfully.")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and password.")
        raise
    except Exception as e:
        print(f"An error occurred during login: {e}")
        raise

def send_mail():
    """Send an email to a list of recipients."""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_address, email_pass = get_credentials("Collection/Email Automation/credentials.txt")
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as s:
            login(email_address, email_pass, s)

            # Message details
            subject = "Your Subject Here"
            body = """\
Hello,

This is a test email sent from Python!

Best regards,
Your Name"""

            message = EmailMessage()
            message.set_content(body)
            message['Subject'] = subject
            message['From'] = email_address

            with open("emails.csv", newline="") as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for email in spamreader:
                    if email:
                        recipient = email[0].strip()
                        message['To'] = recipient
                        s.send_message(message)
                        print(f"Email sent to {recipient}")

            print("All emails sent successfully.")

    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_mail()
