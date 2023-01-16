BRAILLE_BASE_CODE = 0x2800


def dots(*args):
    base = BRAILLE_BASE_CODE

    for dot in list(args):
        if dot < 1 or dot > 8:
            print("Dot index must in range 1 to 8")
            return 0x00
        base += 1 << (dot - 1)
    return chr(base)


PREFIX = {
    "TODO2":     dots(4, 5),
    "greek":     dots(4, 5, 6),
    "TODO4":     dots(5),
}

NUMBERS = {
    '1': dots(3, 4, 5, 6) + dots(1),
    '2': dots(3, 4, 5, 6) + dots(1, 2),
    '3': dots(3, 4, 5, 6) + dots(1, 4),
    '4': dots(3, 4, 5, 6) + dots(1, 4, 5),
    '5': dots(3, 4, 5, 6) + dots(1, 5),
    '6': dots(3, 4, 5, 6) + dots(1, 2, 4),
    '7': dots(3, 4, 5, 6) + dots(1, 2, 4, 5),
    '8': dots(3, 4, 5, 6) + dots(1, 2, 5),
    '9': dots(3, 4, 5, 6) + dots(2, 4),
    '0': dots(3, 4, 5, 6) + dots(2, 4, 5),
}

SYMBOLS = {
    '@': dots(1, 5, 6),
    ',': dots(2),
    ';': dots(2, 3),
    ':': dots(2, 5),
    '/': dots(2, 5, 6),
    '?': dots(2, 6),
    '+': dots(2, 3, 5),
    '=': dots(2, 3, 5, 6),
    '~': dots(2, 3, 4, 6),
    '"': dots(2, 3, 6),
    '*': dots(3, 5),
    '°': dots(3, 5, 6),
    '#': dots(3, 4, 5, 6) + dots(1, 3),
    '.': dots(3),
    '-': dots(3, 6),
    '$': dots(4) + dots(1, 4, 5),
    '€': dots(4) + dots(1, 2, 3),
    '£': dots(4) + dots(1, 2, 3),
    '^': dots(4) + dots(2, 3, 4, 6),
    '|': dots(4, 5, 6) + dots(1, 2, 4, 5, 6),
    '`': dots(4, 5, 6) + dots(2, 3, 4, 6),
    '{': dots(5) + dots(1, 2, 3),
    '}': dots(4, 5, 6) + dots(2),
    '>': dots(5) + dots(1, 3, 5),
    '<': dots(5) + dots(2, 4, 6),
    '&': dots(5) + dots(1, 2, 3, 4, 6),
    '[': dots(5) + dots(1, 2, 3, 5, 6),
    '[': dots(5) + dots(2, 3, 4, 5, 6),
    '´': dots(5) + dots(2, 3, 4, 6),
    '(': dots(5) + dots(1, 2, 6),
    ')': dots(5) + dots(3, 4, 5),
    '!': dots(5) + dots(2, 3, 5)

}

ALPHABET = {
    'a': dots(1),
    'á': dots(1, 2, 3, 5, 6),
    'â': dots(1, 6),
    'à': dots(1, 2, 4, 6),
    'ã': dots(3, 4, 5),
    'b': dots(1, 2),
    'c': dots(1, 4),
    'ç': dots(1, 2, 3, 4, 6),
    'd': dots(1, 4, 5),
    'e': dots(1, 5),
    'é': dots(1, 2, 3, 4, 5, 6),
    'ê': dots(1, 2, 6),
    'f': dots(1, 2, 4),
    'g': dots(1, 2, 4, 5),
    'h': dots(1, 2, 5),
    'i': dots(2, 4),
    'í': dots(3, 4),
    'j': dots(2, 4, 5),
    'k': dots(1, 3),
    'l': dots(1, 2, 3),
    'm': dots(1, 3, 4),
    'n': dots(1, 3, 4, 5),
    'o': dots(1, 3, 5),
    'ó': dots(3, 4, 6),
    'ô': dots(1, 4, 5, 6),
    'õ': dots(2, 4, 6),
    'p': dots(1, 2, 3, 4),
    'q': dots(1, 2, 3, 4, 5),
    'r': dots(1, 2, 3, 5),
    's': dots(2, 3, 4),
    't': dots(2, 3, 4, 5),
    'u': dots(1, 3, 6),
    'ú': dots(2, 3, 4, 5, 6),
    'v': dots(1, 2, 3, 6),
    'w': dots(2, 4, 5, 6),
    'x': dots(1, 3, 4, 6),
    'y': dots(1, 3, 4, 5, 6),
    'z': dots(1, 3, 5, 6),

    'A':  dots(4, 6) + dots(1),
    'Á':  dots(4, 6) + dots(1, 2, 3, 5, 6),
    'Â':  dots(4, 6) + dots(1, 6),
    'À':  dots(4, 6) + dots(1, 2, 4, 6),
    'Ã':  dots(4, 6) + dots(3, 4, 5),
    'B':  dots(4, 6) + dots(1, 2),
    'C':  dots(4, 6) + dots(1, 4),
    'Ç':  dots(4, 6) + dots(1, 2, 3, 4, 6),
    'D':  dots(4, 6) + dots(1, 4, 5),
    'E':  dots(4, 6) + dots(1, 5),
    'É':  dots(4, 6) + dots(1, 2, 3, 4, 5, 6),
    'Ê':  dots(4, 6) + dots(1, 2, 6),
    'F':  dots(4, 6) + dots(1, 2, 4),
    'G':  dots(4, 6) + dots(1, 2, 4, 5),
    'H':  dots(4, 6) + dots(1, 2, 5),
    'I':  dots(4, 6) + dots(2, 4),
    'Í':  dots(4, 6) + dots(3, 4),
    'J':  dots(4, 6) + dots(2, 4, 5),
    'K':  dots(4, 6) + dots(1, 3),
    'L':  dots(4, 6) + dots(1, 2, 3),
    'M':  dots(4, 6) + dots(1, 3, 4),
    'N':  dots(4, 6) + dots(1, 3, 4, 5),
    'O':  dots(4, 6) + dots(1, 3, 5),
    'Ó':  dots(4, 6) + dots(3, 4, 6),
    'Ô':  dots(4, 6) + dots(1, 4, 5, 6),
    'Õ':  dots(4, 6) + dots(2, 4, 6),
    'P':  dots(4, 6) + dots(1, 2, 3, 4),
    'Q':  dots(4, 6) + dots(1, 2, 3, 4, 5),
    'R':  dots(4, 6) + dots(1, 2, 3, 5),
    'S':  dots(4, 6) + dots(2, 3, 4),
    'T':  dots(4, 6) + dots(2, 3, 4, 5),
    'U':  dots(4, 6) + dots(1, 3, 6),
    'Ú':  dots(4, 6) + dots(2, 3, 4, 5, 6),
    'V':  dots(4, 6) + dots(1, 2, 3, 6),
    'W':  dots(4, 6) + dots(2, 4, 5, 6),
    'X':  dots(4, 6) + dots(1, 3, 4, 6),
    'Y':  dots(4, 6) + dots(1, 3, 4, 5, 6),
    'Z':  dots(4, 6) + dots(1, 3, 5, 6),
}


def decode(text: str):

    response = ""
    for letter in text:
        if letter in NUMBERS:
            response += NUMBERS[letter]

        elif letter.lower() in ALPHABET:
            response += ALPHABET[letter]

        elif letter == ' ':
            response += ' '

        elif letter in SYMBOLS:
            response += SYMBOLS[letter]

        elif letter == "\n":
            response += "\n"

    return response
