import subprocess

readfile = None
writefile = None
isignored = False;
isfileexists = True

inactive_style_names = ["../inactive_styles/light_blue.css ", "../inactive_styles/dark_blue.css ", "../inactive_styles/dark_blue_orange.css "]
file_path = "../css/style.css"


try:
    readfile = open("ignore_state.txt")
except FileNotFoundError:
    isfileexists = False

if isfileexists:
    line = readfile.readline()
    if line == "0":
        isignored = False
    elif line == "1":
        isignored = True


writefile = open("ignore_state.txt", "w")
if isignored:
    writefile.write("0")
    subprocess.call('git update-index --no-assume-unchanged ' + file_path + inactive_style_names[0] + inactive_style_names[1] + inactive_style_names[2], shell = True)
else:
    writefile.write("1")
    subprocess.call('git update-index --assume-unchanged ' + file_path + inactive_style_names[0] + inactive_style_names[1] + inactive_style_names[2], shell = True)
