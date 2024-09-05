import smtplib
import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email (email, otp):
    sender_email = "deshmukhsachin266@gmail.com"
    sender_password="adtrvwjflygpouxd"
    message=f"Subject: OTP Verification\n\nYour OTP is: {otp}"
    
    try:
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
            print("OTP sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))
def verify_otp(email, entered_otp, generated_otp):
    if entered_otp == generated_otp:
        print("OTP verification successful!")
    else: print("OTP verification failed!")

otp=generate_otp() 
email=input("enter your email address")
send_email(email,otp)
entered_otp=input("Enter your otp recevier") 

verify_otp(email, entered_otp, otp)