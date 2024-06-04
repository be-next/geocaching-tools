# Count the number of letters in each word given in argument

import sys


def count_letters(word):
    return len(word)


def main():
    if len(sys.argv) < 2:
        print("Usage: python letter_count.py <word> [<word> ...]")
        sys.exit(1)

    for word in sys.argv[1:]:
        print(f"{word}: {count_letters(word)}")


# execute main() only if this script is run as the main program
if __name__ == "__main__":
    main()
