import getpass

common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome"
]


def check_character_types(password):
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    for c in password:
        if c.isupper():
            has_upper = True

        if c.islower():
            has_lower = True

        if c.isdigit():
            has_number = True

        if not c.isalnum():
            has_special = True

    return has_upper, has_lower, has_number, has_special


def check_common_password(password):
    return password.lower() in common_passwords


def calculate_strength(password, has_upper, has_lower,
                       has_number, has_special, is_common):

    score = 0

    if len(password) >= 8:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_number:
        score += 1

    if has_special:
        score += 1

    if is_common:
        return "Weak", score

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score


def give_recommendations(password, has_upper, has_lower,
                         has_number, has_special, is_common):

    recommendations = []

    if len(password) < 12:
        recommendations.append("Use at least 12 characters.")

    if not has_upper:
        recommendations.append("Add uppercase letters.")

    if not has_lower:
        recommendations.append("Add lowercase letters.")

    if not has_number:
        recommendations.append("Add numbers.")

    if not has_special:
        recommendations.append("Add special characters such as !, @, or #.")

    if is_common:
        recommendations.append("Avoid common or easily guessed passwords.")

    return recommendations


def main():

    print("=" * 45)
    print("       PASSWORD SECURITY ANALYZER")
    print("=" * 45)

    password = getpass.getpass("Enter password: ")

    has_upper, has_lower, has_number, has_special = \
        check_character_types(password)

    is_common = check_common_password(password)

    strength, score = calculate_strength(
        password,
        has_upper,
        has_lower,
        has_number,
        has_special,
        is_common
    )

    print("\nPassword Analysis")
    print("-" * 25)

    print("Length:", len(password))
    print("Uppercase:", "Yes" if has_upper else "No")
    print("Lowercase:", "Yes" if has_lower else "No")
    print("Number:", "Yes" if has_number else "No")
    print("Special character:", "Yes" if has_special else "No")
    print("Common password:", "Yes" if is_common else "No")

    print("\nScore:", score, "/ 5")
    print("Strength:", strength)

    recommendations = give_recommendations(
        password,
        has_upper,
        has_lower,
        has_number,
        has_special,
        is_common
    )

    if recommendations:
        print("\nSecurity Recommendations")
        print("-" * 30)

        for recommendation in recommendations:
            print("- " + recommendation)
    else:
        print("\nNo basic improvements detected.")


if __name__ == "__main__":
    main()