def get_rgb(r: int, g: int, b: int) -> str:
    """
    Changes your highlight to the chosen value
    :param r: Red value (0 - 255)
    :param g: Green value (0 - 255)
    :param b: Blue value (0 - 255)
    :return: Character of the transformation
    """
    return f"\033[48;2;{r};{g};{b}m"


def get_hex(hexadecimal: str) -> str:
    """
    Changes your highlight to the chosen value
    :param hexadecimal: The hexadecimal value of the color
    :return: Character of the transformation
    """
    if hexadecimal[0] == "#":
        hexadecimal = hexadecimal[1:]

    r = int(hexadecimal[:2], 16)
    g = int(hexadecimal[2:4], 16)
    b = int(hexadecimal[4:], 16)

    return get_rgb(r, g, b)


BLACK: str = '\033[40m'
RED: str = '\033[41m'
GREEN: str = '\033[42m'
YELLOW: str = '\033[43m'
BLUE: str = '\033[44m'
PURPLE: str = '\033[45m'
CYAN: str = '\033[46m'
WHITE: str = '\033[47m'

LIGHT_BLACK: str = '\033[100m'
LIGHT_RED: str = '\033[101m'
LIGHT_GREEN: str = '\033[102m'
LIGHT_YELLOW: str = '\033[103m'
LIGHT_BLUE: str = '\033[104m'
LIGHT_PURPLE: str = '\033[105m'
LIGHT_CYAN: str = '\033[106m'
LIGHT_WHITE: str = '\033[107m'

STOP: str = '\033[49m'
