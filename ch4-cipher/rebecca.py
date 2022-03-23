import sys
import os
import random
from collections import defaultdict, Counter


def main():
    message = input("Enter plaintext or ciphertext: ")
    process = input("Enter 'encrypt' or 'decrypt': ")
    while process not in ("encrypt", "decrypt"):
        process = input("Invalid process. Enter 'encrypt' or 'decrypt': ")
    shift = int(input("Shift value (1-366) =  "))
    while not 1 <= shift <= 366:
        shift = int(input("Invalid valie. Enter digit from 1 to 366: "))
    infile = input("Enter filename with extension: ")

    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile), file=sys.stderr)
        sys.exit(1)
    text = load_file(infile)
    char_dict = make_dict(text, shift)

    if process == "encrypt":
        ciphertext = encrypt(message, char_dict)
        if check_for_fail(ciphertext):
            print("\nProblem finding unique keys.", file=sys.stderr)
            print("Try again, change message, or change code book.\n", file=sys.stderr)
            sys.exit()
        print("\nCharacter and number of occurences in char_dict: \n")
        print(
            "{:>10}{:>10}{:>10}".format(
                repr(key)[1:-1], str(ord(key)), len(char_dict[key])
            )
        )
        print("\nNumber of distinct characters: {}".format(len(char_dict)))
        print("Total number of characters: {:,}\n".format(len(text)))
        print("encrypted ciphertext = \n {}\n".format(ciphertext))
        print("decrypted plaintext = ")
        for i in cyphertext:
            print(text[i - shift], end="", flush=True)

    elif process == "decrypt":
        plaintext = decrypt(message, text, shift)
        print("\ndecrypted plaintext = \n {}".format(plaintext))
