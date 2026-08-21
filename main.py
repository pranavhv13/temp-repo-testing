import random


def generate_random_numbers(count=10, start=0, end=100):
    return [random.randint(start, end) for _ in range(count)]


def simulate_dice_rolls(rolls=10):
    return [random.randint(1, 6) for _ in range(rolls)]


def random_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(length))


def main():
    numbers = generate_random_numbers(12, 1, 50)
    dice = simulate_dice_rolls(8)
    password = random_password(16)

    print("Random numbers:", numbers)
    print("Dice rolls:", dice)
    print("Random password:", password)


if __name__ == "__main__":
    main()
