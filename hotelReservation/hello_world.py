import string
from time import sleep


def main():
    cascadeprint(input("Type Anything! "), 0.05)


def cascadeprint(text, seconds):
    sentence = list()
    for char in range(len(text)): # char is returned as index (0,1,2,3, ...)
        current_char = text[char]
        if current_char.isupper():
            checker(string.ascii_uppercase, sentence, seconds, current_char, char)
        elif current_char.islower():
            checker(string.ascii_lowercase, sentence, seconds, current_char, char)
        elif current_char in string.punctuation:
            checker(string.punctuation, sentence, seconds, current_char, char)
        elif current_char.isdigit():
            checker(string.digits, sentence, seconds, current_char, char)
        elif current_char.isspace():
                    sentence.append(" ")


def checker(stringtype, sen, delay, current_letter, i):
    _ = True
    for c in stringtype:
        if _:
            sen.append(c)
            print(*sen, sep="")
            sleep(delay)
            _ = False
        else:
            sen[i] = c 
            print(*sen, sep="")
            sleep(delay)
        if c == current_letter:
            break


if __name__ == "__main__":
     main()