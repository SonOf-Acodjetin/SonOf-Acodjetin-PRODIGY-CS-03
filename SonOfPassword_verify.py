import re

def password_complexity_checker(password):
    # Criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password)
    lower_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_criteria = re.search(r'[@$!%*?&#]', password)
    
    # Score Calculation
    score = sum([length_criteria, bool(upper_criteria), bool(lower_criteria), bool(digit_criteria), bool(special_criteria)])
    
    # Strength Feedback
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Detailed Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character (@, $, !, %, *, ?, &, #).")
    
    return {
        'strength': strength,
        'score': score,
        'feedback': feedback
    }

def main():
    print("Password Complexity Checker Tool")
    password = input("Enter your password: ")
    result = password_complexity_checker(password)
    
    print(f"\nPassword Strength: {result['strength']}")
    print(f"Score: {result['score']}/5")
    
    if result['feedback']:
        print("Feedback:")
        for suggestion in result['feedback']:
            print(f"- {suggestion}")
    else:
        print("Great! Your password meets all complexity criteria.")

if __name__ == "__main__":
    main()
