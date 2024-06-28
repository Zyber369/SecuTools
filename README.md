# SecuTools: An Automated Security Toolkit

## Project Description
SecuTools is a Python-based automation tool designed to streamline and enhance various security-related functions. This tool provides functionalities such as password generation, file encryption and decryption, network scanning, and vulnerability assessment. The aim is to make security tasks more efficient and accessible for cybersecurity professionals and enthusiasts.

## Project Plan and Scope

### Project Title
SecuTools: An Automated Security Toolkit

### Scope

1. **Password Management**:
   - Generate strong, random passwords.
   - Validate password strength.

2. **File Encryption and Decryption**:
   - Encrypt files using symmetric encryption (AES).
   - Decrypt files with the corresponding key.

3. **Network Scanning**:
   - Scan local networks for active devices.
   - Identify open ports on devices.

4. **Vulnerability Assessment**:
   - Basic vulnerability scan for common vulnerabilities (e.g., using Nmap).
   - Generate a report of identified vulnerabilities.

### Project Phases

1. **Phase 1: Planning and Design**
   - Define detailed requirements and functionalities.
   - Design the software architecture.
   - Set up the GitHub repository.

2. **Phase 2: Development**
   - Implement password management functions.
   - Develop file encryption and decryption functionalities.
   - Create network scanning capabilities.
   - Build basic vulnerability assessment features.

3. **Phase 3: Testing and Validation**
   - Perform unit and integration testing.
   - Validate the functionalities with test cases.

4. **Phase 4: Documentation and Demonstration**
   - Document the code and usage instructions.
   - Create a demonstration script or video.
   - Finalize and deliver the project.

## GitHub Repository

The project's GitHub repository can be found [here](https://github.com/Zyber369/SecuTools).

## Tool Demonstration

### 1. Password Management

```python
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
