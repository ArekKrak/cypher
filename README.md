# 🔐 Cypher

![Python](https://img.shields.io/badge/Python-Language-white?logo=python&logoColor=blue&style=flat)
![VS Code](https://img.shields.io/badge/VS_Code-Editor-007ACC?logo=visualstudiocode&logoColor=white&style=flat)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white&style=flat)](https://github.com/ArekKrak/cypher)

A Python contact form program that encrypts user input using the **Caesar cipher algorithm (key = 15)**.  
Built as a **capstone project** during one of my early bootcamps, it demonstrates my first steps into Python development and cryptography.

---

## Project Overview

**Context:**  
The Caesar cipher is one of the simplest encryption techniques, shifting letters by a fixed number. This project uses a **shift of 15**, ensuring both uppercase and lowercase letters are handled properly while leaving punctuation and spaces intact.

**Your role:**  
Write a Python program that:
- Accepts user input from a “contact form” (Subject, Message, Email).
- Encrypts each input line using ASCII values and modulo arithmetic.
- Outputs the encrypted version of each field.

**Main Features Implemented:**
- Case-sensitive Caesar cipher with wrap-around alphabet.
- Preserves punctuation, numbers, and whitespace.
- User-friendly “contact form” format in the terminal.
- Error handling for interruptions (`KeyboardInterrupt`).

---

## Tech Stack

- **Python 3**
- **Tools**: Visual Studio Code, Git, GitHub

---

## Project Structure

```
cypher/
├── cypher-python.py    # Main program logic
└── README.md           # Project documentation
```

---

## How It Works

1. The program greets the user with a formatted “Contact Form”.
2. Each field (Subject, Message, Email) is taken as input.
3. The Caesar cipher function (`+15 shift`) encrypts the text character by character.
4. The encrypted string is printed to the console.

---

## How to Run

1. Clone the repository:

```
git clone https://github.com/ArekKrak/cypher.git
cd cypher
```
2. Run the program:
```
python3 cypher-python.py
```

---
## Example Output

![Demo animation](cypher.gif)

---
## Key Concepts Demonstrated

- ASCII manipulation with ```ord()``` and ```chr()```
- Modular arithmetic in Python
- Control flow with ```if```/```elif```/```else```
- String building and concatenation
- Basic error handling (```try/except```)
- Command-line interaction

---
## Future Improvements

- Add a decipher function for decryption.
- Allow the user to set a custom key instead of a fixed ```15```.
- Extend support to non-ASCII alphabets.
- Package as a simple CLI tool with arguments.

---
## Acknowledgements

- Project brief provided by my course provider (HyperionDev).
- Built as one of my earliest Python projects, intended for learning purposes rather than real-world cryptography.

---
## Contact
If you're a recruiter, mentor, or fellow developer interested in collaboration or feedback:

**Arek Krakowiak**  
[369arek12@protonmail.com](mailto:369arek12@protonmail.com)

---

Thank you for viewing this project!