# SonOfPassword_verify

SonOfPassword_verify is a simple yet effective password complexity checker tool written in Python. It assesses the strength of a password based on length, use of uppercase and lowercase letters, digits, and special characters. The tool provides immediate feedback to help users improve their passwords.

## How It Works

### Input
The user is prompted to enter a password for evaluation.

### Evaluation Criteria
The password is assessed based on the following criteria:
1. Minimum length of 8 characters.
2. At least one uppercase letter.
3. At least one lowercase letter.
4. At least one digit.
5. At least one special character from the following: `@, $, !, %, *, ?, &, #`.

### Feedback
The tool evaluates the password and provides a score out of 5, indicating how many criteria were met. It also gives detailed feedback on how to improve the password if any criteria are missing.

### Strength Levels
The password strength is categorized into the following levels:
- **Very Strong**: 5/5 criteria met
- **Strong**: 4/5 criteria met
- **Moderate**: 3/5 criteria met
- **Weak**: 2/5 criteria met
- **Very Weak**: 1 or 0 criteria met

## How to Run

1. Clone the repository or copy the script into your environment.
2. Run the tool by executing the script in your terminal:
   ```bash
   python password_checker.py
