"""
Password Generator & Validator
Author: Liza Bambu
Date: 28 February 2026

Generate secure passwords and validate password strength.
"""

import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_special):
    """
    Generate a secure password with guaranteed character types
    
    Args:
        length (int): Password length
        use_upper (bool): Include uppercase letters
        use_lower (bool): Include lowercase letters
        use_digits (bool): Include numbers
        use_special (bool): Include special characters
        
    Returns:
        str: Generated password or error message
    """
    characters = ""
    password_chars = []
    
    # Build character pool and ensure at least one of each selected type
    if use_upper:
        characters += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))
    
    if use_lower:
        characters += string.ascii_lowercase
        password_chars.append(random.choice(string.ascii_lowercase))
    
    if use_digits:
        characters += string.digits
        password_chars.append(random.choice(string.digits))
    
    if use_special:
        characters += string.punctuation
        password_chars.append(random.choice(string.punctuation))
    
    # Check if any character type was selected
    if characters == "":
        return "Error: No character types selected."
    
    # Check if length is sufficient
    if length < len(password_chars):
        length = len(password_chars)
    
    # Fill remaining length with random characters
    remaining = length - len(password_chars)
    for i in range(remaining):
        password_chars.append(random.choice(characters))
    
    # Shuffle to avoid predictable patterns (like uppercase always first)
    random.shuffle(password_chars)
    
    # Convert list to string
    password = ''.join(password_chars)
    
    return password


def validate_password(password):
    """
    Validate password strength and provide feedback
    
    Args:
        password (str): Password to validate
        
    Returns:
        dict: Validation results with strength and details
    """
    # Check each criterion
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Check for common passwords
    common_passwords = [
        'password', '123456', '12345678', 'qwerty', 'abc123',
        'monkey', 'letmein', 'password1', '123123', 'welcome'
    ]
    is_common = password.lower() in common_passwords
    
    # Calculate score
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    # Override if common password
    if is_common:
        strength = "Weak"
        score = 0
    elif score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {
        "Length OK": length_ok,
        "Has Uppercase": has_upper,
        "Has Lowercase": has_lower,
        "Has Digit": has_digit,
        "Has Special": has_special,
        "Is Common": is_common,
        "Strength": strength,
        "Score": score
    }


def get_password_length():
    """Get valid password length from user"""
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length >= 8:
                return length
            else:
                print("❌ Password must be at least 8 characters!")
        except ValueError:
            print("❌ Please enter a valid number!")


def display_validation_result(result):
    """
    Display validation results in a nice format
    
    Args:
        result (dict): Validation results
    """
    print("\n" + "=" * 60)
    print("  PASSWORD STRENGTH ANALYSIS")
    print("=" * 60)
    
    # Strength with emoji
    strength_emoji = {
        "Strong": "🟢",
        "Medium": "🟡",
        "Weak": "🔴"
    }
    
    emoji = strength_emoji.get(result["Strength"], "⚪")
    print(f"\nStrength: {emoji} {result['Strength']}")
    print(f"Score: {result['Score']}/5")
    
    # Visual bar
    filled = "█" * result['Score']
    empty = "░" * (5 - result['Score'])
    print(f"[{filled}{empty}]")
    
    print("\nDetails:")
    
    # Show each check with symbols
    checks = [
        ("Length OK (8+ characters)", result["Length OK"]),
        ("Has uppercase letters", result["Has Uppercase"]),
        ("Has lowercase letters", result["Has Lowercase"]),
        ("Has numbers", result["Has Digit"]),
        ("Has special characters", result["Has Special"])
    ]
    
    for description, passed in checks:
        symbol = "✓" if passed else "❌"
        print(f"  {symbol} {description}")
    
    if result["Is Common"]:
        print("\n  ⚠️  WARNING: This is a commonly used password!")
    
    print("=" * 60)


def handle_generate():
    """Handle password generation"""
    print("\n" + "-" * 60)
    print("  GENERATE PASSWORD")
    print("-" * 60)
    
    # Get password length
    length = get_password_length()
    
    # Get preferences
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_special = input("Include special characters? (y/n): ").lower() == "y"
    
    # Generate password
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    
    # Display result
    print("\n" + "-" * 60)
    if password.startswith("Error"):
        print(f"  ❌ {password}")
    else:
        print(f"  Generated Password: {password}")
        print("-" * 60)
        print(f"  Length: {len(password)} characters")
        print(f"  Uppercase: {'Yes' if use_upper else 'No'}")
        print(f"  Lowercase: {'Yes' if use_lower else 'No'}")
        print(f"  Numbers: {'Yes' if use_digits else 'No'}")
        print(f"  Special: {'Yes' if use_special else 'No'}")
    print("-" * 60)


def handle_validate():
    """Handle password validation"""
    print("\n" + "-" * 60)
    print("  VALIDATE PASSWORD")
    print("-" * 60)
    
    user_password = input("\nEnter password to validate: ")
    
    if not user_password:
        print("❌ No password entered!")
        return
    
    result = validate_password(user_password)
    display_validation_result(result)
    
    # Give suggestions based on strength
    if result["Strength"] == "Weak":
        print("\n💡 Tip: Use the generator to create a strong password!")
    elif result["Strength"] == "Medium":
        print("\n💡 Tip: Add more character types for better security!")


def handle_generate_and_validate():
    """Generate a password and immediately validate it"""
    print("\n" + "-" * 60)
    print("  GENERATE & VALIDATE")
    print("-" * 60)
    
    # Get password length
    length = get_password_length()
    
    # Get preferences
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_special = input("Include special characters? (y/n): ").lower() == "y"
    
    # Generate password
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    
    if password.startswith("Error"):
        print(f"\n❌ {password}")
        return
    
    # Display generated password
    print("\n" + "-" * 60)
    print(f"  Generated Password: {password}")
    print("-" * 60)
    
    # Validate it
    result = validate_password(password)
    display_validation_result(result)


def display_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("  PASSWORD GENERATOR & VALIDATOR")
    print("=" * 60)
    print("1. Generate password")
    print("2. Validate password")
    print("3. Generate and validate")
    print("4. Exit")
    print("=" * 60)


def main():
    """Main program loop"""
    print("\n" + "=" * 60)
    print("  WELCOME TO PASSWORD TOOL")
    print("=" * 60)
    print("  Create secure passwords and check password strength!")
    print("=" * 60)
    
    while True:
        display_menu()
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            handle_generate()
        
        elif choice == '2':
            handle_validate()
        
        elif choice == '3':
            handle_generate_and_validate()
        
        elif choice == '4':
            print("\n" + "=" * 60)
            print("  Thank you for using Password Tool!")
            print("=" * 60)
            print("  💡 Remember: Never share your passwords!")
            print("=" * 60)
            print("\nGoodbye! 🔐\n")
            break
        
        else:
            print("\n❌ Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()