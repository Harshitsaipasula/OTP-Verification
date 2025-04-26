import smtplib
import random
import time
from tkinter import messagebox, Tk

def send_otp_to_email(email, otp):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        sender_email = "harshithsaipasula@gmail.com"
        sender_password = "xifj visv eqmy rrfd"

        server.login(sender_email, sender_password)

        subject = "OTP for Your App Access"
        body = f"Your OTP is: {otp}"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(sender_email, email, message)
        server.quit()
        print(f"OTP sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def generate_otp():
    return random.randint(100000, 999999)


def validate_otp(correct_otp):
    attempts = 0
    max_attempts = 3  

    while attempts < max_attempts:
        user_otp = input(f"Enter the OTP (Attempt {attempts + 1} of {max_attempts}): ")
        if user_otp == str(correct_otp):
            display_popup("Access Granted", "Success! You have entered the correct OTP.")
            return True
        else:
            display_popup("Access Denied", "Incorrect OTP. Please try again.")
            attempts += 1
            if attempts == max_attempts:
                display_popup("Access Denied", "You have exhausted all attempts. Please try again later.")
                return False
            time.sleep(1) 

def display_popup(title, message):
    root = Tk()
    root.withdraw()  
    messagebox.showinfo(title, message)
    root.quit()

def main():
    registered_email = input("Enter your registered email address: ")

    otp = generate_otp()
    send_otp_to_email(registered_email, otp)

    if not validate_otp(otp):
        print("OTP verification failed after 3 attempts.")
    else:
        print("OTP verification successful.")

if __name__ == "__main__":
    main()

