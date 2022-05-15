# <p id="title">Text Editing</p>

Set of variables and functions for text editing.

Python library by LassaInora.

--------
## Summary

- **[Links](#links)**
- **[Contacts](#contact)**
- **[Character attributes](#character_attributes)**
  - ***[variables](#character_attributes_var)***
- **[Color](#color)**
  - ***[variables](#color_var)***
  - ***[functions](#color_functions)***
- **[Font](#font)**
  - ***[variables](#font_var)***
- **[Highlight](#highlight)**
  - ***[variables](#highlight_var)***
  - ***[functions](#highlight_functions)***
--------

## <p id="links">Links</p>

- [Personal GitHub](https://github.com/LassaInora)
- [GitHub project](https://github.com/LassaInora/LassaLib)
- [Website project](https://lassainora.fr/projet/librairies/lassalib)

## <p id="contact">Contacts</p>

- [Personal email](mailto:axelleviandier@lassainora.fr)
- [Professional email](mailto:lassainora@lassainora.fr)
--------
## <p id="character_attributes">Character attributes:</p>

### <p id="character_attributes_var">variables</p>

- BOLD
  - \033[1m
- NO_BOLD
  - <span style="color: #FF0000; text-decoration: underline;">/!\\</span><span style="color: #FF0000;"> Not widely supported.</span>
  - \033[21m
- LOW_INTENSITY
  - <span style="color: #FF0000; text-decoration: underline;">/!\\</span><span style="color: #FF0000;"> Not widely supported.</span>
  - \033[2m
- NO_LOW_INTENSITY
  - \033[22m
- ITALIC 
  - <span style="color: #FF0000; text-decoration: underline;">/!\\</span><span style="color: #FF0000;"> Not widely supported. Sometimes treated as the reverse.</span>
  - \033[3m
- NO_ITALIC
  - \033[23m
- UNDERLINE
  - \033[4m
- NO_UNDERLINE
  - \033[24m
- SLOWLY_FLASHING 
  - \033[5m
- NO_SLOWLY_FLASHING
  - \033[25m
- RAPIDLY_FLASHING 
  - <span style="color: #FF0000; text-decoration: underline;">/!\\</span><span style="color: #FF0000;"> MS-DOS ANSI.SYS; Not widely supported.</span>
  - \033[6m
- NO_RAPIDLY_FLASHING
  - \033[26m
- NEGATIVE
  - \033[7m
- NO_NEGATIVE
  - \033[27m
- HIDDEN 
  - <span style="color: #FF0000; text-decoration: underline;">/!\\</span><span style="color: #FF0000;"> Not widely supported.</span>
  - \033[8m
- NO_HIDDEN
  - \033[28m
- STRIKETHROUGH 
  - <span style="color: #FF0000; text-decoration: underline;">/!\\</span><span style="color: #FF0000;"> Not widely supported.</span>
  - \033[9m
- NO_STRIKETHROUGH
  - \033[29m
- STOP_ALL
  - \033[0m

## <p id="color">Color:</p>

### <p id="color_var">variables</p>

- BLACK
  - \033[30m
- RED
  - \033[31m
- GREEN
  - \033[32m
- YELLOW
  - \033[33m
- BLUE
  - \033[34m
- PURPLE
  - \033[35m
- CYAN
  - \033[36m
- WHITE
  - \033[37m

+ LIGHT_BLACK
  + \033[90m
+ LIGHT_RED
  + \033[91m
+ LIGHT_GREEN
  + \033[92m
+ LIGHT_YELLOW
  + \033[93m
+ LIGHT_BLUE
  + \033[94m
+ LIGHT_PURPLE
  + \033[95m
+ LIGHT_CYAN
  + \033[96m
+ LIGHT_WHITE
  + \033[97m

* STOP
  * \033[39m

### <p id="color_functions">functions</p>

- get_rgb :
  - Changes your color to the chosen value 
- get_hex : 
  - Changes your color to the chosen value

## <p id="font">Font:</p>

<span style="color: #FF0000; text-decoration: underline;">/!\ </span><span style="color: #FF0000;">Few terminals support this library.</span>

### <p id="font_var">variables</p>

- ONE (The font given by this character is currently unknown.)
  - \033[11m
- TWO (The font given by this character is currently unknown.)
  - \033[12m
- THREE (The font given by this character is currently unknown.)
  - \033[13m
- FOUR (The font given by this character is currently unknown.)
  - \033[14m
- FIVE (The font given by this character is currently unknown.)
  - \033[15m
- SIX (The font given by this character is currently unknown.)
  - \033[16m
- SEVEN (The font given by this character is currently unknown.)
  - \033[17m
- EIGHT (The font given by this character is currently unknown.)
  - \033[18m
- NINE (The font given by this character is currently unknown.)
  - \033[19m
- FRAKTUR
  - \033[20m

+ STOP
  + \033[10m

## <p id="character_attributes">Character attributes:</p>

### <p id="highlight_var">variables</p>

- BLACK
  - \033[40m
- RED
  - \033[41m
- GREEN
  - \033[42m
- YELLOW
  - \033[43m
- BLUE
  - \033[44m
- PURPLE
  - \033[45m
- CYAN
  - \033[46m
- WHITE
  - \033[47m

+ LIGHT_BLACK
  + \033[100m
+ LIGHT_RED
  + \033[101m
+ LIGHT_GREEN
  + \033[102m
+ LIGHT_YELLOW
  + \033[103m
+ LIGHT_BLUE
  + \033[104m
+ LIGHT_PURPLE
  + \033[105m
+ LIGHT_CYAN
  + \033[106m
+ LIGHT_WHITE
  + \033[107m

* STOP
  * \033[49m

### <p id="highlight_functions">functions</p>

- get_rgb :
  - Changes your color to the chosen value 
- get_hex : 
  - Changes your color to the chosen value
