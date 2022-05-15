def get_rgb(r: int, g: int, b: int) -> str:
    """
    Changes your color to the chosen value
    :param r: Red value (0 - 255)
    :param g: Green value (0 - 255)
    :param b: Blue value (0 - 255)
    :return: Character of the transformation
    """
    return f"\033[38;2;{r};{g};{b}m"


def get_hex(hexadecimal: str) -> str:
    """
    Changes your color to the chosen value
    :param hexadecimal: The hexadecimal value of the color
    :return: Character of the transformation
    """
    if hexadecimal[0] == "#":
        hexadecimal = hexadecimal[1:]

    r = int(hexadecimal[:2], 16)
    g = int(hexadecimal[2:4], 16)
    b = int(hexadecimal[4:], 16)

    return get_rgb(r, g, b)

BLACK: str = '\033[30m'
RED: str = '\033[31m'
GREEN: str = '\033[32m'
YELLOW: str = '\033[33m'
BLUE: str = '\033[34m'
PURPLE: str = '\033[35m'
CYAN: str = '\033[36m'
WHITE: str = '\033[37m'

LIGHT_BLACK: str = '\033[90m'
LIGHT_RED: str = '\033[91m'
LIGHT_GREEN: str = '\033[92m'
LIGHT_YELLOW: str = '\033[93m'
LIGHT_BLUE: str = '\033[94m'
LIGHT_PURPLE: str = '\033[95m'
LIGHT_CYAN: str = '\033[96m'
LIGHT_WHITE: str = '\033[97m'

STOP: str = '\033[39m'
