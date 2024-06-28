import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validate_password(password):
    if (len(password) >= 8 and
        any(c.isdigit() for c in password) and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c in string.punctuation for c in password)):
        return True
    return False

# Demo
if __name__ == "__main__":
    generated_password = generate_password()
    print("Generated Password:", generated_password)
    print("Password Validation:", validate_password(generated_password))