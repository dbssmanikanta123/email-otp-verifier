# email-otp-verifier
A simple yet secure Python-based OTP (One Time Password) verification system using email. This script generates a random 6-digit OTP, sends it to the receiver’s email using Gmail SMTP, and verifies user input through the console. Designed for authentication, identity verification, and basic two-factor login systems.
Features:
Multi-user support: The script allows sending OTPs to multiple users at once.
Email integration: Uses Gmail's SMTP server to send OTPs.
OTP generation: A random 4-digit OTP is generated for each user.
Verification: The user is prompted to enter the OTP they received. They have up to 3 attempts to enter the correct OTP.
Failure handling: After 3 incorrect attempts, the verification for that user fails, and the process is terminated for that user.
Requirements:
Python 3.x
The smtplib library (built-in with Python)
email.mime library (built-in with Python)
How to Use:
Run the script.
Enter the number of users you want to send OTPs to.
For each user, input their name and email address.
The script will send an OTP to the email address and ask the user to input it.
The user will have 3 attempts to input the correct OTP. If successful, the user will receive a success message. If the OTP is incorrect after 3 attempts, the verification will fail.
Security Considerations:
Email Credentials: The script requires access to an email account (abc@gmail.com in the example). You should replace this with your own email credentials for production use. It's highly recommended to use an App Password for your Gmail account instead of your main account password for security reasons.
