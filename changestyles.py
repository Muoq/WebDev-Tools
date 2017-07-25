from shutil import copyfile
import sys

style_arg = sys.argv[1]
available_styles = ["light_blue", "dark_blue", "blue_orange"]
actual_style_names = ["light_blue", "dark_blue", "dark_blue_orange"]

try:
    style_arg = int(style_arg)
    actual_style_path = "../inactive_styles/" + str(actual_style_names[style_arg]) + ".css"
except ValueError:
    if style_arg in available_styles:
        actual_style_path = "../inactive_styles/" + str(actual_style_names[available_styles.index(style_arg)]) + ".css"
    else:
        print("Please enter a valid style.")
        quit()


copyfile(actual_style_path, "../css/style.css")
