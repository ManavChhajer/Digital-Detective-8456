"""Convert a non-negative decimal integer to binary and hexadecimal."""


def convert(n: int) -> tuple[str, str]:
    return format(n, "b"), format(n, "X")


def main() -> None:
    raw = input("Enter a whole number (0 or more): ").strip()
    if not raw.isdigit():
        print("Please enter digits only.")
        return
    n = int(raw)
    b, h = convert(n)
    print(f"Decimal {n} -> Binary {b} -> Hex 0x{h}")


if __name__ == "__main__":
    main()
