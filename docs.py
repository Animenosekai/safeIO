from markdownCreation import *
from safeIO import TextFile
scriptFile = TextFile("safeIO.py")

README = MarkdownFile()
README.add(Header("safeIO", 1, README))
README.add(Quote(" Safely make I/O operations to files in Python even from multiple threads... and more!"))
README.add(Header("Table of Content", 1, README))
README.add(TableOfContent(README, 3))

def removeSpaceBefore(string):
    string = str(string)
    try:
        curentCharacter = string[0]
    except:
        return string
    while curentCharacter == " ":
        try:
            string = string[1:]
            curentCharacter = string[0]
        except:
            break

    return string

currentlyDocs = False
for line in scriptFile:
    line = line.replace("\n", "")
    if "            " in line:
        continue
    if "def _" in line:
        continue
    elif "def " in line:
        currentlyDocs = True
        currentMethod = removeSpaceBefore(line).replace(" ", "").replace("def", "").replace(":", "")
        name = currentMethod[:currentMethod.find("(")]
        README.add(Header(name, 3, README))
        README.add(ItalicText(currentMethod))
    elif '"""' in line:
        if currentlyDocs:
            currentlyDocs = False
        else:
            currentlyDocs = True
    elif "class " in line:
        README.add(Separator())
        README.add(Header(line.replace("class ", "").replace(":", ""), 2, README))
    elif not currentlyDocs:
        README.add(Quote(removeSpaceBefore(line)))
    

README.save("README.md")
print(README)