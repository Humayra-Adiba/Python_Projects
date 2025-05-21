import random
import string

def get_character_pool(include_letters: bool, include_digits: bool, include_symbols: bool) -> str:
    pool = ''
    if include_letters:
        pool += string.ascii_letters
    if include_digits:
        pool += string.digits
    if include_symbols:
        pool += string.punctuation
    return pool

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter password length: "))
        include_letters = input("Include letters (a-z, A-Z)? (y/n): ").strip().lower() == 'y'
        include_digits = input("Include digits (0-9)? (y/n): ").strip().lower() == 'y'
        include_symbols = input("Include symbols (!@#$ etc)? (y/n): ").strip().lower() == 'y'

        character_pool = get_character_pool(include_letters, include_digits, include_symbols)
        password = generate_password(length, character_pool)

        print(f"\nGenerated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")


def generate_password(length: int, character_pool: str) -> str:
    if not character_pool:
        raise ValueError("Character pool is empty. Please enable at least one character type.")
    return ''.join(random.choice(character_pool) for _ in range(length))


if __name__ == "__main__":
    main()
