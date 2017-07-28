from shutil import copyfile
import sys
import os.path
import xml.etree.ElementTree as ET

data_file_name = "chn_data.xml"
data = None
tree = None
paths = None
names = None
src_path = None
dest_path = None
file_name = None
new_style = None
current_style = None

#reads the style sheet for the name of the current style
def get_current_style(file_path):
    file = open(file_path, "r")
    line = file.readline()
    isSlash = False
    isStar = False
    isComment = False
    line = line.replace("/", "")
    line = line.replace("*", "")
    line = line.replace("\n", "")
    return line

#creates xml document, creating the root tag: data
def create_data_file():
    global tree, data, paths, names, src_path, dest_path, file_name
    data = ET.Element("data")
    #paths: child to data, contains paths to src and dest folders of css files
    paths = ET.SubElement(data, "paths")
    #names: child to data, contains names of current_style and the name of the css file to be replaced
    names = ET.SubElement(data, "names")
    src_path = ET.SubElement(paths, "src_path")
    src_path.text = "L:/Workspace/WebDev/SimpleWebSite/inactive_styles/"
    dest_path = ET.SubElement(paths, "dest_path")
    dest_path.text = "L:/Workspace/WebDev/SimpleWebSite/css/"
    file_name = ET.SubElement(names, "file_name")
    file_name.text = "style.css"

    tree = ET.ElementTree(data)
    tree.write(data_file_name)

def console_command_handle(args):
    #valid commands: -p, --path, --src, --dst
    try:
        if args[1] == "-p" or args[1] == "--path":
            print("Press CTRL + C to cancel.")
            src_path_str = input("Enter src path: ")
            dest_path_str = input("Enter dest path: ")
            if not src_path_str == "%%":
                src_path.text = src_path_str
            if not dest_path_str == "%%":
                dest_path.text = dest_path_str
        elif args[1] == "-src":
            if len(args) < 3:
                print("Error: You need to enter a path.")
                quit()
            elif len(args) > 3:
                print("Error: Too many arguments.")
                quit()
            src_path.text = args[2]
        elif args[1] == "-dst":
            if len(args) < 3:
                print("Error: You need to enter a path.")
                quit()
            elif len(args) > 3:
                print("Error: Too many arguments.")
                quit()
            dest_path.text = args[2]
        elif args[1] == "help":
            pass
        else:
            print("Error: \"" + args[1] + "\" is not a valid chn command.")
            quit()
    except KeyboardInterrupt:
        quit()

    tree.write(data_file_name)

try:
    tree = ET.parse(data_file_name)
    data = tree.getroot()
    paths = data.find("paths")
    names = data.find("names")
    src_path = paths.find("src_path")
    dest_path = paths.find("dest_path")
    file_name = names.find("file_name")
except:
    create_data_file()

available_styles = ["light_blue", "dark_blue", "blue_orange"]
actual_style_names = ["light_blue.css", "dark_blue.css", "dark_blue_orange.css"]
current_style = actual_style_names[available_styles.index(get_current_style(dest_path.text + file_name.text))]

console_args = sys.argv
if console_args[1][0] == "-":
    console_command_handle(console_args)
elif len(console_args) == 2:

    try:
        style_arg = int(console_args[1])
        new_style = actual_style_names[style_arg]
    except (ValueError, TypeError):
        style_arg = str(console_args[1])
        if style_arg not in available_styles:
            print("Please enter a valid style.")
            quit()
        new_style = actual_style_names[available_styles.index(str(style_arg))]

    copyfile(dest_path.text + file_name.text, src_path.text + current_style)
    copyfile(src_path.text + new_style, dest_path.text + file_name.text)
elif len(console_args) == 1:
    print(current_style)
    quit()


tree.write(data_file_name)
