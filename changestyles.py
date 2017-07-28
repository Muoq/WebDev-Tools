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
if (len(console_args) > 2):
    print("You can only enter one command")
    quit()
elif(len(console_args) == 1):
    print(current_style)
    quit()

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

tree.write(data_file_name)
