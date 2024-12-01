import string
from time import sleep


def main():
    cascade_print(input("Type Anything! "), 0.05)


def cascade_print(text: str, seconds: float) -> None:
    """
    Procedure to output text to terminal in a cascading fashion.

    Args:
        text (str)      : The text to be outputted cascadingly.
        seconds (float) : The amount of delay between the printing
                          of each character in text.

    Returns:
        None
    """
    sentence = []
    for char in range(len(text)): # char is returned as index (0,1,2,3, ...)
        current_char = text[char]
        if current_char.isupper():
            checker(
                 string.ascii_uppercase, 
                 sentence, 
                 seconds, 
                 current_char, 
                 char
            )
        elif current_char.islower():
            checker(
                 string.ascii_lowercase, 
                 sentence, 
                 seconds, 
                 current_char, 
                 char
            )
        elif current_char in string.punctuation:
            checker(
                 string.punctuation, 
                 sentence, 
                 seconds, 
                 current_char, 
                 char
            )
        elif current_char.isdigit():
            checker(
                 string.digits, 
                 sentence, 
                 seconds, 
                 current_char, 
                 char
            )
        elif current_char.isspace():
                    sentence.append(" ")


def checker(stringtype, sen: str, delay: float, current_letter: str, idx: int) -> None:
    """
    Args:
        stringtype          : The type of string, whether it's alphabet, digits, punctuation, etc.
        sen (str)           : The string it is checking currently.
        delay (float)       : The amount of delay between the printing of each character in text.
        current_letter (str): The letter this procedure is currently checking.
        idx (int)           : Index of the string.

    Returns:
        None
    """
    _ = True
    for c in stringtype:
        if _:
            sen.append(c)
            print(*sen, sep="")
            sleep(delay)
            _ = False

        else:
            sen[idx] = c 
            print(*sen, sep="")
            sleep(delay)

        if c == current_letter:
            return


if __name__ == "__main__":
     main()