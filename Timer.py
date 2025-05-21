import time

def get_user_input() -> int:
    try:
        return int(input("Enter time in seconds: "))
    except ValueError:
        print(" Please enter a valid number.")
        return 0


def format_time(seconds: int) -> str:
    minutes, secs = divmod(seconds, 60)
    return f"{minutes:02d}:{secs:02d}"


def main() -> None:
    seconds = get_user_input()
    if seconds > 0:
        countdown(seconds)


def countdown(seconds: int) -> None:
    while seconds >= 0:
        print(f"\rTime left: {format_time(seconds)}", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's up! ")


if __name__ == "__main__":
    main()
