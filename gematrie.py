import sys


def alphabeticValueSum(word):
    word = word.lower()
    return sum(ord(char) - ord("a") + 1 for char in word if char.isalpha())


def main():
    if len(sys.argv) < 2:
        print("Usage: python gematrie.py <word> [<word> ...]")
        sys.exit(1)

    sum = 0
    for word in sys.argv[1:]:
        val = alphabeticValueSum(word)
        print(f"{word}: {val}")
        sum += val

    print(f"\nSum: {sum}")


if __name__ == "__main__":
    main()
