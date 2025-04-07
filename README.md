# email-otp-verifier
A simple yet secure Python-based OTP (One Time Password) verification system using email. This script generates a random 6-digit OTP, sends it to the receiver’s email using Gmail SMTP, and verifies user input through the console. Designed for authentication, identity verification, and basic two-factor login systems.
Key Features:
OTP Generation

Uses the random module to generate a secure 6-digit numeric OTP.

Ensures OTP is in the range of 100000 to 999999.

Email Sending (SMTP)

Constructs an email with the OTP using smtplib and email.mime.

Sends the email securely via Gmail's SMTP server (smtp.gmail.com on port 587).

Requires the sender’s App Password (for Gmail security) which is securely entered using getpass.

OTP Verification

Prompts the user to input the OTP they received via email.

Allows up to 3 attempts to enter the correct OTP.

Validates the input to ensure it's a 6-digit number.

Displays success or failure messages accordingly.

Modules Used:
smtplib: For sending email via SMTP.

random: For OTP generation.

getpass: To securely input the email app password.

email.mime: For formatting the email content.

How It Works:
Setup: Specify the sender and receiver email addresses.

Generate OTP: A 6-digit OTP is created.

Send OTP: The OTP is emailed from sender to receiver.

User Input: The user is asked to enter the OTP.

Verify: If the entered OTP matches the generated one within 3 attempts, verification succeeds.

Security Notes:
Use App Passwords instead of your main email password (especially for Gmail).

Never log or print OTPs or passwords in real-world applications.

In production, consider rate-limiting and more robust error handling.
