# SecuTools: An Automated Security Toolkit

SecuTools is a Python-based automation tool designed to streamline and enhance various security-related functions. This tool provides functionalities such as password generation and validation, and network scanning. The aim is to make security tasks more efficient and accessible for cybersecurity professionals and enthusiasts.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Password Management](#password-management)
  - [Network Scanning](#network-scanning)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Authors and Acknowledgements](#authors-and-acknowledgements)
- [Contact](#contact)

## Installation

To set up SecuTools on your local machine, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Zyber369/SecuTools.git
    ```

2. Navigate to the project directory:

    ```bash
    cd SecuTools
    ```

3. (Optional) Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
## Credits

SecuTools was developed with the help of several libraries, tools, and resources. We would like to acknowledge their contributions to the project:

- **Python**: The core language used to develop SecuTools.
- **Standard Library**:
  - `random` and `string`: Used for password generation and validation.
  - `socket`: Used for network scanning functionalities.
- **Git and GitHub**: For version control and repository hosting.
- **PyCharm**: Integrated Development Environment (IDE) used for writing and debugging the code.
- **pip**: Package installer for managing dependencies.
- **Markdown**: For writing documentation, including this README file.

### Libraries

- **Python Standard Library**:
  - `random`: Used for generating random passwords.
  - `string`: Used for character manipulation in password generation.
  - `socket`: Used for network scanning to check for open ports on devices.

### Tools

- **Git**: For version control and collaboration.
- **GitHub**: For hosting the project's repository and facilitating collaboration.
- **PyCharm**: As the primary IDE for developing and testing the project.
- **pip**: To install and manage Python packages and dependencies.

### Resources

- **Python Documentation**: [Python Docs](https://docs.python.org/3/)
- **Socket Programming in Python**: [Python Socket Programming](https://docs.python.org/3/howto/sockets.html)
- **Git Documentation**: [Git Docs](https://git-scm.com/doc)
- **Markdown Guide**: [Markdown Guide](https://www.markdownguide.org/)
## Usage

### Password Management

The password management module allows you to generate strong, random passwords and validate their strength.

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
print("Generated Password:", generate_password())
print("Password Validation:", validate_password("P@ssw0rd123"))

