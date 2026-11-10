import os
SEQUENCE_START = "\033[90m"
SEQUENCE_END = "\033[0m"
def log(text):
    if os.getenv("DEBUG") == "True":
        print(f" {SEQUENCE_START}{text}{SEQUENCE_END}")
#"\033[90m" is ANSI escape code for gray color and "\033[0m" is ANSI escape code to reset the color back to default.]"

# \033 => is signal to command prompt/terminal that the following characters are ANSI escape codes and not normal text.
# [ is the start of command
# 90 is for gray color
#  m end of the command
# to stop that command we use \033[0m which is ANSI escape code to reset the color back to default.
#\033[90m<text>\033[0m => this will print the <text> in gray color in the terminal/command prompt.

#in windows power shell if you want to print the text in gray color then you can use the following command:
# python it goes interpreter mode and then you can use the following command to print the text in gray color:
# >>> print("\033[90mHello\033[0m")
# Hello
# >>> print("\033[91mHello\033[0m")
# Hello
# >>>