"""
this is a simple simulation how login with otp
"""

import secrets, time

users = {
    "user@mail.com":"user1234",
    "me@mail.com":"meIam1234",
    "you@mail.com":"you1234",
    "them@mail.com":"them1234",
    "name@mail.com":"name1234"
}

def generate_otp():
        otp = ""
        for i in range(6):
            otp += str(secrets.randbelow(10))
        return otp
    
while True:
    email = input("\nEmail\t\t: ")
    password = input("Password\t: ")

    if email in users and users[email] == password:
        otp = generate_otp()
        print(f"\nOTP\t\t: {otp}")
        
        created_time = time.time()
        
        attempt = 3
        while attempt > 0:
            user_otp = input("\nEnter OTP\t: ")
        
            if time.time() - created_time > 30:
                print("OTP expired.")
                break
            if user_otp == otp:
                print("Login Success!")
                break
            else: 
                attempt -= 1
                print("Invalid OTP!")
                continue
        else:
            print("Too many failed attempts!")
    else: 
        print("Invalid Credentials!")
    
    if input("\nTry to login again? (y/n): ").lower() != "y":
        print("Gbye!")
        break