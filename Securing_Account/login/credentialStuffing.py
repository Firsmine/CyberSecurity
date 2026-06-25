"""
this is a simulation if your email password leaked and you were using the same password on the other platform so the attacker can login into the platform with your stollen email password.
"""

# database
gmail = {
    "user@mail.com":"user1234",
    "me@mail.com":"meIam1234",
    "you@mail.com":"you1234",
    "them@mail.com":"them1234",
    "name@mail.com":"name1234"
}
github = {
    "user@mail.com":"user1234",
    "me@mail.com":"meIam1234",
    "you@mail.com":"you1234",
    "them@mail.com":"them1234",
    "name@mail.com":"name1234"
}

while True:
    stollen_email = input("\nEmail\t\t: ").strip().lower()
    stollen_password = input("Password\t: ").strip()

    if stollen_email in github:
        if github[stollen_email]==stollen_password:
            print("Login success!")
        else:
            print("Wrong password!")
    else:
        print("Account not found!")
        
    if input("\nTry another credential? (y/n): ").lower()!= "y":
        print("Gbye!")
        break