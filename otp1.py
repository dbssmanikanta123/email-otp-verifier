import smtplib
import random
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_otp():
    """Generates a secure 6-digit OTP."""
    return random.randint(100000, 999999)

def send_otp(sender_email, receiver_email, otp):
    """Sends OTP from sender to receiver email securely."""
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "OTP for Verification"
    body = f"Your OTP for verification is: {otp}\n\nDo not share it with anyone."
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        email_password = getpass.getpass("Enter your email's App Password: ")

        server.login(sender_email, email_password)
        server.send_message(msg)
        server.quit()
        print(f"\n OTP successfully sent to {receiver_email}")

    except smtplib.SMTPAuthenticationError:
        print("Authentication Error: Check your email and App Password.")
        exit()
    except Exception as e:
        print(f" An error occurred: {e}")
        exit()

def verify_otp(correct_otp):
    """Verifies the OTP with 3 retry attempts."""
    for attempt in range(3):
        try:
            user_otp = int(input("\nEnter the OTP received: "))
            if user_otp == correct_otp:
                print(" OTP Verification Successful!")
                return True
            else:
                print("Invalid OTP. Try again.")
        except ValueError:
            print("Please enter a valid numeric OTP.")
    
    print("Too many incorrect attempts. Verification failed.")
    return False

if __name__ == "__main__":
    sender_email = "manikantacharan700@gmail.com"
    receiver_email = "srinivas@codegnan.com"
    
    otp = generate_otp()
    send_otp(sender_email, receiver_email, otp)
    verify_otp(otp)
