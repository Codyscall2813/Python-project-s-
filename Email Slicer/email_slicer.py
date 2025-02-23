def email_slicer(email):
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        raise ValueError("Invalid email address.")


if __name__ == "__main__":
    email = input("Enter your email address: ")
    try:
        username, domain = email_slicer(email)
        print(f"    Your username is: {username}")
        print(f"    Your domain is: {domain}")
    except ValueError as e:
        print(e)
