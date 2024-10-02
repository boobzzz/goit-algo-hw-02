from collections import deque
import math


def check_palindrome(phrase: str) -> bool:
    result = True
    phrase_arr = list(phrase.replace(' ', '').lower())
    dec = deque(phrase_arr)

    for i in range(math.floor(len(dec) / 2)):
        if dec.popleft() != dec.pop():
            result = False
            return result

    return result


def main():
    strings = ["riddle", "tenet", "noon", "No devil lived on"]

    for s in strings:
        message = 'Phrase is not a palindrome'
        is_palindrome = check_palindrome(s)
        if is_palindrome:
            message = 'Phrase is a palindrome'
        print(message)


if __name__ == "__main__":
    main()
