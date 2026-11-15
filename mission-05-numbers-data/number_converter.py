"""Convert a positive decimal integer to binary and hexadecimal."""

def main():
    raw_value = input("Enter a positive decimal integer: ").strip()

    try:
        number = int(raw_value)
        if number <= 0:
            print("Please enter an integer greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    print(f"Decimal:     {number}")
    print(f"Binary:      {bin(number)[2:]}")
    print(f"Hexadecimal: {hex(number)[2:].upper()}")


if __name__ == "__main__":
    main()
