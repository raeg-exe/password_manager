import secrets
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()+"
ALL_CHARS = LETTERS + NUMBERS + SYMBOLS

MIN_LENGTH = 8


def generate_password(length):
    if length < MIN_LENGTH:
        raise ValueError(f"Password must be at least {MIN_LENGTH} characters.")

    # ensure at least one of each type
    chars = [
        secrets.choice(LETTERS),
        secrets.choice(NUMBERS),
        secrets.choice(SYMBOLS),
    ]

    # fill the rest with fully random chars
    for _ in range(length - len(chars)):
        chars.append(secrets.choice(ALL_CHARS))

    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def score_password(password):
    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in SYMBOLS for c in password)

    score = 0

    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= MIN_LENGTH:
        score += 1

    score += has_lower + has_upper + has_digit + has_symbol

    if score >= 7:
        label = "Very strong"
    elif score >= 5:
        label = "Strong"
    elif score >= 3:
        label = "Medium"
    else:
        label = "Weak"

    return score, label


def get_int(prompt, min_value=None, max_value=None):
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
            continue

        return value


def main():
    print("Starting password generator...")

    length = get_int(
        f"How many characters would you like your password to be (min {MIN_LENGTH}): ",
        min_value=MIN_LENGTH,
    )

    print("Generating password...")
    password = generate_password(length)

    print("\nYour password is:", password)
    score, label = score_password(password)
    print(f"Password strength: {label} (score: {score})")


if __name__ == "__main__":
    main()